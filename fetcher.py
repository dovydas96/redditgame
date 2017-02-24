import praw,io,work
from collections import deque
from urllib2 import urlopen
from PIL import Image,ImageTk

reddit = praw.Reddit("bot1")

def random_subs(num):
    q = deque()
    for i in range(num):
        a = reddit.random_subreddit()
        q.append(a)
    return(q)

def testWorkingLink(url):
    try:
        imageb = urlopen(url).read()
        data = io.BytesIO(imageb)
        img = Image.open(data)
        return(True)

    except:
        return(False)

def get_link(num):
    subreddits = random_subs(num)
    for i in range(num):
        for sub in subreddits[i].hot(limit=5):
            if ("imgur" in sub.url or "reddituploads" in sub.url) and "gallery" not in sub.url:
                if testWorkingLink(sub.url):
                    return(subreddits,sub.url)
    return(get_link(num))
