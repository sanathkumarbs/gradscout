#!/usr/bin/env python
"""Firebase Database Interaction Module."""

from firebase import firebase


class Firebase(object):
    """Class for Accessing Firebase Database."""

    def __init__(self):
        """Initialize Firebase Object for Database Access."""
        self.firebase = firebase.FirebaseApplication(
            'https://gradscout-40fed.firebaseio.com/', None)
        self.data = self._get_data()

    def _get_data(self):
        """Get complete data for quicker cached access.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            program_dict (dict): Python Dict of Complete Program Details
        """
        endpoint = "/programs/"
        result = self.firebase.get(endpoint, None)
        return result

    def get_detailed_program(self, program_id):
        """Get the Detailed Program Details for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            program_dict (dict): Python Dict of Complete Program Details
        """
        result = None
        try:
            result = self.data[int(program_id)]
        except KeyError:
            endpoint = "/programs/" + str(program_id)
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_count(self):
        """Get the total count of programs available in the database.

        Returns:
            count (int): Total count of the programs in the database
        """
        count = None
        try:
            count = len(self.data)
        except KeyError:
            endpoint = "/programs/"
            result = self.firebase.get(endpoint, None)
            count = len(result)
        return count

    def get_program_research(self, program_id):
        """Get the Program Research Details for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            research_dict (dict): Python Dict of Research Details
        """
        result = None
        try:
            result = self.data[int(program_id)].get('research')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/research'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_admission_rate(self, program_id):
        """Get the Admission Rate for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            admission_rate (int): Admission Rate in Percentage
        """
        result = None
        try:
            result = self.data[int(program_id)].get('admission_rate')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/admission_rate'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_fees(self, program_id):
        """Get the Program Fees for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            fees_dict (dict): Python Dict of Program Fees
        """
        result = None
        try:
            result = self.data[int(program_id)].get('fees')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/fees'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_acad(self, program_id):
        """Get the Academic Requirements for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            acad_dict (dict): Python Dict of Academic Requirement Details
        """
        result = None
        try:
            result = self.data[int(program_id)].get('academic_requirements')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/academic_requirements'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_living(self, program_id):
        """Get the Living Expenses for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            program_dict (dict): Python Dict of Living Expense Details
        """
        result = None
        try:
            result = self.data[int(program_id)].get('living_expenditure')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/living_expenditure'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_location(self, program_id):
        """Get the Location Details of a given Program ID.

        Returns:
            location_dict (dict): Python Dict of Location Details
        """
        result = None
        try:
            result = self.data[int(program_id)].get('location')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/location'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_ownership(self, program_id):
        """Get the Ownership Details for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            ownership_dict (dict): Python Dict of Ownership Details
        """
        result = None
        try:
            result = self.data[int(program_id)].get('ownership')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/ownership'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_details(self, program_id):
        """Get the Program Details for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            program_dict (dict): Python Dict of Program Details
        """
        result = None
        try:
            result = self.data[int(program_id)].get('program')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/program'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_university(self, program_id):
        """Get the University Details for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            program_dict (dict): Python Dict of University Details
        """
        result = None
        try:
            result = self.data[int(program_id)].get('university')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/university'
            result = self.firebase.get(endpoint, None)
        return result

    def get_program_rank(self, program_id):
        """Get the Rank Details for a given Program ID.

        Args:
            program_id (int): Unique ID for Program

        Returns:
            program_dict (dict): Python Dict of Rank Details
        """
        result = None
        try:
            result = self.data[int(program_id)].get('rank')
        except KeyError:
            endpoint = "/programs/" + str(program_id) + '/rank'
            result = self.firebase.get(endpoint, None)
        return result
