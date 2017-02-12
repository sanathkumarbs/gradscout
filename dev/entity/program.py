#!/usr/bin/env python
"""Class Object for Program."""


class Program(object):
    """Class Object for Program."""

    def __init__(self):
        """Initializing the Program Object."""
        self._name = None
        self._fee = None

    @property
    def name(self):
        """Name property of the Program Object.

        Sample: Information Management
        """
        return self._name

    @name.setter
    def name(self, name):
        """Set the Name of the Program Object.

        Sample: Information Management
        """
        self._name = name

    @name.deleter
    def name(self):
        """Delete the Name property of the Program Object."""
        del self._name

    @property
    def fee(self):
        """Fee per year in USD for pursuing the Program.

        Sample: 30000
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Set the Fee per year in USD for pursuing the Program.

        Fee per year in USD for pursuing the Program.
        Sample: 30000
        """
        self._fee = fee

    @fee.deleter
    def fee(self):
        """Delete the Fee property of the Program Object."""
        del self._fee

    @property
    def length(self):
        """Length of the program in months.

        Sample: 21
        """
        return self._length

    @length.setter
    def length(self, length):
        """Set the Length of the program in months.

        Sample: 21
        """
        self._length = length

    @length.deleter
    def length(self):
        """Delete the Length property of the Program Object."""
        del self._length

    @property
    def gpa(self):
        """Average GPA in the Program.

        Sample: 3.7
        """
        return self._gpa

    @gpa.setter
    def gpa(self, gpa):
        """Set the Average GPA in the Program.

        Sample: 3.7
        """
        self._gpa = gpa

    @gpa.deleter
    def gpa(self):
        """Delete the GPA property of the Program Object."""
        del self._gpa

    @property
    def gre(self):
        """Average GRE Score in the Program.

        Sample: 321
        Min: 260
        Max: 340
        """
        return self._gre

    @gre.setter
    def gre(self, gre):
        """Set the Average GRE Score in the Program.

        Sample: 321
        Min: 260
        Max: 340
        """
        self._gre = gre

    @gre.deleter
    def gre(self):
        """Delete the GRE Score property of the Program Object."""
        del self._gre

    @property
    def gmat(self):
        """Average GMAT Score in the Program.

        Sample: 321
        Min: 200
        Max: 800
        """
        return self._gmat

    @gmat.setter
    def gmat(self, gmat):
        """Set the Average GMAT Score in the Program.

        Sample: 321
        Min: 200
        Max: 800
        """
        self._gmat = gmat

    @gmat.deleter
    def gmat(self):
        """Delete the GMAT Score property of the Program Object."""
        del self._gmat
