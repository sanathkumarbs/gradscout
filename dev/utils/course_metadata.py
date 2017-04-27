#!/usr/bin/env python
"""Module for cleaning courses and extracting metadata."""

import re
import json
import math
import pprint
from nltk import pos_tag
from database import Firebase
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()
firebase = Firebase()

STOPWORDS = set(stopwords.words('english'))


class GetData(object):
    """Get the Input Data."""

    def __init__(self):
        """Initializing with the data files."""
        cur_data_file = ("/Users/bagursreenivasamurth/Dev/gradscout/"
                         "data/data_for_database/firebase_export.json")
        course_data_file = (
            "/Users/bagursreenivasamurth/Dev/gradscout/data/curriculum/cur_data.json")

        self.cur_json_data = self._read_json_data(cur_data_file)
        self.course_data = self._read_json_data(course_data_file)

    def get_data(self):
        """Return the loaded data."""
        return self.cur_json_data, self.course_data

    def _read_json_data(self, filepath):
        json_file = open(filepath, 'r').read()
        json_object = json.loads(json_file)
        return json_object

    def _read_file(self, filepath):
        with open(filepath, 'r') as cur_data_file:
            data = cur_data_file.read()

        return data


class Cleaner(object):
    """Cleans the course data."""

    def __init__(self, data):
        """Initializing cleaner."""
        # Raw input data
        self.data = data

        # Cleaned Data
        self.cleaned_data = None

        # Will be a keyword metadata list
        self.metadata = []

        # Importing Keywords for Areas
        self.area_keywords = self._import_keywords()

    def _import_keywords(self):
        """Importing list of keywords."""
        with open('/Users/bagursreenivasamurth/Dev/gradscout/data/curriculum/keywords.txt', 'r') as ip:
            area_keywords = ip.read().split('\n')

        return area_keywords

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

                if not len(meta) < 3:
                    self.metadata.append(meta)

    def is_keyword(self, word):
        """Selecting only the keywords."""
        if word in self.area_keywords:
            return True

        return False

    def get_metadata(self):
        """Get the cleaned course metadata as a string."""
        return ' '.join(self.metadata)

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


class Classify(object):
    """Classifying program into areas of interest."""

    def __init__(self, raw_corpus):
        """Initializing the classifying class with keywords of interest."""
        self.area_keywords = self._area_keywords()
        self.raw_corpus = raw_corpus
        self.corpus_values = raw_corpus.values()
        self.corpus_keys = raw_corpus.keys()

        # Stores the areas classified for each program
        self.classification = {}

        self.classify_areas()

    def _area_keywords(self):
        """Importing all areas and keywords."""
        keywords_file = (
            "/Users/bagursreenivasamurth/Dev/gradscout/data/curriculum/keywords_areas.json")

        data = self._read_json_data(keywords_file)

        return data

    def _read_json_data(self, filepath):
        json_file = open(filepath, 'r').read()
        json_object = json.loads(json_file)
        return json_object

    def classify_areas(self):
        """Classify the programs into different areas."""
        for area in self.area_keywords:
            vocab = self.get_vocab(area)
            scores = self.analyze(vocab)
            for index in xrange(0, len(scores)):
                program = self.corpus_keys[index]
                pid = re.search('\d+', program).group(0)
                score = scores[index]
                confidence = self.classify(score)

                result = self.check_confidence(
                    confidence, area, vocab, program)

                result = result * 100

                updated_confidence = round(result, 2)

                if pid not in self.classification:
                    self.classification[pid] = [(area, updated_confidence)]
                else:
                    areas = self.classification[pid]
                    res = (area, updated_confidence)
                    areas.append(res)
                    self.classification[pid] = areas

    def classify(self, score):
        """
        Classify the programs into an area if it matches the threshold.

        Input to be an array or list of matching areas
        """
        total = len(score)
        count = 0
        score_threshold = 1
        # classification_threshold = int(math.floor(total / 4))

        for item in score:
            if item > score_threshold:
                count += 1

        confidence = (float(count) / float(total))

        return confidence

    def check_confidence(self, confidence, area, vocab, program):
        updated_confidence = float(confidence)

        pid = re.search('\d+', program).group(0)
        program_details = firebase.get_program_details(pid)
        program_name = program_details['name']

        program_keys = program_name.split()
        area_keys = area.split('_')

        test = []
        test.extend(area_keys)
        test.extend(vocab)

        confidence_boost = False
        boost = "high"

        lower_programkeys = [element.lower() for element in program_keys]
        lower_test = [element.lower() for element in test]

        for program_key in lower_programkeys:
            if program_key in lower_test:
                    confidence_boost = True
            common_keys = ['computer', 'engineering', 'information', 'science']
            if program_key in common_keys:
                boost = "low"

        if confidence_boost:
            if boost != "low":
                updated_confidence += 0.30
            else:
                updated_confidence += 0.15

        return updated_confidence

    def get_vocab(self, area):
        """Get the area keywords for each area of specalization."""
        vocab = list(self.area_keywords[area])
        return vocab

    def bigrams_per_line(self, doc):
        """Generate bigrams for a given data."""
        for ln in doc.split('\n'):
            terms = re.findall(r'\w{2,}', ln)
            for bigram in zip(terms, terms[1:]):
                yield '%s %s' % bigram

    def analyze(self, vocab):
        """
        Analyze the corpus with given vocab using Vectorization.

        vocab - list
        """
        cv = CountVectorizer(vocabulary=vocab)
        # cv = CountVectorizer(analyzer=self.bigrams_per_line, vocabulary=vocab)
        result = cv.fit_transform(self.corpus_values).toarray()
        return result

    def get_classification(self):
        """Return a dict of classified areas for each program."""
        return self.classification

if __name__ == '__main__':
    get_data = GetData()
    cur_data, course_data = get_data.get_data()

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

    for key, areas in classifications.items():
        pid = re.search('\d+', key).group(0)
        program_details = firebase.get_program_details(pid)
        program_name = program_details['name']

        print '-' * 30
        print 'Program ID:', pid
        print 'Program Name:', program_name
        for area in areas:
            name = str(area[0])
            percent = area[1] * 100
            print 'Area: %s     Confidence: %s' % (name, percent)

    print 'Total Programs: ', len(classifications.keys())
