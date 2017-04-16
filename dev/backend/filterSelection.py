import Filters
"""
1. FilterSelection class gets the selected user input criteria
   and assignins that value to the respective paramaters
2. Whatever value is not None will get passed to the respective
   filter method from the filters class
3. Each filter method from the filters class will run the filter
   on the firebase and return the list of id after applying the filter
4. The run filter method will finally combine these lists into a set
   to remove the duplicates and return the final list of program ids
"""


class FilterSelection(object):
	"""Class for Selecting Programs Matching Filters."""

    def __init__(
            self,
            overall_rank=None,
            usnews=None,
            cwur=None,
            forbes=None,
            times=None,

            state=None,
            city=None,
            zipcode=None,
            region=None,

            fees_in_state=None,
            fees_out_of_state=None,

            gpa=None,
            verbal=None,
            quant=None,

            boarding=None,
            books=None,
            overall_expenses=None,

            admission_rate=None,

            areas_of_interest=None):

        self.overall_rank = overall_rank
        self.usnews = usnews
        self.cwur = cwur
        self.forbes = forbes
        self.times = times

        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.region = region

        self.fees_in_state = fees_in_state
        self.fees_out_of_state = fees_out_of_state

        self.gpa = gpa
        self.verbal = verbal
        self.quant = quant

        self.boarding = boarding
        self.books = books
        self.overall_expenses = overall_expenses

        self.admission_rate = admission_rate

        self.areas_of_interest = areas_of_interest

        # List of programs matching atleast one of the requested criteria
        self.unique_programs = None

        # List of programs meeting all requested criteria
        self.common_programs = []

        # Verbose program dict with all matching info
        self.matches = None

        # creating the object of Filters class
        self.filters = Filters()

        # Program Count 
        self.count = self.filters.count

    def filter_programs(self):
        """Filter the programs"""
        
        # Deploy Filter Selection
        self.run_selected_filters()

        # Getting all the unique programs
        self.unique_programs = list(self.matches.keys())

        # Validating we atleast have one program matching one criteria
        # Fall back to all programs if no match is found

        if len(self.unique_programs) < 1:
            # Setting unique programs to all programs
            self.unique_programs = []
            self.unique_programs.extend(range(0,self.count-1))

            # Setting all matches to zero
            self.matches = []
            self.matches = dict.fromkeys(self.unique_programs, None)

            # Setting all common programs to all programs
            self.common_programs = []
            self.common_programs = self.common_programs.extend(
                range(0, self.count-1))

        return (self.common_programs, self.unique_programs, self.matches)

    def update_results(self, matching_programs):
        """Helper method to update matching programs results"""

        # Update the common program list
        if self.common_programs is not None:
            common = self.common_programs.intersection(matching_programs)

            if len(common) > 0:
                self.common_programs = common
            else:
                self.common_programs =[]

        elif:
            self.common_programs = []
            self.common_programs.extend(matching_programs)

        for program in matching_programs:
            # Update the verbose program dict of results
            if self.matches is None:
                self.matches[program] = 1
            elif program in self.matches:
                self.matches[program] += 1

    def run_selected_filters(self):

        if self.overall_rank is not None:
            matching_programs = self.filters.filter_rank_overall(overall_rank)
            self.update_results(matching_programs)

        if self.usnews is not None:
            matching_programs = self.filters.filter_rank_usnews(usnews)
            self.update_results(matching_programs)

        if self.cwur is not None:
            matching_programs = self.filters.filter_rank_cwur(cwur)
            self.update_results(matching_programs)

        if self.forbes is not None:
            matching_programs = self.filters.filter_rank_forbes(forbes)
            self.update_results(matching_programs)

        if self.times is not None:
            matching_programs = self.filters.filter_rank_times(times)
            self.update_results(matching_programs)

        if self.state is not None:
            matching_programs = self.filters.filter_location_state(state)
            self.update_results(matching_programs)

        if self.city is not None:
            matching_programs = self.filters.filter_location_city(city)
            self.update_results(matching_programs)

        if self.zipcode is not None:
            inal_list.append = self.filters.filter_location_zip(zipcode)
            self.update_results(matching_programs)

        if self.region is not None:
            matching_programs = self.filters.filter_location_region(region)
            self.update_results(matching_programs)

        if self.fees_in_state is not None:
            matching_programs = self.filters.filter_fees_in_state(fees_in_state)
            self.update_results(matching_programs)

        if self.fees_out_of_state is not None:
            matching_programs = self.filters.filter_fees_out_state(
                fees_out_of_state)
            self.update_results(matching_programs)

        if self.gpa is not None:
            matching_programs = self.filters.filter_gpa(gpa)
            self.update_results(matching_programs)

        if self.verbal is not None:
            matching_programs = self.filters.filter_gre_verbal(verbal)
            self.update_results(matching_programs)

        if self.quant is not None:
            matching_programs = self.filters.filter_gre_quant(quant)
            self.update_results(matching_programs)

        if self.boarding is not None:
            matching_programs = self.filters.filter_boarding(boarding)
            self.update_results(matching_programs)

        if self.books is not None:
            matching_programs = self.filters.filter_books(books)
            self.update_results(matching_programs)

        if self.overall_expenses is not None:
            matching_programs = self.filters.filter_overall_expenses(
                overall_expenses)
            self.update_results(matching_programs)

        if self.admission_rate is not None:
            matching_programs = self.filters.filter_admission_rate(admission_rate)
            self.update_results(matching_programs)
