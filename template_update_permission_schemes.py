# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import time

url = "https://<domain>/rest/api/3/permissionscheme"

auth = HTTPBasicAuth("<email>", "<token>")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#data = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
#print(data[0]['name'])

# Parse the JSON response
data = json.loads(response.text)

cou = 1

# Iterate over the list of permission schemes and print the names
for scheme in data.get('permissionSchemes', []):
    cou +=1
    if  cou == 499:
        count = 1
        time.sleep(300)
    url = "https://<domain>/rest/api/2/permissionscheme/{}/permission".format(scheme['id'])

    auth = HTTPBasicAuth("<email>", "<token>")

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "holder": {
        "type": "group",
        "value": "<groupid>"
      },
      "permission": "<permission name>"
    } )

    response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
    )