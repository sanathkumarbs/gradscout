from database import Firebase

firebase = Firebase()
	
count = firebase.get_program_count()

overall_list=[]
param=10

'''
Overall rank is the sum of all ranks. Hence, it does not start from 
1 and ends at 59. Thus, to get to 10 programs, we need to simply
iterate over the top 10 program id

'''
for pid in range(0, param+1):
	res=firebase.get_program_rank(pid)
	overall_list.append(pid)

print overall_list





