import os
import sys
import json
import http.server
import socketserver
import threading

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


HOST = 'localhost'
PORT = 18000
HTTP_ROOT = f'http://{HOST}:{PORT}'

os.chdir('./brainhack_book/_build/html')

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return super().do_GET()

server = socketserver.TCPServer((HOST, PORT), HttpRequestHandler)
server.allow_reuse_address = True
def start_server():
    server.serve_forever()

daemon = threading.Thread(name='daemon_server', target=start_server)
daemon.setDaemon(True)
daemon.start()


options = webdriver.ChromeOptions()
options.add_argument('--headless')

capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)


validate_anchors = {}
visited_pages = set()
to_visit_pages = [HTTP_ROOT]

while len(to_visit_pages) > 0:
    page = to_visit_pages.pop(0)
    driver.get(page)
    visited_pages |= { page }
    elems = driver.find_elements_by_xpath('//a[@href]')
    for elem in elems:
        next_page = elem.get_attribute('href')
        if not next_page.startswith(HTTP_ROOT):
            continue
        next_page, anchor, *_ = next_page.split('#') + [None]
        if anchor:
            validate_anchors[next_page] = validate_anchors.get(next_page, set()) | { anchor }
        if next_page in visited_pages:
            continue
        if next_page not in to_visit_pages:
            to_visit_pages += [next_page]

failed_anchors = {}
for page, anchors in validate_anchors.items():
    driver.get(page)
    for anchor in anchors:
        found = driver.find_elements_by_id(anchor)
        if not found:
            failed_anchors[page] = failed_anchors.get(page, set()) | { anchor }

logs = driver.get_log('performance')
failed_requests = {}
for log in logs:
    if '"Network.responseReceived"' not in log['message']:
        continue

    data = json.loads(log['message'])['message']['params']['response']

    # Ignore vendors
    if data['url'].startswith(f'{HTTP_ROOT}/_static/vendor'):
        continue

    if data['status'] >= 400:
        failed_requests[data['url']] = data


if failed_requests:
    print('Failed requests')
    for d in failed_requests.values():
        print(d['url'], d['status'], file=sys.stderr)

if failed_anchors:
    print('Failed anchors')
    for page, anchors in failed_anchors.items():
        print(page, ", ".join(anchors), file=sys.stderr)

if failed_requests or failed_anchors:
    sys.exit(1)

sys.exit(0)