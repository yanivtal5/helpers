from slacker import Slacker
import json



def create_slack_connection():
    conn_data = json.load(open('credentials_example.json'))
    slack = Slacker(conn_data["slack_token"])
    return slack

def run_slack_post(conn, channel, post_str):
    return conn.chat.post_message(channel,post_str)

def prepare_post(opening_message,query_name,res):
    conn_data = json.load(open('credentials_example.json'))
    post = ""
    post += opening_message + "\n"
    post_body = ""
    if query_name == "block_crit_bugs":
        for item in res:
            post_body += str(conn_data["jira_url"]) + "/browse/" + str(item) + " " + str(item.fields.status) + " " + str(item.fields.summary) + " @" + str(item.fields.assignee) + "\n"
    if query_name == "get_tickets_info" or query_name == "get_bugs_last_5_min_info_according_to_priority":
        for item in res:
            post_body += str(item.fields.status) + " " + str(conn_data["jira_url"]) + "/browse/" + str(item) + " " + str(item.fields.summary) + " @" + str(item.fields.assignee) + "\n"
    post += post_body
    return post
