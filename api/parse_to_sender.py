# Description: This file is responsible for sending data to Parser microservice.

import json
import httpx

url = 'http://localhost:8200/mews/xml'


def send_to_mews(mews_object: str) -> str:
    print('sending sender data to mews ', mews_object)
    print('type of mews_object is', type(mews_object))
    client = httpx.Client()
    response = client.post(url, json=mews_object, headers={'Content-Type': 'application/json'})
    response_json = json.loads(response.text)
    if response.status_code != 200:
        print('error in sending data to mews')
        print('response_json', response_json)
        return 'error'
    print('data sent to mews')
    print('response_json', response_json)
    return response_json
