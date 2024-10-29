"""
    Dify api 
"""

import requests

DIFY_BASE="https://api.dify.ai/v1"

# completion-messages:
# post, with inputs dict
def completion_messages(inputs, api_key):
    url = DIFY_BASE + "/completion-messages"
    inputs = {
        "inputs": inputs,
        "response_mode": "blocking",
        "user": "test",
    }
    # set key as bearer header
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=inputs, headers=headers).json()

    # parse response
    response = response["answer"]

    return response