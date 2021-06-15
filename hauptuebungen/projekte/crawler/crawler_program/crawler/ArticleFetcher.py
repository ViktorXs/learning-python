import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .CrawledArticle import CrawledArticle


class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"

        while url != "":
            print(url)

            time.sleep(1)
            r = requests.get(url)
            page = BeautifulSoup(r.text, "html.parser")

            for card in page.select(".card"):
                title = card.select(".card-title span")[1].text
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                image = urljoin(url, card.select_one("img").attrs["src"])

                yield CrawledArticle(title, emoji, content, image)

            next_button = page.select_one(".navigation .btn")
            if next_button:
                next_page = next_button.attrs["href"]
                next_page = urljoin(url, next_page)
                url = next_page
            else:
                url = ""
                print("done")
