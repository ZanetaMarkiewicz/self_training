import requests
from bs4 import BeautifulSoup


# path = r"D:\!_Python_trainig\scripts_IS\NYT_data.csv"


# def data_download():
#     data_url = "https://www.nytimes.com"
#
#     nyt_data = requests.get(data_url)
#     soup = BeautifulSoup(nyt_data.text)
#
#     for story_heading in soup.find_all(class_="story-heading"):
#         if story_heading.a:
#             print(story_heading.a.text.replace("\n", " ").strip())
#         else:
#             print(story_heading.contents[0].strip())

    # title = soup.find_all('span', recursive=False, )
    # # print(soup.prettify())
    # print(title)
#
# data_download()


soup = BeautifulSoup(requests.get("https://www.nytimes.com"))