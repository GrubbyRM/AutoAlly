import requests


def get_car_brands():
    response = requests.get('https://carapi.app')
    if response.status_code == 200:
        return response.json()
    return None
