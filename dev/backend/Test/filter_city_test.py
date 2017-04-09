from database import Firebase

firebase = Firebase()

count = firebase.get_program_count()
	
city_list=[]

param="Seattle"

for pid in range(0, count):
	res=firebase.get_program_location(pid)
	if res['city']==param:
		city_list.append(pid)

print city_list

