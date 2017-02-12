#!/usr/bin/env python
"""Creating data folders for each university"""

import os
import re


def create_folder(name):
    path = '/Users/bagursreenivasamurth/Dev/gradscout/data/uni_data/'
    uni_data_path = path + name
    try:
        os.mkdir(uni_data_path)
    except Exception as e:
        print 'Error in creating folder'
        print 'Exception: %s', e


def get_university_names():
    path = '/Users/bagursreenivasamurth/Dev/gradscout/data/uni_data/'

    files = os.listdir(path)

    filenames = []

    for filename in files:
        if is_name(filename):
            filenames.append(is_name(filename))

    print filenames

    return filenames


def is_name(filename):
    regex = r"(\w+).htm"
    match = re.match(regex, filename)

    if match:
        return match.group(1)
    else:
        None


def run():
    university_names = get_university_names()

    for university in university_names:
        create_folder(university)


if __name__ == "__main__":
    run()
