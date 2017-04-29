#!/usr/bin/env python
"""Module for building JSON data for Firebase."""


class Schema(object):
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

        self.schema = {}
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

        self._build_structure()

    def _build_structure(self):
        self.schema['research'] = self.research.research_dict
        self.schema['admission_rate'] = self.admission_rate
        self.schema['fees'] = self.fees.fees_dict
        self.schema['academic_requirements'] = self.acad.acad_dict
        self.schema['living_expenditure'] = self.living.living_dict
        self.schema['location'] = self.location.location_dict
        self.schema['ownership'] = self.ownership.ownership_dict
        self.schema['program'] = self.program.program_dict
        self.schema['rank'] = self.rank.rank_dict
        self.schema['university'] = self.university.university_dict

    def get_schema_dict(self):
        return self.schema


class University(object):
    """docstring for ClassName"""

    def __init__(self, university_id, name):
        self.university_id = university_id
        self.name = name
        self.university_dict = self._get_structure()

    def _get_structure(self):
        structure = {
            "id": self.university_id,
            "name": self.name
        }
        return structure


class Rank(object):
    """docstring for ClassName"""

    def __init__(self, cwur, cwur_score, forbes, overall, times, usnews, usnews_score):
        self.cwur = cwur
        self.cwur_score = cwur_score
        self.forbes = forbes
        self.overall = overall
        self.times = times
        self.usnews = usnews
        self.usnews_score = usnews_score
        self.rank_dict = self._get_structure()

    def _get_structure(self):
        structure = {
            "cwur": self.cwur,
            "cwur_score": self.cwur_score,
            "forbes": self.forbes,
            "overall": self.overall,
            "times": self.times,
            "usnews": self.usnews,
            "usnews_score": self.usnews_score
        }
        return structure


class Program(object):
    """docstring for ClassName"""

    def __init__(self, department, program_id, length, name, school, website):
        self.department = department
        self.program_id = program_id
        self.length = length
        self.name = name
        self.school = school
        self.website = website
        self.program_dict = self._get_structure()

    def _get_structure(self):
        structure = {
            "department": self.department,
            "id": self.program_id,
            "length": self.length,
            "name": self.name,
            "school": self.school,
            "website": self.website
        }
        return structure


class Ownership(object):
    """docstring for ClassName"""

    def __init__(self, ownership_id):
        self.ownership_id = ownership_id
        self.name_classification = self._get_classification()
        self.name = self._get_name()
        self.ownership_dict = self._get_structure()

    def _get_name(self):
        if self.name_classification[str(self.ownership_id)]:
            return self.name_classification[str(self.ownership_id)]
        else:
            raise KeyError("No Entry for given Ownership ID in Ownership Data")

    def _get_classification(self):
        name_classification = {
            "1": "Public",
            "2": "Private nonprofit",
            "3": "Private for-profit"
        }
        return name_classification

    def _get_structure(self):
        structure = {
            "id": self.ownership_id,
            "name": self.name
        }
        return structure


class Location(object):
    """docstring for ClassName"""

    def __init__(self, city, lat, lon, region_id, state, zipcode):
        self.city = city
        self.lat = lat
        self.lon = lon
        self.region_id = region_id
        self.region_name = self._get_region()
        self.state = state
        self.zipcode = zipcode
        self.location_dict = self._get_structure()

    def _get_region(self):
        region_name = {
            "0": "U.S. Service Schools",
            "1": "New England",
            "2": "Mid East",
            "3": "Great Lakes",
            "4": "Plains",
            "5": "Southeast",
            "6": "Southwest",
            "7": "Rocky Mountains",
            "8": "Far West",
            "9": "Outlying Areas",
        }
        if str(self.region_id) in region_name:
            return region_name[str(self.region_id)]
        else:
            raise KeyError("No Entry for given Region ID in Region Data")
            return None

    def _get_structure(self):
        structure = {
            "city": self.city,
            "lat": self.lat,
            "lon": self.lon,
            "region_id": self.region_id,
            "region_name": self.region_name,
            "state": self.state,
            "zip": self.zipcode
        }
        return structure


class Living(object):
    """docstring for ClassName"""

    def __init__(self, boarding, books, other, overall):
        self.boarding = boarding
        self.books = books
        self.other = other
        self.overall = overall
        self.living_dict = self._get_structure()

    def _get_structure(self):
        structure = {
            "boarding": self.boarding,
            "books": self.books,
            "other": self.other,
            "overall": self.overall
        }
        return structure


class Acad(object):
    """docstring for ClassName"""

    def __init__(self, gpa, quant, verbal):
        self.gpa = gpa
        self.quant = quant
        self.verbal = verbal
        self.acad_dict = self._get_structure()

    def _get_structure(self):
        structure = {
            "gpa": self.gpa,
            "gre": {
                "quant": self.quant,
                "verbal": self.verbal
            }
        }
        return structure


class Fees(object):
    """docstring for ClassName"""

    def __init__(self, in_state, out_of_state):
        self.in_state = in_state
        self.out_of_state = out_of_state
        self.fees_dict = self._get_structure()

    def _get_structure(self):
        structure = {
            "in_state": self.in_state,
            "out_of_state": self.out_of_state
        }
        return structure


class Research(object):
    """docstring for ClassName"""

    def __init__(self, carnegie_basic_id):
        self.carnegie_basic_id = carnegie_basic_id
        self.name_classification = self._get_classification()
        self.carnegie_basic_name = self._get_name()
        self.research_dict = self._get_structure()

    def _get_name(self):
        if self.name_classification[str(self.carnegie_basic_id)]:
            return self.name_classification[str(self.carnegie_basic_id)]
        else:
            raise KeyError("No Entry for given Carnegie ID in Carnegie Data")
            return None

    def _get_structure(self):
        structure = {
            "carnegie_basic_id": self.carnegie_basic_id,
            "name": self.carnegie_basic_name
        }
        return structure

    def _get_classification(self):
        name_classification = {
            "0": "None",
            "1": "Associate's Colleges: High Transfer-High Traditional",
            "2": "Associate's Colleges: High Transfer-Mixed Traditional/Nontraditional",
            "3": "Associate's Colleges: High Transfer-High Nontraditional",
            "4": "Associate's Colleges: Mixed Transfer/Vocational & Technical-High Traditional",
            "5": "Associate's Colleges: Mixed Transfer/Vocational & Technical-Mixed Traditional/Nontraditional",
            "6": "Associate's Colleges: Mixed Transfer/Vocational & Technical-High Nontraditional",
            "7": "Associate's Colleges: High Vocational & Technical-High Traditional",
            "8": "Associate's Colleges: High Vocational & Technical-Mixed Traditional/Nontraditional",
            "9": "Associate's Colleges: High Vocational & Technical-High Nontraditional",
            "10": "Special Focus Two-Year: Health Professions",
            "11": "Special Focus Two-Year: Technical Professions",
            "12": "Special Focus Two-Year: Arts & Design",
            "13": "Special Focus Two-Year: Other Fields",
            "14": "Baccalaureate/Associate's Colleges: Associate's Dominant",
            "15": "Doctoral Universities: Highest Research Activity",
            "16": "Doctoral Universities: Higher Research Activity",
            "17": "Doctoral Universities: Moderate Research Activity",
            "18": "Master's Colleges & Universities: Larger Programs",
            "19": "Master's Colleges & Universities: Medium Programs",
            "20": "Master's Colleges & Universities: Small Programs",
            "21": "Baccalaureate Colleges: Arts & Sciences Focus",
            "22": "Baccalaureate Colleges: Diverse Fields",
            "23": "Baccalaureate/Associate's Colleges: Mixed Baccalaureate/Associate's",
            "24": "Special Focus Four-Year: Faith-Related Institutions",
            "25": "Special Focus Four-Year: Medical Schools & Centers",
            "26": "Special Focus Four-Year: Other Health Professions Schools",
            "27": "Special Focus Four-Year: Engineering Schools",
            "28": "Special Focus Four-Year: Other Technology-Related Schools",
            "29": "Special Focus Four-Year: Business & Management Schools",
            "30": "Special Focus Four-Year: Arts",
            "31": "Special Focus Four-Year: Law Schools",
            "32": "Special Focus Four-Year: Other Special Focus Institutions",
            "33": "Tribal Colleges",
            "-2": "Not applicable"
        }
        return name_classification
