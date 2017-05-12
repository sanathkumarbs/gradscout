import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import statsmodels.api as sm
'''
One way to assign weights to the ser filtered list is directly
using the scores from the correlation matrix

Example:
1. Location
2. Rank
3. GPA

Get the list of university IDs along with the user criteria(Location, Job, )

1. Input: 	a) List of program ids from filter module

			b) User selected criteria

			c) for creating the weights, pass only the numeric parameters to the users

			d) you should pass the ids filtered based on the location, curriculum, or other textual information 

2. Need to have correlation values for each quantitative criteria : Example - we can have n by n array showing the values  between every two options 

3. To calculate weights based on the Correlation values(get_weights): Input would be list of university ids after filtering and the list of user criteria

4. To calculate the score based on the input(get_scores): For score calculations,  input would be again the university ids after filtering them 
and user criteria list. 

We then need to have the noamalized table values for all 60 programs. Then for the UW, we would go 
to the UW entry in the table for look for the normalized value under location, rank and gpa.

5. get_count_weight(list of program ids):Also, we will have a list where we can see ids and their counts. 
More the count, more the percentage given to that program in the final calculation.

score(uw for location)*wt(for location)+  

'''

'''
#get_weights(list of ids, list of user criteria)

1. Maintains a dictionary where:

key: quantitative criteria for user input
value: dictionary of quantitative criteria and it's correlation valueor 

for criteria in list:
	if dict.key==criteria:
		temp=dict[key]
		for key in temp:
			for criteria in list:
				if key==criteria:
					list.append(temp[criteria])
				

			list.append



	  

dict={'location':{'location':1.0,'gpa':0.04,'in_state_fees':0.06};
		'gpa':{'location':0.06,'gpa':1.0,.........}
		'in_state_fees':{.........}}

#get_scores(list of ids, list of user criteria)
#get_count_weights(list of program ids)


'''
class MatchingAlgorithm(object):



	def get_weights():



	def get_count_weights():


	def get_scores():


	def get_final_list():








