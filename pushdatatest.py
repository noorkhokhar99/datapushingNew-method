import requests
url = ''
payload = {
    
}

# GET
r = requests.get(url)

# GET with params in URL
r = requests.get(url, params=payload)

# POST with form-encoded data
r = requests.post(url, data=payload)

# POST with JSON 
import json
r = requests.post(url, data=json.dumps(payload))

# Response, status etc
r.text
r.status_code
if r.status_code == 200:
    print("Data successfully pushed to cloud.")
else:
    print("Failed to push the data to cloud.")


