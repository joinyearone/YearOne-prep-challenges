import json
import os
import yaml

from datetime import date
from pprint import pprint

import requests

API_TOKEN = os.environ.get("API_TOKEN")
COMMUNITY_ID = os.environ.get("COMMUNITY_ID")
CIRCLE_COMMUNITY_PATH = os.environ.get("CIRCLE_COMMUNITY_PATH")
DAILY_SPACE_ID = os.environ.get("DAILY_SPACE_ID")
TOPICS_PATH = "./topics.yaml"


def read_topics_yaml(yml_file=TOPICS_PATH):
    """
    Opens and reads a yml file, defaults to the topics yaml, if another file path isn't passed to the function.
    """
    
    try:
        with open(yml_file, "r") as stream:
            
                data = yaml.safe_load(stream)
                return data

    except TypeError as e:
        return TypeError(e)
    except yaml.YAMLError as exc:
        raise yaml.YAMLError(f"{exc}")



def post_to_circle(space_id, title_text, body_message, author_email=None):
    """
    Sends POST request to circle platform, posting new content to the community
    platform in the designated space.

    """

    url = f"{CIRCLE_COMMUNITY_PATH}/api/v1/posts?community_id={COMMUNITY_ID}&space_id={space_id}&"
    title = f"name={title_text}&"
    body = f"internal_custom_html={body_message}&"
    url_ending_params = (
        "is_comments_enabled=true&is_liking_enabled=true&is_truncation_disabled=false"
    )
    author = f"&user_email={author_email}"

    url_pieces = [url, title, body, url_ending_params]
    if author_email:
        # If the author is None, it'll default to an admin as the author
        url_pieces.append(author)

    post_url = "".join(url_pieces)

    payload = {}
    headers = {"Authorization": API_TOKEN}
    try:
        response = requests.request("POST",
                                    post_url,
                                    headers=headers,
                                    data=payload)
        return response.status_code
    except Exception as e:
        return f"Error on circle post: {e}"


def get_post_count(space_id):
    """
    Sends a call to the circle community call see how many posts have been posted. 
    """

    url = f"{CIRCLE_COMMUNITY_PATH}/api/v1/posts?community_id={COMMUNITY_ID}&space_id={space_id}"

    payload = {}
    headers = {"Authorization": API_TOKEN}
    try:
        circle_api = requests.request("GET",
                                      url,
                                      headers=headers,
                                      data=payload).json()
        post_count = len(circle_api)

        return post_count
    except Exception as e:
        return f"{e}"
