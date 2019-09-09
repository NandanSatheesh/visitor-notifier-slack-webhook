import json
import requests

slack_data = {
	"attachments": [
        {
            "fallback": "Visitor Bot Attachment.",
            "color": "#36a64f",
            "author_name": "Visitor Notifier",
            "author_link": "https://github.com/NandanSatheesh",
            "title": "Hey there! :wave: \n",
            "text": "Mr. Aman is waiting at the reception for you",
            "fields": [
                {
                    "title": "Purpose",
                    "value": "Interview for SDE-3",
                    "short": "false"
                }
            ],
            "footer": "Just Another API on Slack",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png"
        }
    ]
}

webhook_url = open("webhook_url.txt","r").read()

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'})

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text))