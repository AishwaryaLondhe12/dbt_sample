import datetime
import requests
def lambda_handler(event, context):
    data = []

 # Loop through the list of contacts and extract the required fields

    contacts = api_response()
    for contact in contacts["contacts"]:
        item = {
            "id": contact['id'],
            first_name": contact['firstame'],
            "lastname": contact['lastname']}
# Return the contact data in the required Fivetran JSON format

        data.append(item)
    date_time = datetime.datetime.now()
    date_time_str = date_time.isoformat()
    return {
    "state": {
            "contacts": date_time_str
            },
             "insert": {
            "contacts": data
                     },

             "schema": {
                 "contacts": {
                 "primary_key": ["id"]
 }
},

             "hasMore": False

}

def api_response():
     api_url = 'https://smf.crm3.redtailtechnology.com/api/public/v1/contacts?page=1'
 # Set the required headers for the API request
     headers = {'Authorization': 'NkFDQzMxREUtMjQxNy00QUVELUI3RTAtRjcxRTMyNjMxRUY0OjEzNDhGMjBGLUY5OTAtNDU5MC1BM0NBLTE1OTc4Mzg5OTBGRg=='}
 # Send the API request to get the list of contacts
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