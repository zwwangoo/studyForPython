import requests
from requests.exceptions import ConnectionError


def get_response(requests_params, result_type='str'):
    try:
        print(requests_params.url())
        response = requests.get(
            requests_params.url(),
            headers=requests_params.headers(),
        )
        if response.status_code == 200:
            if result_type == 'json':
                return response.json()
            else:
                return response.text
        return {}
    except ConnectionError:
        print('Failed to establish a new connection!')
        return get_response(requests_params, result_type)
