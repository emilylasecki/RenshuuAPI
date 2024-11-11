# main for running elements to be displayed on GUI
# add a feature so if renshuu is down it displays the message that it is currently unavailable.

import requests
import json
import pandas as pd
from api_key import api_key


#connect to Resnhuu server and load in content as needed
def main():

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }   
    url = 'https://api.renshuu.org/v1/profile/'  # get the number of reviews due today
    url2 = 'https://api.renshuu.org/v1/schedule/' # get the lists to extract how many of each type of review is due

    # part 1 - profile

    response = requests.get(url, headers=headers)

    print(response.status_code)
    x = response.json()
    print(json.dumps(x, indent=4, sort_keys=True))

    filter_fields=['adventure_level', 'real_name', 'studied', 'api_usage', 'studied', 'kao']

    dict_result = { key: x[key]  for key in x if key in filter_fields}

    with open("profile.json", "w") as outfile:  # extract desired fields into json file
        json.dump(dict_result, outfile)

    
    df = pd.read_json("profile.json", lines=True)
    df.to_excel("API_Stuff.xlsx")

   # print(dict_result)

    # part 2 - schedules

    response = requests.get(url2, headers=headers)
    x = response.json()
    print(json.dumps(x, indent=4, sort_keys=True))
    filter_fields=['schedules', 'today']
    dict_result = { key: x[key]  for key in x if key in filter_fields}

    with open("schedules.json", "w") as outfile:  # extract desired fields into another json file
        json.dump(dict_result, outfile)
        #data = json.load(outfile)

    f = open('profile.json')
    file = json.load(f)
    name = file['kao']
    print(name)

    r = open('schedules.json')
    file2 = json.load(r)

    history = file2['schedules']

    i=0

    for schedules in history:
        if "vocab" in schedules['name'] or "Vocab" in schedules['name'] or "Words" in schedules['name'] or "words" in schedules['name']:
            data = (  # need to find a better way to grab variables
                schedules['id'],
                schedules['name']
            )
            i=i+1

    print(",".join(map(str, data)))
    print(i)

    #name = file2['schedules']['id']
    #val = m['name']
    #print(val)

# reload stats upon click
# placeholder method
def reload():

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }   

    #endpoint = '/v1/profile'
    url = 'https://api.renshuu.org/v1/profile'

    response = requests.get(url, headers=headers)

    print(response.status_code) # 200 is good
    x = response.json()
    print(json.dumps(x, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()