from filters import Filters
from matchingAlgorithm import MatchingAlgo
from database import Firebase
import pandas as pd
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


class Recommend(object):
    """Class for Selecting Programs Matching Filters."""

    def __init__(self,
                 overall_rank=None,
                 rank=None,
                 usnews=None,
                 cwur=None,
                 forbes=None,
                 times=None,
                 state=None,
                 city=None,
                 zipcode=None,
                 region=None,
                 budget=None,
                 location=None,
                 in_state=None,
                 out_of_state=None,
                 gpa=None,
                 verbal=None,
                 quant=None,
                 boarding=None,
                 books=None,
                 overall_expenses=None,
                 admission_rate=None,
                 aoi=None):
        """Initializing Filter Class."""
        self.rank=rank
        self.overall_rank = overall_rank
        self.usnews = usnews
        self.cwur = cwur
        self.forbes = forbes
        self.times = times

        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.region = region
        self.location=location

        self.in_state = in_state
        self.out_of_state = out_of_state

        self.gpa = gpa
        self.verbal = verbal
        self.quant = quant

        self.budget=budget
        self.boarding = boarding
        self.books = books
        self.overall_expenses = overall_expenses

        self.admission_rate = admission_rate

        self.aoi = aoi

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

        self.firebase = Firebase()



    

    def filter_programs(self):
        """Filter the programs."""
        # Deploy Filter Selection
        specializations, user_selected_criteria = self.run_selected_filters()

        # Getting all the unique programs
        self.unique_programs = list(self.matches.keys())

        # Getting all common program intersection
        common = set.intersection(*map(set, self.common_programs))

        # Validating we atleast have one program matching one criteria
        # Fall back to all programs if no match is found

        if len(self.unique_programs) < 1:
            # Setting unique programs to all programs
            self.unique_programs = []
            self.unique_programs.extend(range(0, self.count - 1))

            # Setting all matches to zero
            self.matches = []
            self.matches = dict.fromkeys(self.unique_programs, 1)

            # Setting all common programs to all programs
            common = []
            common = common.extend(range(0, self.count - 1))

        return (common, self.unique_programs, self.matches, specializations, user_selected_criteria)





    def update_results(self, matching_programs):
        """Helper method to update matching programs results."""
        self.common_programs.append(matching_programs)

        for program in matching_programs:
            # Update the verbose program dict of results
            if self.matches is None:
                self.matches = {}
                self.matches[program] = 1
            elif program in self.matches:
                self.matches[program] += 1
            else:
                self.matches[program] = 1




    def run_selected_filters(self):
        specializations=[]
        user_selected_criteria=[]
        
#Based on the UI Options

        if self.rank is not None:
            matching_programs = self.filters.filter_rank_usnews(self.rank)
            self.update_results(matching_programs)
            matching_programs = self.filters.filter_rank_cwur(self.rank)
            self.update_results(matching_programs)
            matching_programs = self.filters.filter_rank_forbes(self.rank)
            self.update_results(matching_programs)
            matching_programs = self.filters.filter_rank_times(self.rank)
            self.update_results(matching_programs)
            rank_list=["usnews","cwur","forbes","times"]
            user_selected_criteria.extend(rank_list)


        if self.budget is not None:
            matching_programs = self.filters.filter_fees_out_state(self.budget)
            self.update_results(matching_programs)
            matching_programs = self.filters.filter_fees_in_state(self.budget)
            self.update_results(matching_programs)
            matching_programs = self.filters.filter_boarding(self.budget)
            self.update_results(matching_programs)
            matching_programs = self.filters.filter_books(self.budget)
            self.update_results(matching_programs)
            user_selected_criteria.append("in_state")
            user_selected_criteria.append("out_of_state")
            user_selected_criteria.append("boarding")
            user_selected_criteria.append("books")


        if self.aoi is not None:
            specializations.extend(self.aoi)


        if self.location is not None:
            matching_programs = self.filters.filter_location_region(self.location)
            self.update_results(matching_programs)







        """Individual filters."""
        if self.overall_rank is not None:
            matching_programs = self.filters.filter_rank_overall(self.overall_rank)
            self.update_results(matching_programs)

        if self.usnews is not None:
            matching_programs = self.filters.filter_rank_usnews(self.usnews)
            self.update_results(matching_programs)

        if self.cwur is not None:
            matching_programs = self.filters.filter_rank_cwur(self.cwur)
            self.update_results(matching_programs)

        if self.forbes is not None:
            matching_programs = self.filters.filter_rank_forbes(self.forbes)
            self.update_results(matching_programs)

        if self.times is not None:
            matching_programs = self.filters.filter_rank_times(self.times)
            self.update_results(matching_programs)



        if self.state is not None:
            matching_programs = self.filters.filter_location_state(self.state)
            self.update_results(matching_programs)

        if self.city is not None:
            matching_programs = self.filters.filter_location_city(self.city)
            self.update_results(matching_programs)

        if self.zipcode is not None:
            matching_programs = self.filters.filter_location_zip(self.zipcode)
            self.update_results(matching_programs)



        if self.in_state is not None:
            matching_programs = self.filters.filter_fees_in_state(
                self.in_state)
            self.update_results(matching_programs)
            
        if self.out_of_state is not None:
            matching_programs = self.filters.filter_fees_out_state(
                self.out_of_state)
            self.update_results(matching_programs)   

        if self.gpa is not None:
            matching_programs = self.filters.filter_gpa(self.gpa)
            self.update_results(matching_programs)

        if self.verbal is not None:
            matching_programs = self.filters.filter_gre_verbal(self.verbal)
            self.update_results(matching_programs)

        if self.quant is not None:
            matching_programs = self.filters.filter_gre_quant(self.quant)
            self.update_results(matching_programs)

        if self.boarding is not None:
            matching_programs = self.filters.filter_boarding(self.boarding)
            self.update_results(matching_programs)

        if self.books is not None:
            matching_programs = self.filters.filter_books(self.books)
            self.update_results(matching_programs)

        if self.overall_expenses is not None:
            matching_programs = self.filters.filter_overall_expenses(
                self.overall_expenses)
            self.update_results(matching_programs)

        if self.admission_rate is not None:
            matching_programs = self.filters.filter_admission_rate(
                self.admission_rate)
            self.update_results(matching_programs)

        return specializations, user_selected_criteria

        




    def get_user_criteria(self):
        if self.rank is not None:
            self.user_selected_criteria.extend("usnews")
            self.user_selected_criteria.extend("forbes")
            self.user_selected_criteria.extend("times")
            self.user_selected_criteria.extend("cwur")

        if self.in_state is not None:
            self.user_selected_criteria.extend("in_state")
            self.user_selected_criteria.extend("out_of_state")
            self.user_selected_criteria.extend("boarding")
            self.user_selected_criteria.extend("books")
            self.user_selected_criteria.extend("admission_rate")

        if self.gpa is not None:
            self.user_selected_criteria.extend("gpa")

        if self.verbal is not None:
            self.user_selected_criteria.extend("verbal")

        if self.quant is not None:
            self.user_selected_criteria.extend("quant")

        if self.aoi is not None:
            self.specializations_list.extend(aoi)
        else:
            self.specializations_list=['information_assurance_cyber_security',
                          'business_intelligence',
                          'computer_networks',
                         'web_application_development',
                          'library_science',
                          'management_consulting',
                          'human_center_design_engineering',
                          'information_architecture',
                          'software_engineering',
                         'data_science_analytics',
                          'distributed_systems']
    

        return (self.user_selected_criteria, self.specializations_list)

    #Getting the json list after the filtering
    def get_filtered_json(self, program_list):
        json_list=[]
        for each in program_list:
            result=self.firebase.get_detailed_program(each)
            json_list.append(result)
        return json_list

    def construct_dataframe(self, json_list, program_list):
        df=pd.io.json.json_normalize(json_list)
        df.columns = df.columns.map(lambda x: x.split(".")[-1])
        c_list=list(df.columns.values)
        col_list=[]
        for each in c_list:
            each=each.encode("utf-8")
            col_list.append(each)
   
 
        df = df.loc[:,['gpa','quant','verbal',
     'admission_rate',
     'business_intelligence',
     'computer_networks',
     'data_science_analytics',
     'distributed_systems',
     'human_center_design_engineering',
     'information_architecture',
     'information_assurance_cyber_security',
     'library_science',
     'management_consulting',
     'software_engineering',
     'web_application_development',
     'in_state',
     'out_of_state',
     'boarding',
     'books',
     'other',
        'length',
        'cwur',
        'forbes',
     'times',
     'usnews']]
        df["program_id"] = program_list
        return df





    def recommend_programs(self):

        set_list, program_list, program_dict, specializations, user_selected_criteria = self.filter_programs()

        json_list = self.get_filtered_json(program_list)

        df = self.construct_dataframe(json_list, program_list)

        #user_selected_criteria=["forbes","out_of_state"]

        #specializations_list=['information_assurance_cyber_security',
                        #  'business_intelligence',
                        #  'computer_networks']

        #user_selected_criteria, specializations_list=self.get_user_criteria()

        match=MatchingAlgo(df, program_list, specializations, user_selected_criteria)

        recommendations = match.rank_programs()

        return recommendations
        




        
