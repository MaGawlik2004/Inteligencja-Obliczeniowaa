import praw
import json

# Twoje dane logowania do Reddita
reddit = praw.Reddit(
    client_id="16sOzPjeCzNNcMVfKgpMYg",
    client_secret="9hH7IhaXxSDpAxlihDAzwdNEyKfCJA",
    user_agent="lab08 by /u/Icy-Resident2107"
)

# Pobierz 100 postów z wybranego subreddita
subreddit = reddit.subreddit("developers")  # możesz zmienić np. na 'politics', 'funny', itp.
posts = []

for post in subreddit.hot(limit=100):
    posts.append({
        "title": post.title,
        "score": post.score,
        "url": post.url,
        "created": post.created_utc,
        "num_comments": post.num_comments
    })

# Zapisz do pliku JSON
with open("reddit_posts.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=4)

print("✅ Pobrano i zapisano 100 postów do pliku reddit_posts.json")
