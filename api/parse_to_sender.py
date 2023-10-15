# Description: This file is responsible for sending data to Parser microservice.

import json
import httpx

url = 'http://localhost:8200/mews/send'


def send_to_mews(mews_object: str) -> str:
    print('sending parser data to mews ', mews_object)
    return 'success'
    # client = httpx.Client()
    # response = client.post(url, data=mews_object)
    # response_json = json.loads(response.text)
    # print('response_json', response_json)
    # return response_json
