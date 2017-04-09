from database import Firebase

firebase = Firebase()

count = firebase.get_program_count()
	
gpa_list=[]
param=3.2
for pid in range(0, count):
	res=firebase.get_program_acad(pid)
	if res['gpa']<=param:
		gpa_list.append(pid)

print gpa_list