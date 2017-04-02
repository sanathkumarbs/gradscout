#!/usr/bin/env python
"""Module for importing data into Firebase."""

import json
from json_builder import Schema, Research, Fees, Acad, Living, Location, \
    Ownership, Program, Rank, University


class GetData(object):
    """docstring for university"""

    def __init__(self):
        program_data_filepath = ("/Users/bagursreenivasamurth/Dev/gradscout/"
                                 "data/data_for_database/program_data.json")
        college_data_filepath = ("/Users/bagursreenivasamurth/Dev/"
                                 "gradscout/data/data_for_database/"
                                 "college_data.json")

        self.program_data_list = self._read_data(program_data_filepath)
        self.college_data_dict = self._read_data(college_data_filepath)

    def _read_data(self, filepath):
        json_file = open(filepath, 'r').read()
        json_object = json.loads(json_file)
        return json_object


class ExtractData(object):
    """docstring for ExtractData"""

    def __init__(self, program_data, college_data):
        self.program_data = program_data
        self.college_data = self._get_college_data(college_data)
        self.research = self._get_research()
        self.admission_rate = self._get_admission_rate()
        self.fees = self._get_fees()
        self.acad = self._get_acad()
        self.living = self._get_living()
        self.location = self._get_location()
        self.ownership = self._get_ownership()
        self.program = self._get_program()
        self.university = self._get_university()
        self.rank = self._get_rank()

    def _get_college_data(self, college_data):
        uni_name = self.program_data['uni_name']
        if uni_name in college_data:
            return college_data[uni_name]
        else:
            raise KeyError("No Entry for given University in College Data")
            return None

    def _get_research(self):
        carnegie_basic_id = self.college_data['carnegie_basic']
        research = Research(carnegie_basic_id)
        return research

    def _get_admission_rate(self):
        admission_rate = self.college_data['admission_rate']
        return admission_rate

    def _get_fees(self):
        in_state = self.program_data['in_state']
        out_of_state = self.program_data['out_of_state']

        fees = Fees(in_state, out_of_state)
        return fees

    def _get_acad(self):
        gpa = self.program_data['gpa']
        quant = self.program_data['quant']
        verbal = self.program_data['verbal']

        acad = Acad(gpa, quant, verbal)
        return acad

    def _get_living(self):
        boarding = self.program_data['boarding']
        books = self.program_data['books']
        other = self.program_data['other']
        overall = self.program_data['overall_costs']

        living = Living(boarding, books, other, overall)
        return living

    def _get_location(self):
        city = self.college_data['city']
        lat = self.college_data['lat']
        lon = self.college_data['lon']
        region_id = self.college_data['region_id']
        state = self.college_data['state']
        zipcode = self.college_data['zip']

        location = Location(city, lat, lon, region_id,
                            state, zipcode)
        return location

    def _get_ownership(self):
        ownership_id = self.college_data['ownership']

        ownership = Ownership(ownership_id)
        return ownership

    def _get_program(self):
        department = self.program_data['department']
        program_id = self.program_data['program_id']
        length = self.program_data['length']
        name = self.program_data['name']
        school = self.program_data['school']
        website = self.program_data['website']

        program = Program(department, program_id,
                          length, name, school, website)
        return program

    def _get_rank(self):
        cwur = self.program_data['cwur']
        cwur_score = self.program_data['cwur_score']
        forbes = self.program_data['forbes']
        overall = self.program_data['overall_ranking']
        times = self.program_data['times']
        usnews = self.program_data['usnews']
        usnews_score = self.program_data['usnews_score']

        rank = Rank(cwur, cwur_score, forbes, overall,
                    times, usnews, usnews_score)
        return rank

    def _get_university(self):
        university_id = self.program_data['uni_id']
        name = self.program_data['uni_name']

        university = University(university_id, name)
        return university


class JSONBuilder(object):
    """docstring for university"""

    def __init__(self,
                 admission_rate,
                 research,
                 fees,
                 acad,
                 living,
                 location,
                 ownership,
                 program,
                 rank,
                 university):

        self.research = research
        self.admission_rate = admission_rate
        self.fees = fees
        self.acad = acad
        self.living = living
        self.location = location
        self.ownership = ownership
        self.program = program
        self.rank = rank
        self.university = university
        self.json_dict = None

        self._build_json()

    def _build_json(self):
        schema = Schema(self.admission_rate,
                        self.research,
                        self.fees,
                        self.acad,
                        self.living,
                        self.location,
                        self.ownership,
                        self.program,
                        self.rank,
                        self.university)
        self.json_dict = schema.get_schema_dict()

    def get_json_data(self):
        return self.json_dict


if __name__ == '__main__':
    import_obj = GetData()
    program_data = import_obj.program_data_list
    college_data = import_obj.college_data_dict
    json_dict_data = []

    for program in program_data:
        data = ExtractData(program, college_data)

        json_builder = JSONBuilder(data.admission_rate,
                                   data.research,
                                   data.fees,
                                   data.acad,
                                   data.living,
                                   data.location,
                                   data.ownership,
                                   data.program,
                                   data.rank,
                                   data.university)

        dict_data = json_builder.get_json_data()
        json_dict_data.append(dict_data)

    json_filepath = ("/Users/bagursreenivasamurth/Dev/gradscout/"
                     "data/data_for_database/firebase.json")

    with open(json_filepath, 'w') as json_file:
        json.dump(json_dict_data, json_file)
