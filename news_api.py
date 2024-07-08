import requests


class NewsAPI:
    """
    A class to interact with the News API to get news articles.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"

    def get_company_news(self, company_name: str, num_articles: int = 3) -> list:
        """
        Get news articles for the given company name.

        :param company_name: Name of the company to search for news articles.
        :param num_articles: Number of articles to retrieve.
        :return: List of news articles.
        """
        params = {
            "q": company_name,
            "sortBy": "relevancy",
            "apiKey": self.api_key,
            "language": "en",
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])[:num_articles]
        return articles
