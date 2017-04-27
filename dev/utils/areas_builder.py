#!/usr/bin/env python
"""Module for building JSON content for Areas of Interest."""

import re
import json
import pprint
from database import Firebase
from course_metadata import GetData, Cleaner, Classify

firebase = Firebase()


class AreaOfInterest(object):
    """Build a Python Dict for given Area of Interest Scores."""

    def __init__(self, area_scores):
        """Building the Dict."""
        self.area_scores = area_scores
        self.schema = {}

        self._build_structure()

    def _build_structure(self):
        for aoi in self.area_scores:
            area = aoi[0]
            score = aoi[1]
            self.schema[area] = score

    def get_schema_dict(self):
        """Return the Schema."""
        return self.schema


def get_course_metadata(course_data):
    """Get the Course Metadata."""
    raw_corpus = {}

    for program in course_data:
        # raw data of the program curriculum
        raw_data = course_data[program]

        # Cleaning the data to extract metadata
        cleaner = Cleaner(raw_data)
        cleaner.clean()

        # Metadata of program's curriculum
        metadata = cleaner.get_metadata()

        # Updating the corpus with metadata
        raw_corpus[program] = metadata

    # Performing classification for each program
    classifier = Classify(raw_corpus)

    # Getting all the classifications
    classifications = classifier.get_classification()

    return classifications


def print_course_metadata(classifications):
    """Print the Course Metadata."""
    for key, areas in classifications.items():
        pid = re.search('\d+', key).group(0)
        program_details = firebase.get_program_details(pid)
        program_name = program_details['name']

        print '-' * 30
        print 'Program ID:', pid
        print 'Program Name:', program_name
        for area in areas:
            name = str(area[0])
            percent = area[1]
            print 'Area: %s     Confidence: %s' % (name, percent)

    print 'Total Programs: ', len(classifications.keys())


def build_new_structure(programs):
    """Build the new structure with the Course Metadata and existing data."""
    structure = {'programs': []}

    for pid, data in enumerate(programs):
        areas = classifications[str(pid)]

        aoi = AreaOfInterest(areas)
        schema = aoi.get_schema_dict()

        data['areaofinterest'] = schema

        structure['programs'].append(data)

    return structure

if __name__ == '__main__':
    get_data = GetData()
    cur_json_data, course_data = get_data.get_data()
    classifications = get_course_metadata(course_data)

    programs = cur_json_data['programs']

    structure = build_new_structure(programs)

    json_filepath = ("/Users/bagursreenivasamurth/Dev/gradscout/"
                     "data/data_for_database/firebase_updated.json")

    with open(json_filepath, 'w') as json_file:
        json.dump(structure, json_file)
