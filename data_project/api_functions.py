"""Script contains functions needed to interact with IGBD API."""

from requests import post
from os import environ
from dotenv import load_dotenv

def generate_token() -> dict:
    """Generates a Twitch auth token."""

    load_dotenv('.env')

    get_token_string = (
        f"https://id.twitch.tv/oauth2/token?"
        f"client_id={environ['TWITCH_CLIENT_ID']}&"
        f"client_secret={environ['TWITCH_APP_SECRET']}&"
        f"grant_type=client_credentials"
    )

    response = post(get_token_string)

    return response.json()
