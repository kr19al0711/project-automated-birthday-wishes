import logging 
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

#API_DOCUMENTATION_URL = "https://api.slack.com/methods"

class notifySlack():
    TOKEN = "xoxb-3786689328966-4190498962049-4OxEX8xEGKcZmf7CoDgX76mk"
    channel_id = ""
    slack_client = ""

    def __init__(self,channel_id = "C045M8XKUQ1"):
        self.slack_client = WebClient(self.TOKEN)
        self.channel_id = channel_id

    def post_message(self,message,parent_thread=None):
        try:
            result = self.slack_client.chat_postMessage(
                channel=self.channel_id,
                text=message,
                thread_ts=parent_thread
            )
            print(result)
            return result["ts"]
        except SlackApiError as e:
            print(f"Error: {e}")

def main(): 
    notifier = notifySlack()
    thread_id = notifier.post_message("notify_slack module is working fine!")
    notifier.post_message("Replying to original message",parent_thread=thread_id)

if __name__ == "__main__":
    main()