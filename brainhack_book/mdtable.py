from pathlib import Path

import csv

div_h = "-"
div_v = "|"
padding = 2


class MarkdownTable():
    def __init__(self, table, title):
        self.table = table
        self.title = title

    def generate(self, filename):
        header = self.table [0]
        body = self.table [1:]

        # add dividers
        horiz = self.header_div(header)
        header = self.add_div(header)
        body = [self.add_div(row) for row in body]
        mdtable = self.assemble_table(self.title, header, horiz, body)
        self.write_md(filename, mdtable)

    @staticmethod
    def add_div(line):
        div = ''.join([padding * ' ', div_v, padding * ' '])
        return div.join(line)

    @staticmethod
    def header_div(header):
        col_widths = [len(cell) for cell in header]
        horizs = ["-" * w for w in col_widths]
        div = ''.join([padding * div_h, div_v, padding * div_h])
        return div.join(horizs)

    @staticmethod
    def assemble_table(title, header, horiz, body):
        table = [title, header, horiz, *body]
        return [row.rstrip() for row in table]

    @staticmethod
    def write_md(filepath, table):
        # write to a markdown
        md = '\n'.join(table)
        with open(filepath, "w") as f:
            f.write(md)

def parse_affliation(data):
    parsed = data[2:]  # start of header
    return parsed

def read_file(filename, delimiter="\t"):
    if delimiter not in [",", "\t"]:
        print(f"unsupported delimiter `{delimiter}`")
        return

    with open(filename, "r") as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        return list(csv_reader)


if __name__ == '__main__':
    project_root = Path("__file__").parent
    ack_path = project_root / "data" / "acknowledgements.csv"
    table = read_file(ack_path, delimiter=",")
    mder = MarkdownTable(table, title="# Acknowledgements")
    mder.generate(project_root / "brainhack_book" / "acknowledgements.md")

    # aff_path = project_root / "affiliations.csv"
    # aff = read_file(aff_path, delimiter="\t")
