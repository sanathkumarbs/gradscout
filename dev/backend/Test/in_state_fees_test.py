from database import Firebase

firebase = Firebase()

count = firebase.get_program_count()
	
fees_in_list=[]
param=50000
for pid in range(0, count):
	res=firebase.get_program_fees(pid)
	if res['in_state']<=param:
		fees_in_list.append(pid)
print fees_in_list

		