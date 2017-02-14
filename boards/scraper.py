import requests
from bs4 import BeautifulSoup


def get_gd_frontpage():
    result = requests.get('http://boards.na.leagueoflegends.com/en/f/mNBeEEkI')
    soup = BeautifulSoup(result.text, "html.parser")
    post_list = soup.find_all("tr", {"class": "discussion-list-item"})

    print("riot  votes|views  author  title")
    print("--------------------------------------------")
    for post in post_list:
        has_riot_comment = "  "
        title_string = post.find("div", {"class": "discussion-title"}).span.text
        author = post.find("span", {"class": "username"}).text
        view_count = post.find("td", {"class": "view-counts"}).span['data-short-number']
        upvotes = 0
        downvotes = 0

        if post.find("div", {"class": "pin"}) is None:
            upvotes = int(post.div['data-apollo-up-votes'])
            downvotes = int(post.div['data-apollo-down-votes'])

        if post.find("td", {"class": "riot-commented"}).find("a", {"class": "riot-fist"}) is not None:
            has_riot_comment = "+R"

        print("{0} {1:2}|{2:8} {3:24} {4}"
              .format(has_riot_comment, upvotes-downvotes, view_count, author, title_string))
