import os
import requests
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()

# Access variables
earthdata_api_token = os.getenv("EARTHDATA_API_TOKEN")

# These ones work:
# data = 'GPM_3IMERGHH_06_precipitationCal'
# latitude = 4.75
# longitude = 0.55
# time_start = '2000-06-01T00:00:00'
# time_end = '2000-06-21T19:30:00'

# These (new) ones don't; it returns: `{"message":null}`
data = 'GPM_3IMERGDL_06_precipitationCal'
latitude = 52.076 # Latitude for Mica dam
longitude = 118.566 # Longitude for Mica dam
time_start = '2022-01-01T00:00:00Z' # Jan 1, 2022 @ 6AM PST
time_end = '2022-01-02T00:00:00Z' # Jan 2, 2022 @ 6AM PST

headers = {
    'authorizationtoken': earthdata_api_token,
}

params = (
    ('data', data),
    ('location', f'[{latitude},{longitude}]'),
    ('time', f'{time_start}/{time_end}'),
)

response = requests.get('https://api.giovanni.earthdata.nasa.gov/timeseries', headers=headers, params=params)
print(response.text)