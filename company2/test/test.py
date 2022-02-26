import requests, pprint

payload = {
    'username': 'yuanyuan',
    'password': '12345678'
}

response = requests.post('http://localhost:8000/api/mgr/signin',
                         data=payload)

pprint.pprint(response.json())
