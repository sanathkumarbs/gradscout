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

<<<<<<< HEAD

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
=======
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
>>>>>>> e82a65fec1765e479de5d96ef8a73af7a8e5d4cb

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

        # creating the object of Filters()class
        self.filters = Filters()

    def run_selected_filters_1(self):

        final_list = []

        if self.overall_rank != None:
            final_list.append = filters.filter_rank_overall(overall_rank)

        if self.usnews != None:
            final_list.append = filters.filter_rank_usnews(usnews)

        if self.cwur != None:
            final_list.append = filters.filter_rank_cwur(cwur)

        if self.forbes != None:
            final_list.append = filters.filter_rank_forbes(forbes)

        if self.times != None:
            final_list.append = filters.filter_rank_times(times)

        if self.state != None:
            final_list.append = filters.filter_location_state(state)

        if self.city != None:
            final_list.append = filters.filter_location_city(city)

        if self.zipcode != None:
            inal_list.append = filters.filter_location_zip(zipcode)

        if self.region != None:
            final_list.append = filters.filter_location_region(region)

        if self.fees_in_state != None:
            final_list.append = filters.filter_fees_in_state(fees_in_state)

        if self.fees_out_of_state != None:
            final_list.append = filters.filter_fees_out_state(
                fees_out_of_state)

        if self.gpa != None:
            final_list.append = filters.filter_gpa(gpa)

        if self.verbal != None:
            final_list.append = filters.filter_gre_verbal(verbal)

        if self.quant != None:
            final_list.append = filters.filter_gre_quant(quant)

        if self.boarding != None:
            final_list.append = filters.filter_boarding(boarding)

        if self.books != None:
            final_list.append = filters.filter_books(books)

        if self.overall_expenses != None:
            final_list.append = filters.filter_overall_expenses(
                overall_expenses)

        if self.admission_rate != None:
            final_list.append = filters.filter_admission_rate(admission_rate)

        return set(final_list)