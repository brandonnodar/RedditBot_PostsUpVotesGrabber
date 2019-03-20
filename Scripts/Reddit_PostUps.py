import praw
import datetime as dt
import time
import os.path
import csv
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates

# EDITABLE
subreddit_name = "gaming"
subreddit_section_name = "new"
query_limit = 1000 # How many posts to grab each time you query the subreddit. Max is 1000.
num_ups_threshold = 500 # The minimum number of up votes a post must have in order to be displayed on the graph.

# BE CAUTIOUS EDITING.
now = dt.datetime.now()
date = ""
directory_name = str()

# Initializations. DO NOT EDIT UNLESS LAST RESORT.
submission_ids_arr = []
post_stats_arr = []
post_stats_ups = []
post_stats_createdtime = []

def GrabPosts():
    global query_limit
    global post_stats_ups
    global submission_ids_arr

    total_posts = 0
    posts_meet_criteria = 0
    subreddit = reddit.subreddit(subreddit_name)
    submissions = subreddit.new (limit = query_limit)
    current_12hr_readable = str(dt.datetime.now().time().strftime("%I:%M:%S %p"))
    print("Grabbing posts..." + str(current_12hr_readable))

    for submission in submissions:
        submission_id = submission.id
        submission_shortlink = submission.shortlink
        submission_created = submission.created
        submission_ups = submission.ups
        submission_num_comments = submission.num_comments
        readable_datetime = dt.datetime.utcfromtimestamp(submission_created).strftime("%m/%d/%Y %I:%M:%S %p")
        readable_time = dt.datetime.utcfromtimestamp(submission_created).strftime("%H:%M:%S")
        total_posts += 1

        if not submission.stickied:
            if int(submission_ups) >= num_ups_threshold:
                posts_meet_criteria += 1
                post_stats_ups.append(submission_ups)
                submission_ids_arr.append(str(submission_id))
                d = dates.datestr2num(readable_time)
                post_stats_createdtime.append(d)
                print("Sub URL: " + str(submission_shortlink) + " // UPS: " + str(submission_ups) + " // NUM COM: " + str(submission_num_comments) + " // TIME POSTED: " + str(readable_datetime))

    print("\n" + str(posts_meet_criteria) + " out of " + str(total_posts) + " met the criteria.")
    print("UPDATED CALLS: " + str(reddit.auth.limits) + "\n\n------------------\n")

def GraphData():
    global post_stats_ups
    global post_stats_createdtime
    global submission_ids_arr

    print("Graphing data now...")

    x = np.array(post_stats_createdtime)
    y = np.array(post_stats_ups)
    plt.plot([], [])
    plt.scatter(x, y)

    plt.gcf().autofmt_xdate()
    myFmt = dates.DateFormatter('%m/%d %I:%M %p')
    plt.gca().xaxis.set_major_formatter(myFmt)
    plt.xlabel('Time')
    plt.ylabel('Up Votes')
    plt.title("Subreddit: " + str(subreddit_name) + " - New Section")
    plt.show()

def RunProgram():
    global date

    now = dt.datetime.now()
    date = now.date()
    GrabPosts()
    GraphData()

# PROGRAM EXECUTION STARTS HERE.
reddit = praw.Reddit(client_id = 'hbmOzzvWNwQb0A', client_secret = 'QaatCU-Wr0nuj7Wz8bvr4DX3D_8', username = 'soupnstuff', password = 'Teslamodel3', user_agent = 'soupy')
print("INITIAL CALLS: " + str(reddit.auth.limits))
RunProgram()