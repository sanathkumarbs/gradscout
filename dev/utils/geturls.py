import requests
import json

f=open('UniversityName.txt','r')
uniList = f.read().split(',')
# Function to get the url response
def get_data(url, par):
    response = requests.get(url,params=par)
    if response.status_code == 200:
        data = response.json()
        print(response.text)
        print(response.status_code)
        return data
    else:
        print(response.text)
        print(response.status_code)

for i in range(26): # List of universities
    print(i)
    url = "https://api.data.gov/ed/collegescorecard/v1/schools"
    par = {'api_key':'nuTZILvRsNuwfuG5hhZ2MNaXtFtjGxeDiCpVQeNb','school.name': uniList[i],'_fields':'id,school.name,school.city,school.state,school.zip,school.region_id,school.ownership,location.lat,location.lon,school.carnegie_basic,2013.admissions.admission_rate.overall,2013.cost.attendance.academic_year,2013.cost.attendance.program_year,2013.cost.tuition.in_state,2013.cost.tuition.out_of_state,2013.cost.tuition.program_year,2013.aid.students_with_any_loan'}  
    data = get_data(url,par)