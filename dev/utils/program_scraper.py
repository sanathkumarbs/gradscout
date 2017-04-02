#!/usr/bin/env python
"""Module for scraping program data."""

import re
import os

# import sys
# sys.path.insert(0, '/Users/bagursreenivasamurth/Dev')

from bs4 import BeautifulSoup
import codecs

# from gradscout.dev.entity.program import Program
# from gradscout.dev.entity.university import University
# from gradscout.dev.entity.school import School


class Soupify(object):
    """docstring for Soupify"""

    def __init__(self, path):
        self.path = path
        self.html = None
        self.soup = None
        self.text = None
        self.initial_setup()

    def initial_setup(self):
        self.get_soup()
        self.get_html()
        self.get_text()

    def get_soup(self):
        file = codecs.open(self.path, 'r', 'utf-8')
        self.soup = BeautifulSoup(file.read(), "html.parser")
        file.close()

    def get_html(self):
        self.html = str(self.soup)

    def get_text(self):
        self.text = self.soup.get_text()

    def get_data(self):
        # TODO: Return a dict of data scraped
        # {University: {University Data}, School: {School Data}...}
        title = self.get_program_name()

    def get_program_name(self):
        titles = self.soup.findAll("title")

        for title in titles:
            print title.findAll(text=True)[0]

        program_name_words = ['M.S.', 'MS', 'Master', 'Science', 'of']


def get_raw_html():
    path = '/Users/bagursreenivasamurth/Dev/gradscout/data/program/'

    files = os.listdir(path)

    filenames = []

    for filename in files:
        if is_name(filename):
            file_path = path + is_name(filename)
            filenames.append(file_path)

    return filenames


def is_name(filename):
    regex = r"(.*).htm"
    match = re.match(regex, filename)

    if match:
        return match.group(0)
    else:
        None


def run():
    uni_files_path = get_raw_html()

    for uni_file_path in uni_files_path:
        soup = Soupify(uni_file_path)
        soup.get_program_name()


def print_parsed_uni_data(university):
    print '-' * 65
    print 'University Name: ', university.name
    print '-' * 65

if __name__ == "__main__":
    run()
