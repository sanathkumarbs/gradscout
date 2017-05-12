import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import statsmodels.api as sm
from collections import defaultdict
from scipy import spatial
import operator


class MatchingAlgo(object):
    def __init__(self, df=None, program_list=None, user_specializations=None, criteria=None):
        self.df=df
        if not criteria:
            self.criteria = ["fees_out_of_state","gpa","overall_expenses","acceptance_rate"]
        else:
            self.criteria = criteria
        self.program_list = program_list
        self.user_specializations=user_specializations


    def filter_dataframe(self):
        all_specializations_list = ['business_intelligence',
     'computer_networks',
     'data_science_analytics',
     'distributed_systems',
     'human_center_design_engineering',
     'information_architecture',
     'information_assurance_cyber_security',
     'library_science',
     'management_consulting',
     'software_engineering',
     'web_application_development']
    
        user_input=[]
        user_input.extend(self.criteria)
        user_input.extend(self.user_specializations)
    
        drop_list=list(set(all_specializations_list) - set(self.user_specializations))
        sliced_data = self.df.drop(self.df.ix[:,drop_list].columns, axis=1)
    
        return sliced_data, user_input

    def get_scores(self, user_input):
        count=0
        for each in user_input:
            count=count+1
    #initializing the dictionary with preferences as key and hard coded scores for each of them 
        preference_score_dict=dict((el,0) for el in user_input)
        for key, value in preference_score_dict.iteritems():
            preference_score_dict[key]=100.0/float(count)
    
        return preference_score_dict

    def normalize_dataframe(self, sliced_data):
        colList=[]
        c=0
        for column in sliced_data:
            colList.append(column)
            c=c+1
        df = pd.DataFrame(columns=colList)
    
        for column in sliced_data:
            res=sliced_data[column]
            res=np.array(res).tolist()
            #print type(res)
            minimum=min(res)
            maximum=max(res)
            minimum=float(minimum)
            maximum=float(maximum)
            denom=maximum-minimum
            denom=float(denom)
            col=[]

            for value in res:
                if denom == 0.0:
                    temp=maximum
                else:
                    temp=float((value-minimum))/float(((maximum)-(minimum)))
                #To noamalized between 0 to 1
                    temp=temp*1
                col.append(temp)

            df[column]=pd.Series(col) 
    
        norm_df=df
    
        norm_df.drop(['program_id'],inplace=True,axis=1)
        lst=[]
    
        for i in self.program_list:
            lst.append(i)
        
        norm_df.insert( 0,'program_id', lst)
        index_list=norm_df.program_id.tolist()
        norm_df=norm_df.set_index([index_list])
        norm_df
    
        norm_dic=norm_df.set_index(norm_df.index).T.to_dict('dict')
    
        return norm_dic, norm_df

    def get_standard_vector(self, norm_df, preference_score_dict):
            vector_df=norm_df.drop('program_id',1)
    
            #Calculating the mean for every column from sliced dataframe
            mean_vector=vector_df.mean()
    
            #Creating the dictionary with key as column name and value as mean of normalized values for each program 
            mean_score=mean_vector.to_dict()
            #print "Mean score dictionary-----"
            #print mean_score

    
            #Calculating the absolute correlaiton
            corr_abs=vector_df.corr().abs()
    
            #creating the dictionary of the correlation scores
            corr_score=corr_abs.mean().to_dict()
            #print "correlation score dictionary-----"
            #print corr_score
    
            #Multiplying the mean score with the correlation score to get the final score
            standard_mean_score_dict={}
    
            for k in mean_score:
                standard_mean_score_dict[k]=mean_score[k]*corr_score[k]
    
            for preference in preference_score_dict:
                standard_mean_score_dict[preference]=standard_mean_score_dict[preference]*preference_score_dict[preference]
 
            return standard_mean_score_dict

            #Since we are again multiplying the related preference score with user input, we need to add 1 to it.
            #Example- 0.4 weightage to  DS should be considered as 1.4 since considering 0.4 would reduce it


            

    def get_final_score(self, standard_mean_score_dict, norm_df):
            recommendations={}
    
            #converting normalized dataframe into dictionary
            norm_dict=norm_df.set_index('program_id').T.to_dict()
    
            #creating list of values from dictionaries based on the sorted keys order from standard_mean_score_vector dictionary
            standard_score_list = [v for k, v in sorted(standard_mean_score_dict.iteritems())]
    
            for program, details_dic in norm_dict.iteritems():
            #print details_dic
                #Getting the sorted list of normalized values for every program
                sorted_list=[v for k, v in sorted(details_dic.iteritems())]
                result = 1 - spatial.distance.cosine(standard_score_list, sorted_list)
                recommendations[program]=result
    
            recommendations=sorted(recommendations.items(), key=lambda kv: kv[1], reverse=True)
    
    
            return recommendations

    def rank_programs(self):
        sliced_data, user_input = self.filter_dataframe()

        preference_score_dict=self.get_scores(user_input)

        norm_dic, norm_df = self.normalize_dataframe(sliced_data)

        standard_mean_score_dict = self.get_standard_vector(norm_df, preference_score_dict)

        recommendations=self.get_final_score(standard_mean_score_dict, norm_df)

        return recommendations
