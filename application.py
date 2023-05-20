from session import session
from models import Author, Article


def main():
    for author in session.query(Author):
        # articles = session.query(Article).filter_by(author_id=author.id)
        # for article in articles:
        #     print(author, article)
        for article in author.articles:
            print(author, article)


if __name__ == '__main__':
    main()
