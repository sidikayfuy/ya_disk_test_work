import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

API_URL = 'https://cloud-api.yandex.net/v1/disk'


def check_api_availability():
    try:
        response = requests.get(API_URL, timeout=5,
                                headers={'Authorization': 'OAuth ' + settings.YANDEX_API_KEY})
        if response.status_code != 200:
            raise ImproperlyConfigured(f"API is not available. Status code: {response.status_code}. Message: {response.text}")
        print("API is available!")
    except requests.exceptions.RequestException as e:
        raise ImproperlyConfigured(f"API request failed: {e}")
