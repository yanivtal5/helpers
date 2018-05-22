# Helpers
Various scripts/snippets I used for small/large projects

1. get_calories_from_garmin.py - python script used to fetch data from Garmin Connect website (https://connect.garmin.com) assuming username, password and ID are known , notes in the script
2. query_svn.py - python script to run a query on the SVN repository to get the last-day changes, for on premise. There are placeholders in the file to be replaced with actually data
3. query_jira.py - python script to run a query on JIRA to get bugs/epics/user stories, for on premise.
4. post_slack.py - python script to post messages on a Slack channel. 

Articles #2-#4 can be bundled together to post messages regarding SVN and JIRA events on a Slack channel, for example bug-alerts channel (monitors (using a cron job  or something similar) the JIRA and posts critical/blocker bugs) , or merges to Dev branch done each day with the corresponding JIRA ticket and status.
the additional - credentials_example.json, jira_queries_examples.json, teams_example.json files are used for configuration. Need to be filled with actual data.
