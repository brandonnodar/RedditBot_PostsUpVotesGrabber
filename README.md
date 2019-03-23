<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/tinyqubit/RedditBot_TopPosts/master/Images/Reddit_Logo.png" alt="Reddit" width="200">
  </br>
  Reddit Bot: Top Posts Grabber
  <br>
</h1>

<p align="center">
  <a href="#instructions">Instructions</a> •
  <a href="#libraries-used">Libraries Used</a> •
  <a href="#example-graph-output">Example Graph Output</a> •
  <a href="#future-features">Future Features</a>
</p>

# Purpose
Collect the all the posts from the ‘new’ section of a given subreddit, and only show the user the posts that meet your ‘up votes’ threshold. This uses the Reddit API praw library.

## Instructions
Before using the script, you'll need to set up your credentials to use the Reddit API. You'll notice at the bottom of the script you'll see:
```python
reddit = praw.Reddit(client_id = 'CLIENT_ID', client_secret = 'CLIENT_SECRET', username = 'USERNAME', password = 'PASSWORD', user_agent = 'USER_AGENT')
```
You can watch this video made by Sentdex to help you set this up!
https://www.youtube.com/watch?v=NRgfgtzIhBQ

Edit the values of these 3 variables to your preference.
```python
# The name of the subreddit you want to use.
(string) subreddit_name

# Number of posts you want to grab. The max is 1000.
(int) query_limit

# The minimum number of up votes a post must have to be eligible to display on graph.
(int) num_ups_threshold
```

Once you set your variable values, you can run the script and it will output the Reddit post's information to the console along with the graph output.

## Libraries Used
```
praw
datetime
time
matplotlib
numpy
```

## Example Graph Output
This displays the posts over time. Each dot represents a single subreddit post you collected that met the *num_ups_threshold* requirement.
<p align="center">
<img src="https://raw.githubusercontent.com/tinyqubit/RedditBot_TopPosts/master/Images/Example_Plot_1.png" alt="Reddit" width="700">
</p>

## Future Features
- Write post's data to a text file for more details statistics on each post. Will include things like number of comments, post title, update time, etc.
- Ability to ask user for variable values through the console instead of going into the script to change them.
- Ability to modify a search window for specific date and time a post was uploaded.
