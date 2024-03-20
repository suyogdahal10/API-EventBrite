import requests
import json
api_key = ''
organization_id = ''

event_id = ''

organization_url = f'https://www.eventbriteapi.com/v3/organizations/{organization_id}/events/'
headers = {'Authorization': 'Bearer your_bearer_here'}


response = requests.get(organization_url, headers=headers)

if response.status_code==200:
    data = response.json()
    print(data)
    for events in data['events']:
        event_id =events['id'] #retreive event id from the JSON of the organization page.
        event_name = events['name']['text']
        event_link = events['url']
        event_image = events['logo']['url']
        print(event_link)
        print(f'Event ID: {event_id}')
        print (f'Event Name: {event_name}')
        event_attendee_url = f'https://www.eventbriteapi.com/v3/events/{event_id}/attendees/'
        response1 = requests.get(event_attendee_url, headers=headers)
        if response1.status_code == 200:
            data1 = response1.json()
            print('List of Attendees:')


            for person in data1['attendees']:
                first_name = person['profile']['first_name']
                last_name = person['profile']['last_name']
                email_name = person['profile']['email']
                print(first_name, last_name, email_name)
        else:
            print("Failed")
        print('====================')
else:
    print("Failed")
