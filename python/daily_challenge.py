import os
import requests
import json
import datetime
import urllib.parse
import py_actions

BINARYSEARCH_TOKEN = os.environ.get("BINARYSEARCH_TOKEN")

day_of_week = datetime.date.today().isoweekday()

def createContest():
    easy_med = [0,1]
    med_hard = [2,3]

    if day_of_week > 3:
        difficulties = med_hard
    else:
        difficulties = easy_med

    headers = {
        "x-access-token": f"{BINARYSEARCH_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "capacity": 50,
        "companies": [],
        "contestSessionId": False,
        "difficulties": difficulties,
        "educationalContest": True,
        "inviteOnly": True,
        "isPublic": False,
        "listId": False,
        "questionIds": [],
        "questionsPerSession": 4,
        "time": 28800,
        "timeMultiple": 1,
        "topics": []
    }
    algoURL = 'https://binarysearch.com/api/rooms'
    payload = json.dumps(payload)
    try:
        res = requests.request("POST", algoURL, headers=headers, data=payload).json()
        return res
    except Exception as e:
        return f"Error on pad fetch: {e}"


def format_post_body(contestURL):
    dt = datetime.datetime.today()
    date_string = f"{dt.month}/{dt.day}"
    if day_of_week > 3:
        difficulty = "Medium & Hard"
    else:
        difficulty = "Easy & Medium"
    try:
        title = f"Daily Algo Challenge: {date_string}"
        level = f"<strong>Difficulty Level:</strong> {difficulty}"
        body = f"""<strong>▶️ Here's today's YearOne Algo Challenge!</strong><br>
                {level}<br> <br>
                <h3> 🔗 <a href="{contestURL}" target="_blank">Join the challenge </a></h3>
                <br>
               <strong> ✅ Join the room | ✅ Hit 'Ready' | ✅ Begin the challenge!</strong><br>
                
                <br>
                <hr>
                <p><strong>If you haven't joined before, here's how to participate: </strong><br>
                <ol>
                <li> Sign up for an account at <a href="https://binarysearch.com" target="_blank">Binary Search </a></li>
                <li>Click the link above to join our private challenge room</li>
                <li>Don't forget to use the voice chat or room chat to see how others are doing!</li>
                </ol>
                </p>
                <br>
                <p>
                <strong> FAQs</strong>
                <br>
                <ul>
                <li>How long does the challenge run? It runs for 8 hours, beginning at 8 am Eastern Time </li>
                <li>How often does it run? Monday to Friday!</li>
                <li>Is it free? Of course!</li>
                </ul>
                </p>"""
        end_body = "<br> \
                    Don't forget to let us know that you've completed this question!<br> \
                    Leave a comment below 👇👇👇👇"

        post_body = "".join(body + end_body)
        encoded_body = urllib.parse.quote(post_body)

        return (title, encoded_body)
    except KeyError as e:
        return e
    except TypeError as f:
        return f"{f}"


def actions():
    """
    Calls required functions to choose topic, format text body, and post to Circle.
    """
    try:
        contest_data = createContest()

        room_slug = contest_data['uniqueSlug']

        contestURL = f'https://www.binarysearch.com/room/{room_slug}'

        title, post_body = format_post_body(contestURL)

        py_actions.post_to_circle(py_actions.DAILY_SPACE_ID, title, post_body)

    except Exception as e:
        return e


print(actions())