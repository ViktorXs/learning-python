import crawler
import csv

fetcher = crawler.ArticleFetcher()

with open("./articles/articles.csv", "w", newline="", encoding='utf-8') as csvfile:
    article_writer = csv.writer(csvfile, delimiter=";", quotechar='"')
    counter = 0  # Counter Vorgabe für beschränkung

    for article in fetcher.fetch():
        if counter == 19:  # Beschränken
            break
        counter = counter + 1

        article_writer.writerow([article.emoji, article.title, article.content, article.image])

        print(article.emoji + ": " + article.title)
    print("done")
