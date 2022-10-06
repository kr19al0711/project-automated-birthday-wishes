from calendar import month
from concurrent.futures import thread
import fetch_records
import notify_slack
import logging 
import datetime

logging.basicConfig(level=logging.DEBUG,filename="log.txt",format="%(asctime)s:%(levelname)s:%(message)s")

def main():

    logging.info("Starting Automated Birthday Wishes script.")
    date_today = datetime.datetime.now()
    fetch_obj = fetch_records.FetchRecord()
    slack_notifier = notify_slack.notifySlack()


    day = date_today.day
    month = date_today.month
    
    # try:
    person_list = fetch_obj.fetch_by_birthday(day,month)
    if len(person_list) == 0:
        logging.info("No one to wish today.")
    else:
        thread_id = slack_notifier.post_message("Automated Birthday Wish Script")
        for person in person_list:
            wish_string = "Wish {} a Very Happy Birthday".format(person["Name"])
            slack_notifier.post_message(message=wish_string,parent_thread=thread_id)
            logging.info(wish_string)


            
    # except Exception as e:
    #     logging.error(f"Some error occured {e}")
    #     print(e)


main()