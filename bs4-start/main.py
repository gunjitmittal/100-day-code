from bs4 import BeautifulSoup
import requests

page = requests.get("https://news.ycombinator.com/")
contents = page.text
soup = BeautifulSoup(contents, "html.parser")
article_texts = []
article_links = []
stories = soup.find_all(name="a", class_="titlelink")
scores = soup.find_all(name="span", class_="score")
for story in stories:
    story_text = story.getText()
    story_link = story.get("href")
    article_links.append(story_link)
    article_texts.append(story_text)
score_list = [int(score.getText().split(" ")[0]) for score in scores]

max_score = max(score_list)
max_index = score_list.index(max_score)
print(article_texts[max_index])
print(article_links[ma])
print(score_list)