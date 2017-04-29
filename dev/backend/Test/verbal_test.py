from database import Firebase

firebase = Firebase()

count = firebase.get_program_count()
	
verbal_list=[]

param=150

for pid in range(0, count):
	res=firebase.get_program_acad(pid)
	for each in res:
		if each=='gre':
			temp=res[each]
			val=temp['verbal']
			if val<=param:
				verbal_list.append(pid)


print verbal_list