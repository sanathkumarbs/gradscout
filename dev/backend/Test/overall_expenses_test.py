from database import Firebase

firebase = Firebase()

count = firebase.get_program_count()
	
overall_list=[]
param=30000
for pid in range(0, count):
	res=firebase.get_program_living(pid)
	if res['overall']<=param:
		overall_list.append(pid)

print overall_list