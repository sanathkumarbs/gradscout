from database import Firebase

firebase = Firebase()

count = firebase.get_program_count()


	
verbal_list=[]

overall_list=[]




param=150

for pid in range(0, count):
	res=firebase.get_program_acad(pid)
	for each in res:
		if each=='gre':
			temp=res[each]
			val=temp['verbal']
			if val<=param:
				verbal_list.append(pid)


overall_list.append(verbal_list)

gpa_list=[]
param1=3.2
for pid in range(0, count):
	res=firebase.get_program_acad(pid)
	if res['gpa']<=param1:
		gpa_list.append(pid)


overall_list.append(gpa_list)

final=set.intersection(*map(set,overall_list))
        
    

  

