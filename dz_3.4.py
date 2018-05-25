from pprint import pprint
from urllib.parse import urlencode
import requests

APP_ID = '0ca81308e6054719b01540c80bbaabb2'
OAUTH_URL = 'https://oauth.yandex.ru/authorize'

oauth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

# print('?'.join((OAUTH_URL, urlencode(oauth_data))))

TOKEN = 'AQAAAAAms-hEAAUCC7IbwQ5Sf0y4vyyf7QyPFzc'

users = {'roman': TOKEN}


def get_counters_list(token):
    headers = {
        'Authorization': 'OAuth {}'.format(token)
    }
    response = requests.get('https://api-metrika.yandex.ru/management/v1/counters',
                            headers=headers
                            )
    return (response.json())


def get_counter_info(token):
    headers = {
        'Authorization': 'OAuth {}'.format(token, counter_id)
    }
    response = requests.get('https://api-metrika.yandex.ru/management/v1/counter/{}'.format(counter_id),
                            headers=headers
                            )
    return response.json()


counters = get_counters_list(users['roman'])
#pprint(counters)

for counter in counters:
    counter_info = get_counter_info(users['roman'], counter['id'])
    pprint(counter_info)