#!/usr/bin/env python
"""Module for scraping data."""

import os
import re

import codecs
from bs4 import BeautifulSoup


class University(object):
    """docstring for university"""

    def __init__(self, path):
        self.path = path
        self.html = None
        self.soup = self.get_soup()
        self.name = self.get_name()

    def get_soup(self):
        file = codecs.open(self.path, 'r', 'utf-8')
        soup = BeautifulSoup(file.read(), "html.parser")
        self.html = str(soup)
        file.close()
        return soup

    def get_name(self):
        if self.has_namee():
            name = self.has_namee()
            return name
        else:
            print 'WARNING: University Name was not parsed'
            return None

    def has_name(self):
        name_regex = r"<h1>([\w+\s+]+)<\/h1>"
        match = re.match(name_regex, self.html, re.UNICODE)
        if match:
            return match.group(0)
        else:
            None

    def has_namee(self):
        match = self.soup.select('h1')
        if match and len(match) == 1:
            return match[0].text
        else:
            None


def get_raw_html():
    path = '/Users/bagursreenivasamurth/Dev/gradscout/data/uni_data/'

    files = os.listdir(path)

    filenames = []

    for filename in files:
        if is_name(filename):
            file_path = path + is_name(filename)
            filenames.append(file_path)

    return filenames


def is_name(filename):
    regex = r"(\w+).htm"
    match = re.match(regex, filename)

    if match:
        return match.group(0)
    else:
        None


def run():
    uni_files_path = get_raw_html()
    universities = []

    for uni_file_path in uni_files_path:
        uni_obj = University(uni_file_path)
        universities.append(uni_obj)

    for uni_obj in universities:
        print_parsed_uni_data(uni_obj)


def print_parsed_uni_data(university):
    print '-' * 65
    print 'University Name: ', university.name
    print '-' * 65

if __name__ == "__main__":
    run()
