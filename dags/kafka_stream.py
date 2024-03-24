import json
import uuid
from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2024,3,24,16,41)
}



def get_date():
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    # get value first of index
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

# def stream_data():



# with DAG('user_automation',
#         default_args=default_args,
#         schedule_interval="@daily",
#         catchup=False) as dag:
#
#     streaming_task = PythonOperator(
#         task_id='streaming_data_from_api',
#         python_callable=stream_data
#     )

