from database import Firebase

firebase = Firebase()

count = firebase.get_program_count()

admission_list=[]
param=0.10
for pid in range(0, count):
	res=firebase.get_program_admission_rate(pid)
	if res>=param:
		admission_list.append(pid)

print admission_list