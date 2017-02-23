import praw

reddit = praw.Reddit("bot1")

def main():
    subreddit = reddit.subreddit("me_irl")
    for sub in subreddit.hot(limit=5):
        print sub.url


if __name__ == '__main__':
    main()
