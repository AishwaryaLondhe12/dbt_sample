import datetime
import requests


def lambda_handler(event, context):
    data = []
    # Loop through the list of contacts and extract the required fields
    contacts = api_response()
    for contact in contacts["value"]:
        item = {
            "email_address": contact['mail'],
            "given_name": contact['givenName'],
            "surname": contact['surname'],
            "mailNickname": contact['mailNickname']}

        # Return  the contact data in the required Fivetran JSON format
        data.append(item)
    date_time = datetime.datetime.now()
    date_time_str = date_time.isoformat()
    return {
        "state": {
            contacts: date_time_str:
    },
    "insert": {
        "contact": data
    },

    "schema": {
        "contactss": {
            "primary_key": ["emailaddress"]
        }
    },
    "has_more": False
    }

    def api_response():
        api_url = ""
        access_token = ""
        # Set the required headers for API request
        ={
            'Authorization': 'Bearer {}'.format(access_token)
        }
        # Send  the API  request to get the list of contacts
        # Check the status code of the response
        response = requests.get(api_url, headers=headers)
        if response.status_code != 200:
            return {
                "statusCode": response.status_code,
                "body": response.text
            }
        # Convert the response to JSON format
        contacts = response.json()
        return contacts
