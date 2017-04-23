#!/usr/bin/env python
"""Module for cleaning courses and extracting metadata."""

import re
import csv
import json
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()

STOPWORDS = set(stopwords.words('english'))


class GetData(object):
    """Get the Input Data."""

    def __init__(self):
        """Initializing with the data files."""
        cur_data_file = ("/Users/bagursreenivasamurth/Dev/gradscout/"
                         "data/data_for_database/firebase_export.json")
        course_data_file = ("/Users/bagursreenivasamurth/Dev/"
                            "gradscout/data/data_for_database/"
                            "cur_data.json")

        self.cur_data = self._read_data(cur_data_file)
        self.course_data = self._read_data(course_data_file)

    def _read_data(self, filepath):
        json_file = open(filepath, 'r').read()
        json_object = json.loads(json_file)
        return json_object


class Cleaner(object):
    """Cleans the course data."""

    def __init__(self, data):
        """Initializing cleaner."""
        # Raw input data
        self.data = data

        # Cleaned Data
        self.cleaned_data = None

        # Will be a keyword metadata list
        self.metadata = {}

    def clean(self):
        """Deploy cleaners."""
        # Making all content lowercase
        self._make_lowercase()

        # Remove any newline literals
        self._remove_newlines()

        # Remove all keywords which contain symbols
        self._remove_symbols()

        # Remove single characters
        self._remove_single_characters()

        # Remove any whitespaces
        self._remove_whitespaces()

        # Split string into keywords
        keywords = self._get_keywords()

        for keyword in keywords:
            # Remove any alphanumeric words
            # Removing all english stopwords
            if (self._remove_alphanumeric(keyword) and
                    self._remove_stopwords(keyword)):
                tokens = word_tokenize(keyword)
                tokens_pos = pos_tag(tokens)
                pos = tokens_pos[0][1]

                if 'V' in pos:
                    meta = stemmer.stem(keyword)
                else:
                    meta = lemmatiser.lemmatize(keyword)

                if meta not in self.metadata:
                    # self.metadata[meta] = [1, [keyword]]
                    self.metadata[meta] = 1
                else:
                    # [count, words] = self.metadata[meta]
                    # if keyword not in words:
                    #     words.append(keyword)
                    # self.metadata[meta] = [count + 1, words]
                    count = self.metadata[meta]
                    self.metadata[meta] = count + 1

    def get_metadata(self):
        """Get the cleaned course metadata as a list of keywords."""
        return self.metadata

    def _make_lowercase(self):
        """Converting all courses into lowercase."""
        self.cleaned_data = self.data.lower()

    def _get_keywords(self):
        """Convert course string into a list of keywords."""
        return self.cleaned_data.split()

    def _remove_symbols(self):
        """Removing all symbols."""
        self.cleaned_data = re.sub(r'[^\w]', ' ', self.cleaned_data)

    def _remove_newlines(self):
        """Removing all newline symbols."""
        self.cleaned_data = re.sub(r'\\n', ' ', self.cleaned_data)

    def _remove_single_characters(self):
        """Removing all single characters."""
        self.cleaned_data = re.sub(r'(^| ).( |$)', ' ', self.cleaned_data)

    def _remove_whitespaces(self):
        """Removing all whitespaces."""
        self.cleaned_data = re.sub(r'\s+', ' ', self.cleaned_data)

    def _remove_alphanumeric(self, word):
        """Remove alphanumeric words."""
        regex = "[^a-zA-Z]+"
        if re.search(regex, word):
            return False

        return True

    def _remove_stopwords(self, word):
        """Removing all english stopwords."""
        if word not in STOPWORDS:
            return True

        return False

if __name__ == '__main__':
    # data = GetData()

    # sample_data_file = ("/Users/bagursreenivasamurth/Dev/gradscout/"
    #                    "data/curriculum/sample_course_data.txt")

    sample_data_file = (
        "/Users/bagursreenivasamurth/Dev/gradscout-main/Course Module/CourseExtractCode/Courses With Fnalized Program Names.csv")

    with open(sample_data_file, 'r') as cur_data_file:
        data = cur_data_file.read()

    cleaner = Cleaner(data)
    cleaner.clean()
    # import pprint
    # pprint.pprint(cleaner.metadata)
    with open('metadata_full.csv', 'wb') as csv_file:  # Just use 'w' mode in 3.x
        writer = csv.writer(csv_file)
        for key, value in cleaner.metadata.items():
            writer.writerow([key, value])
