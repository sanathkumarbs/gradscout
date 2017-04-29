#!/usr/bin/env python
"""Class Object for School."""


class School(object):
    """Class Object for School."""

    def __init__(self):
        """Initializing the School Object."""
        self._name = None
        self._school_type = None

    @property
    def name(self):
        """Name property of the School Object.

        Sample: Information School
        """
        return self._name

    @name.setter
    def name(self, name):
        """Set the Name of the School Object.

        Sample: Information School
        """
        self._name = name

    @name.deleter
    def name(self):
        """Delete the Name property of the School Object."""
        del self._name

    @property
    def school_type(self):
        """School Type property of the School Object.

        Options: Business, Engineering, Information
        """
        return self._school_type

    @school_type.setter
    def school_type(self, school_type):
        """Set the School Type of the School Object.

        Options: Business, Engineering, Information
        """
        self._school_type = school_type

    @school_type.deleter
    def school_type(self):
        """Delete the School Type property of the School Object."""
        del self._school_type
