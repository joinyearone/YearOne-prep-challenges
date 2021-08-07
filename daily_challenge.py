from pprint import pprint
import random
import yaml

import py_actions


def random_topic_chooser():
    """
    Opens the topics.yaml and randomly chooses a key where the difficulty 
    level is not 'Advanced'. 'Advanced' topics are not sent as a part of the
    daily challenge.

    """

    def choose_random_topic(data):
        topic = random.choice(list(data.keys()))

        if data[topic]['difficulty'] != 'Advanced':
            return topic
        else:
            return choose_random_topic(data)

    with open("topics.yaml", 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            topic = choose_random_topic(data)

            return data[topic]
        except yaml.YAMLError as exc:
            raise yaml.YAMLError(f"{exc}")


def format_post_body(topic, post_num):
    """
    Format text body to include standardized text:
    Example: 
    👏👏 Thanks to Kristal for the question! 👏👏
    Difficulty Level: Beginner
    Source: Leetcode

    """
    try:
        post_num += 1
        topic_title = topic['title']

        # TODO this formatted string creates an error in the posting, but we should figure it out
        # title = f"Daily Challenge #{post_num}: {topic_title}"

        body = topic['body']
        difficulty = topic['difficulty']
        source = topic['source'] if 'source' in topic else None
        author_email = topic['author_email'] if 'author_email' in topic else None
        author_name = topic['author_name'] if 'author_name' in topic else None

        shout = f"<h2>👏👏 Thanks to <u>{author_name}</u> for the question! 👏👏</h2><br>" \
            if author_name else ""
        level = f"<strong>Difficulty Level:</strong> {difficulty}<br>"
        sourced = f"<strong>Sourced from:</strong> {source}<br>" if source else ""

        pre_body = [shout, level, sourced, "<br>"]
        end_body = "<br><br> \
                    Don't forget to let us know that you've completed this question!<br> \
                    Leave a comment below 👇👇👇👇"
        post_body = "".join(pre_body) + body + end_body

        return (topic_title, post_body, author_email)
    except KeyError as e:
        return e


def actions():
    """
    Calls required functions to choose topic, format text body, and post to Circle.
    """
    try:
        topic = random_topic_chooser()

        post_num = py_actions.get_post_count(py_actions.DAILY_SPACE_ID)

        title, post_body, author_email = format_post_body(topic, post_num)

        py_actions.post_to_circle(
            py_actions.DAILY_SPACE_ID, title, post_body, author_email)

    except Exception as e:
        return e


print(actions())
