"""Script contains functions needed to interact with IGBD API."""

from os import environ
from requests import post
from dotenv import load_dotenv

BASE_URL = 'https://api.igdb.com/v4'

def generate_token() -> dict:
    """Generates a Twitch auth token."""

    load_dotenv('.env')

    get_token_string = (
        f"https://id.twitch.tv/oauth2/token?"
        f"client_id={environ['TWITCH_CLIENT_ID']}&"
        f"client_secret={environ['TWITCH_APP_SECRET']}&"
        f"grant_type=client_credentials"
    )

    response = post(get_token_string, timeout=60)

    return response.json()


def get_info_test() -> dict:
    """Tests API request."""

    load_dotenv('.env')

    query_string = BASE_URL + '/games'

    headers = {
        'Client-ID': environ["TWITCH_CLIENT_ID"],
        'Authorization': "Bearer " + environ["TWITCH_ACCESS_TOKEN"]
    }

    body = {"fields": "*"}

    # Use `json` instead of `data`
    response = post(query_string, headers=headers, json=body, timeout=60)

    return response.json()

if __name__ == '__main__':
    print(get_info_test())
