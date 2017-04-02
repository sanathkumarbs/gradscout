import requests
import json
import pprint

f = open('UniversityName.txt', 'r')
uniList = f.read().split(',')


# Function to get the url response
def get_data(url, par):
    response = requests.get(url, params=par)
    if response.status_code == 200:
        data = response.json()
        # print(response.text)
        print(response.status_code)
        return data
    else:
        # print(response.text)
        print(response.status_code)

college_data = []

for university in uniList:
    print university
    url = "https://api.data.gov/ed/collegescorecard/v1/schools"
    par = {'api_key': 'nuTZILvRsNuwfuG5hhZ2MNaXtFtjGxeDiCpVQeNb',
           'school.name': university,
           '_fields': 'id,school.name,school.city,school.state,school.zip,location.lat,location.lon,school.region_id,school.ownership,school.carnegie_basic,2013.admissions.admission_rate.overall'}
    data = get_data(url, par)
    college_data.append(data[u'results'])

pprint.pprint(college_data)
