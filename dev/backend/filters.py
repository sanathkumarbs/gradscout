from database import Firebase


class Filters(object):

    def __init__(self):
        # filtered_list=[]
        self.firebase = Firebase()
        self.count = self.firebase.get_program_count()

    def filter_rank_overall(self, param):
        overall_list = []
        for pid in range(0, param + 1):
            res = self.firebase.get_program_rank(pid)
            overall_list.append(pid)

        return overall_list

    def filter_rank_usnews(self, param):

        usnews_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_rank(pid)
            if res['usnews'] <= param:
                usnews_list.append(pid)

        return usnews_list

    def filter_rank_cwur(self, param):

        cwur_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_rank(pid)
            if res['cwur'] <= param:
                cwur_list.append(pid)

        return cwur_list

    def filter_rank_forbes(self, param):

        forbes_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_rank(pid)
            if res['forbes'] <= param:
                forbes_list.append(pid)

        return forbes_list

    def filter_rank_times(self, param):

        times_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_rank(pid)
            if res['times'] <= param:
                times_list.append(pid)

        return times_list


# 2. Location
#{u'city': u'Philadelphia', u'region_id': 2, u'zip': 19104, u'lon': -75.193618, u'state': u'PA', u'lat': 39.951002, u'region_name': u'Mid East'}

    def filter_location_state(self, param):

        state_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_location(pid)
            if res['state'] == param:
                state_list.append(pid)

        return state_list

        # return list(set(state_list)&set(filtered_list));

    def filter_location_city(self, param):

        city_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_location(pid)
            if res['city'] == param:
                city_list.append(pid)

        return city_list

        # return list(set(city_list)&set(filtered_list));

    def filter_location_zip(self, param):

        zip_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_location(pid)
            if res['zip'] == param:
                zip_list.append(pid)

        return zip_list

        # return list(set(zip_list)&set(filtered_list));

    def filter_location_region(self, param):

        region_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_location(pid)
            if res['region_name'] == param:
                region_list.append(pid)

        return region_list

        # return list(set(resion_list)&set(filtered_list));


# 3. Fees
#{u'out_of_state': 63000, u'in_state': 42690}

    def filter_fees_in_state(self, param):

        fees_in_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_fees(pid)
            if res['in_state'] <= param:
                fees_in_list.append(pid)

        return fees_in_list

        # return list(set(fees_in_list)&set(filtered_list));

    def filter_fees_out_state(self, param):

        fees_out_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_fees(pid)
            if res['out_state'] <= param:
                fees_out_list.append(pid)

        return fees_out_list

        # return list(set(fees_out_list)&set(filtered_list));


# 4. Score

#{u'gre': {u'quant': 167, u'verbal': 159}, u'gpa': 3}

    def filter_gpa(self, param):

        gpa_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_acad(pid)
            if res['gpa'] <= param:
                gpa_list.append(pid)

        return gpa_list

        # return list(set(fees_list)&set(filtered_list));

    def filter_gre_verbal(self, param):

        verbal_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_acad(pid)
            for each in res:
                if each == 'gre':
                    temp = res[each]
                    val = temp['verbal']
                    if val <= param:
                        verbal_list.append(pid)

        return verbal_list

        # return list(set(fees_list)&set(filtered_list));

    def filter_gre_quant(self, param):

        quant_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_acad(pid)
            for each in res:
                if each == 'gre':
                    temp = res[each]
                    val = temp['quant']
                    if val <= param:
                        quant_list.append(pid)

        return quant_list

        # return list(set(quant_list)&set(filtered_list));


# 5. Living


#{u'boarding': 14601, u'books': 1425, u'overall': 19351, u'other': 3325}

    def filter_boarding(self, param):

        boarding_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_living(pid)
            if res['boarding'] <= param:
                boarding_list.append(pid)

        return boarding_list

        # return list(set(boarding_list)&set(filtered_list));

    def filter_books(self, param):

        books_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_living(pid)
            if res['books'] <= param:
                books_list.append(pid)

        return books_list

        # return list(set(books_list)&set(filtered_list));

    def filter_overall_expense(self, param):

        overall_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_living(pid)
            if res['overall'] <= param:
                overall_list.append(pid)

        return overall_list

        # return list(set(overall_list)&set(filtered_list));


# 6. Admission Rate

# Filter by Admission Rate

    def filter_admission_rate(self, param):

        admission_list = []

        for pid in range(0, self.count):
            res = self.firebase.get_program_admission_rate(pid)
            if res >= param:
                admission_list.append(pid)

        return admission_list

        # return list(set(admission_list)&set(filtered_list));

    '''
	def filter_courses(param):

		course_list=[]
		courses=param.split(" ")

		for pid in range(0, self.count):
			res=firebase.get_program_courses(pid)
			for each in courses:
				if each in res:
					course_list.append(pid)


		return list(set(course_list)&set(filtered_list));




	'''
