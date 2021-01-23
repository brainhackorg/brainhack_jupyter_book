'''
Author: Hao-Ting Wang
Date: 23-01-2021

Generate Markdown table from csv / tsv file and
append to an existing markdown file containing
page header and other free text paragraph for
acknowledgements and contributions page.

Usage:
>> python brainhack_book/mdtable.py

'''
from pathlib import Path
import csv


div_h = "-"
div_v = "|"
padding = 2

class MarkdownTable():
    '''
    Generate and save markdown table from csv/tsv file,
    append to an existing markdown file.

    inputs
    ------
    table:
        table loaded through csv.reader
        Each row is a list and have the same lenght
        e.g.:
        table = [["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "i", "j"]]

    descriptions:
        List of string where each item is a line
    '''
    def __init__(self, table, descriptions):
        self.table = table
        self.descriptions = descriptions

    def generate(self, filename):
        """
        generate markdown file with a table
        save as a .md file
        """
        header = self.table [0]
        body = self.table [1:]

        # add dividers
        horiz = self.header_div(header)
        header = self.add_div(header)
        body = [self.add_div(row) for row in body]
        # write the table
        mdtable = self.assemble_table(self.descriptions,
            header, horiz, body)
        self.write_md(filename, mdtable)

    @staticmethod
    def add_div(line):
        '''
        add markdown table divider to a row
        '''
        div = ''.join([padding * ' ', div_v, padding * ' '])
        return div.join(line)

    @staticmethod
    def header_div(header):
        '''
        add markdown table horizontal divider bellow header
        '''
        col_widths = [len(cell) for cell in header]
        horizs = ["-" * w for w in col_widths]
        div = ''.join([padding * div_h, div_v, padding * div_h])
        return div.join(horizs)

    @staticmethod
    def assemble_table(title_part, header, horiz, body):
        '''
        assemble header, devider and table body as
        a markdown table
        prepend with exisiting .md file
        '''
        table = title_part + [header, horiz, *body]
        return [row.rstrip() for row in table]

    @staticmethod
    def write_md(filepath, table):
        '''
        write output from `assemble_table` to a .md file
        '''
        md = '\n'.join(table)
        with open(filepath, "w") as f:
            f.write(md)

def parse_affliation(data):
    parsed = data[2:]  # start of header
    return parsed

def read_tablefile(filename, delimiter="\t"):
    '''
    Read tsv or csv
    '''
    if delimiter not in [",", "\t"]:
        print(f"unsupported delimiter `{delimiter}`")
        return

    with open(filename, "r") as f:
        csv_reader = csv.reader(f, delimiter=delimiter)
        return list(csv_reader)

def read_page_descriptions(filename):
    '''
    Read the header and addtional text from a markdown file.
    Line breakers were stripped to fit MarkdownTable.assemble_table
    '''
    with open(filename, "r") as f:
        return [l.split("\n")[0] for l in f.readlines()]


if __name__ == '__main__':
    project_root = Path("__file__").parent

    ack_path = project_root / "data" / "acknowledgements.csv"
    ack_desc_path = project_root / "data" / "acknowledgements_descriptions.md"

    table = read_tablefile(ack_path, delimiter=",")
    desc = read_page_descriptions(ack_desc_path)

    mder = MarkdownTable(table, desc)
    mder.generate(project_root / "brainhack_book" / "acknowledgements.md")

    # aff_path = project_root / "affiliations.csv"
    # aff = read_file(aff_path, delimiter="\t")
