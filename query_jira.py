from jira import JIRA
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def create_jira_connection():
    conn_data = json.load(open('credentials_example.json'))
    authed_jira = JIRA(conn_data["jira_url"],auth=(conn_data["jira_username"], conn_data["jira_password"]))
    return authed_jira

def run_jira_query(conn, query_str):
    return conn.search_issues(query_str, maxResults=-1)

def prepare_jira_query(query_object, argument_list):
    query_orig_str = query_object["query_template"]
    if query_object["query_name"] == "block_crit_bugs":
        assignee_str = ""
        for assignee in argument_list:
            assignee_str += "assignee='" + assignee + "' or "
        assignee_str = assignee_str [:-4] #remove last chars
        query_orig_str = query_orig_str.replace("ASSIGNEE_LIST_PLACE_HOLDER",assignee_str)
    if query_object["query_name"] == "get_tickets_info":
        ticket_str = ""
        for ticket in argument_list["tickets"]:
            ticket_str += "id='" + ticket + "' or "
        ticket_str = ticket_str [:-4] #remove last chars
        query_orig_str = query_orig_str.replace("TICKET_LIST_PLACE_HOLDER",ticket_str)
    return  query_orig_str

