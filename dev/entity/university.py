#!/usr/bin/env python
"""Class Object for University."""


class University(object):
    """Class Object for University."""

    def __init__(self):
        """Initializing the University Object."""
        self._name = None
        self._uni_type = None
        self._expense = None
        # Location should probably be another object?
        self._location = None
        self._rank = None

    @property
    def name(self):
        """Name property of the University Object.

        Sample: University of Washington
        """
        return self._name

    @name.setter
    def name(self, name):
        """Set the Name of the University Object.

        Sample: University of Washington
        """
        self._name = name

    @name.deleter
    def name(self):
        """Delete the Name property of the University Object."""
        del self._name

    @property
    def uni_type(self):
        """University Type property of the University Object.

        Options: Public, Private
        """
        return self._uni_type

    @uni_type.setter
    def uni_type(self, uni_type):
        """Set the University Type of the University Object.

        Options: Public, Private
        """
        self._uni_type = uni_type

    @uni_type.deleter
    def uni_type(self):
        """Delete the University Type property of the University Object."""
        del self._uni_type

    @property
    def expense(self):
        """Expense property of the Program Object.

        Living Expense per year in USD for studying at the University.
        Sample: 30000
        """
        return self._expense

    @expense.setter
    def expense(self, expense):
        """Set the Expense of the Program Object.

        Living Expense per year in USD for studying at the University.
        Sample: 30000
        """
        self._expense = expense

    @expense.deleter
    def expense(self):
        """Delete the Expense property of the Program Object."""
        del self._expense

    @property
    def location(self):
        """Location property of the Program Object."""
        return self._location

    @location.setter
    def location(self, location):
        """Set the Location of the Program Object."""
        self._location = location

    @location.deleter
    def location(self):
        """Delete the Location property of the Program Object."""
        del self._location

    @property
    def rank(self):
        """Rank property of the Program Object."""
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Set the Rank of the Program Object."""
        self._rank = rank

    @rank.deleter
    def rank(self):
        """Delete the Rank property of the Program Object."""
        del self._rank
