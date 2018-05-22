import os
import sys
import json

def get_last_day_merged_dev_tickets():
    s_date = os.popen('date --date="1 day ago" +%Y-%m-%d').read().strip()
    n_date = os.popen('date +%Y-%m-%d').read().strip()
    conn_data = json.load(open('credentials_example.json'))
    svn_data = {}
    if conn_data["source_control"] == "svn":
        svn_data["tickets"] = os.popen('svn log --username '+ conn_data["source_control_username"] +' --password '+ conn_data["source_control_password"] +' -r {'+n_date+'}:{'+s_date+'} '+ conn_data["source_control_url"] +' | grep -Eo "<PROJECT_PREFIX>-[0-9]{5}"').read().strip().split("\n")
        svn_data["revision"] = os.popen('svn log --username '+ conn_data["source_control_username"] +' --password '+ conn_data["source_control_password"] +' -r {'+n_date+'}:{'+s_date+'} '+ conn_data["source_control_url"] +' | grep -Eo "r[0-9]{1,5}"').read().strip().split("\n")
    return svn_data
