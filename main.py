import twint
from datetime import datetime
import schedule

# Getting The Time
time = datetime.now()
the_time = time.strftime("%H:%M")
# print(the_time)

# Configuring Twint
config = twint.Config()
config.Search = "Kalongo" # replace with a keyword of choice
config.Near = "Nairobi" # replace with a location (city, country). Comment out to delimit by location
config.Limit = 100 # limits search results
config.Since = "2021-01-01" # returns tweets since this date. Should follow YYYY-MM-DD formar
config.Until = "" # returns twint befor this date
# config.Hide_output = True # Hides output in terminal for better performance, uncomment to see in terminal
config.Filter_retweets = True # filters out retweets
config.Store_csv = True # saves tweets in a csv file
config.Custom_csv = ["id", "tweet", "user_id", "username", "date"]
config.Output = f"dumb_tweets_{the_time}.csv"

# The Search Function
def search():
    twint.run.Search(config)
    return

search()

# The Scheduler
# Scheduling this script to run every day at noon.
# schedule.every().day.at("12:00").do(search)
# May opt for crontab in linuz a server

# while True:
#   schedule.run_pending()
#   time.sleep(0.1)