<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/tinyqubit/RedditBot_TopPosts/master/Images/Reddit_Logo.png" alt="Reddit" width="200">
  </br>
  Reddit Bot: Top Posts Grabber
  <br>
</h1>

# Purpose
Collect the all the posts from the ‘new’ section of a given subreddit, and only show the user the posts that meet your ‘up votes’ threshold.

## Instructions
Edit the values of these 3 variables to your preference.
```python
# The name of the subreddit you want to use.
(string) subreddit_name

# Number of posts you want to grab. The max is 1000.
(int) query_limit

# The minimum number of up votes a post must have to be eligible to display on graph.
(int) num_ups_threshold
```

Once you set your variable values, you can run the script and it will output reddit posts information to the console along with the graph output.

## Libraries Used
```
praw
datetime
time
matplotlib
numpy
```

## Example Graph Output
This displays the posts overtime. Each dot represents a single subreddit post you collected that met the num_ups_threshold requirement.
<p align="center">
<img src="https://raw.githubusercontent.com/tinyqubit/RedditBot_TopPosts/master/Images/Example_Plot_1.png" alt="Reddit" width="600">
</p>
