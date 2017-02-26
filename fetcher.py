import praw,io,random
from collections import deque
from urllib2 import urlopen
from PIL import Image,ImageTk

reddit = praw.Reddit("bot1")

def random_subs(num):
    q = deque()
    print("Finding random subreddits")
    for i in range(num):
        a = reddit.random_subreddit()
        q.append(a)
    print("Found them!")
    return(q)

# must be a way to do this without a seperate function??
def testWorkingLink(url):
    try:
        imageb = urlopen(url).read()
        data = io.BytesIO(imageb)
        img = Image.open(data)
        return(True)
    except:
        return(False)

def get_link(num):
    tested = deque()
    subreddits = random_subs(num)
    print("Looking for an Image")
    for i in range(num):
        selecter = random.randrange(num-1)
        if selecter not in tested:
            for sub in subreddits[selecter].new(limit=7):
                tested.append(selecter)
                if ("imgur" in sub.url or "reddituploads" in sub.url) and "gallery" not in sub.url:
                    if testWorkingLink(sub.url):
                        return(subreddits,sub.url,subreddits[selecter])
    print("No images found!")
    return(get_link(num))
