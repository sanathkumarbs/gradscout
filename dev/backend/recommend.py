from filters import Filters
from recommendAlgo import RecommendationAlgorithm
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
        specializations, user_selected_criteria, result_size = self.run_selected_filters()

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

        return (common, self.unique_programs, self.matches, specializations, user_selected_criteria, result_size)



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
            result_size = self.rank
        else:
            self.rank=15
            result_size=self.rank
            #matching_programs = self.filters.filter_rank_absolute(self.rank)
            #self.update_results(matching_programs)
            #rank_list=["usnews","cwur","forbes","times"]



        if self.budget is not None:
            matching_programs = self.filters.filter_budget(self.budget)
            self.update_results(matching_programs)
            budget_list=["in_state", "out_of_state", "other", "boarding", "books"]
            user_selected_criteria.extend(budget_list)


        if self.aoi is not None:
            specializations.extend(self.aoi)


        if self.location is not None:
            matching_programs = self.filters.filter_location_region(self.location)
            self.update_results(matching_programs)

        return specializations, user_selected_criteria, result_size


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

      'cwur',
      'forbes',
     'times',
     'usnews']]
        df["program_id"] = program_list
        return df



    def recommend_programs(self):

        set_list, program_list, program_dict, specializations, user_selected_criteria, result_size = self.filter_programs()

        program_list.sort()

        list(set_list).sort()


        json_list = self.get_filtered_json(program_list)

        df = self.construct_dataframe(json_list, program_list)



        match=RecommendationAlgorithm(df, set_list, program_list, program_dict, specializations, user_selected_criteria, result_size)

        recommendations= match.rank_programs()



        return recommendations
        




        
