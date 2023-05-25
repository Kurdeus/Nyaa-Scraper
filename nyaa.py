import feedparser


url = 'https://nyaa.si/?page=rss'
response = feedparser.parse(url)
output = [item.link for item in response.entries]
print(output)
