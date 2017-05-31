import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import statsmodels.api as sm
from collections import defaultdict
from scipy import spatial
import operator


class RecommendationAlgorithm(object):
    def __init__(self, df=None, set_list=None, program_list=None, program_dict=None, user_specializations=None, user_selected_criteria=None, result_size=None):
        self.df=df
        self.program_list = program_list
        self.program_dict = program_dict
        self.set_list = set_list
        self.user_specializations = user_specializations
        self.user_selected_criteria=user_selected_criteria
        self.result_size=int(result_size)


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
    
        drop_list=list(set(all_specializations_list) - set(self.user_specializations))
        sliced_data = self.df.drop(self.df.ix[:,drop_list].columns, axis=1)
    
        return sliced_data


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
                    temp=temp*100
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


    def get_vector_normalized(self, norm_df):
        max_col_list=[
    'in_state',
    'out_of_state',
    'gpa',
    'boarding',
    'books',
    'other',
    'quant',
        'verbal']

        max_col_list.extend(self.user_specializations)


        min_col_list=[
       'cwur',
    'forbes', 
    'times',
    'usnews',
    'admission_rate']

        df_max=norm_df[max_col_list]
        df_min=norm_df[min_col_list]
    
        max_vector=df_max.max()
        max_dict = max_vector.to_dict()
    
        min_vector=df_min.min()
        min_dict = min_vector.to_dict()
    
        L=[min_dict, max_dict]
        result = {}
        for d in L:
            result.update(d)
    
        standard_normalized_score_list = [v for k, v in sorted(result.iteritems())]

        return standard_normalized_score_list


    def get_sliced_dict(self, norm_df):
        col_list = [
        'program_id',
        'in_state',
    'out_of_state',
    'gpa',
    'boarding',
    'books',
    'other',
    'quant',
    'verbal',
    'cwur',
    'forbes', 
    'times',
    'usnews',
    'admission_rate']

        #if self.user_specializations not None:
        #    col_list = col_list.extend(self.user_specializations)

        score_df=norm_df[col_list]
        score_dict_norm=score_df.set_index('program_id').T.to_dict()

        return score_dict_norm


    def partition_dataframe(self, norm_df):
        col_list = [
        'program_id',
        'in_state',
        'out_of_state',
        'gpa',
        'boarding',
        'books',
        'other',
        'quant',
        'verbal',
        'cwur',
        'forbes', 
        'times',
        'usnews',
        'admission_rate']

        score_df=norm_df[col_list]
    
        if self.set_list is not None:
            set_score_df=norm_df.loc[norm_df['program_id'].isin(self.set_list)]
            set_dict=set_score_df.set_index('program_id').T.to_dict()
            remaining_list = list(set(self.set_list)^set(self.program_list))
            remaining_score_df = norm_df.loc[norm_df['program_id'].isin(remaining_list)]
            remaining_dict=remaining_score_df.set_index('program_id').T.to_dict()
        else:
            remaining_score_df = norm_df.loc[norm_df['program_id'].isin(remaining_list)]
            remaining_dict=remaining_score_df.set_index('program_id').T.to_dict()

        return set_dict, remaining_dict


    def get_score_combined(self, set_dict, remaining_dict, standard_normalized_score_list):
        recommendations={}

       

        if self.set_list is not None:
            for program, details_dic in set_dict.iteritems():
                sorted_list=[v for k, v in sorted(details_dic.iteritems())]
                #Finding the similarity as the spatial distance between two programs
                result = 1 - spatial.distance.cosine(standard_normalized_score_list, sorted_list)
                #Closer the distance to the one, closer it is to the generalized vector
                recommendations[program] = (round(result*100, 2))*2

            for program, details_dic in remaining_dict.iteritems():
                sorted_list=[v for k, v in sorted(details_dic.iteritems())]
                #Finding the similarity as the spatial distance between two programs
                result = 1 - spatial.distance.cosine(standard_normalized_score_list, sorted_list)
                #Closer the distance to the one, closer it is to the generalized vector
                recommendations[program] = (round(result*100, 2))
        else:
            for program, details_dic in remaining_dict.iteritems():
                sorted_list=[v for k, v in sorted(details_dic.iteritems())]
                #Finding the similarity as the spatial distance between two programs
                result = 1 - spatial.distance.cosine(standard_normalized_score_list, sorted_list)
                #Closer the distance to the one, closer it is to the generalized vector
                recommendations[program] = (round(result*100, 4))



        
        recommendations=sorted(recommendations.items(), key=lambda kv: kv[1], reverse=True)

        return recommendations


    def get_similarity_score_norm(self, score_dict_norm, standard_normalized_score_list):
        recommendations={}

        for program, details_dic in score_dict_norm.iteritems():
            sorted_list=[v for k, v in sorted(details_dic.iteritems())]
            #Finding the similarity as the spatial distance between two programs
            result = 1 - spatial.distance.cosine(standard_normalized_score_list, sorted_list)
            #Closer the distance to the one, closer it is to the generalized vector
            recommendations[program] = round(result*100, 2)

        recommendations=sorted(recommendations.items(), key=lambda kv: kv[1], reverse=True)

        return recommendations


    def get_final_result(self, recommendations):

        dict_tuple = dict(recommendations)
        list_val=[]

        for key, val in dict_tuple.iteritems():
            temp=dict_tuple.get(key)
            list_val.append(temp)
    
        max_val=float(max(list_val))
        min_val=float(min(list_val))

        denom=max_val-min_val

        res_dict={}
        for key, val in dict_tuple.iteritems():
            temp=dict_tuple.get(key)
            temp=(temp-min_val)/denom*100
            res_dict[key]=round(temp,2)

        res_dict

        recommendations=sorted(res_dict.items(), key=lambda kv: kv[1], reverse=True)
        return recommendations[:self.result_size]






    def rank_programs(self):
        sliced_data = self.filter_dataframe()

        norm_dict, norm_df = self.normalize_dataframe(sliced_data)

        standard_normalized_score_list = self.get_vector_normalized(norm_df)

        #score_dict_norm = self.get_sliced_dict(norm_df)

        set_dict, remaining_dict = self.partition_dataframe(norm_df)

        recommendations = self.get_score_combined(set_dict, remaining_dict, standard_normalized_score_list)

        final_result = self.get_final_result(recommendations)

        print "Set List"

        print self.set_list
        


        return final_result



