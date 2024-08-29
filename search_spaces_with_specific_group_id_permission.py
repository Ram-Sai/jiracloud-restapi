import requests
from requests.auth import HTTPBasicAuth
import json

# Define your credentials and headers
auth = HTTPBasicAuth("<email>", "<api token>")
headers = {"Accept": "application/json"}

# Get all spaces
url_spaces = "https://<domain>/wiki/api/v2/spaces"
response_spaces = requests.request("GET", url_spaces, headers=headers, auth=auth)
spaces_data = json.loads(response_spaces.text)

# Group ID to search for
group_id = "<group ID>"

# Iterate through each space
for space in spaces_data['results']:
    space_name = space['name']
    space_id = space['id']
    
    # Get permissions for the current space
    url_permissions = f"https://<domain>/wiki/api/v2/spaces/{space_id}/permissions?limit=250"
    response_permissions = requests.request("GET", url_permissions, headers=headers, auth=auth)
    permissions_data = json.loads(response_permissions.text)
    
    # Filter permissions to check if the group ID has any permissions in this space
    group_permissions = [entry for entry in permissions_data['results'] if entry['principal']['id'] == group_id]
    
    # If the group has permissions in the space, print the space name and ID
    if group_permissions:
        print(f"Group ID: {group_id} has permissions in Space: {space_name}, ID: {space_id}")
