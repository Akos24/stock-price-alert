from dotenv import load_dotenv
import os
from alphavantage_api import AlphaVantageAPI
from news_api import NewsAPI
from twilio_api import TwilioApi

# Load environment variables from .env file
load_dotenv()

# Global variables for API keys and settings
AV_API_KEY = os.getenv("AV_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TO_NUMBER = os.getenv("TO_NUMBER")
FROM_NUMBER = os.getenv("FROM_NUMBER")
SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENTAGE_CHANGE = 5  # The lower bound of the change of percentage where the app sends alerts


def main() -> None:
    """
    Main function to monitor stock changes and send notifications if significant change is detected.
    """
    # Initialize APIs
    alpha_vantage_api = AlphaVantageAPI(AV_API_KEY)
    news_api = NewsAPI(NEWS_API_KEY)
    twilio_api = TwilioApi(TWILIO_SID, TWILIO_TOKEN)

    # Get stock data and calculate percentage change
    data = alpha_vantage_api.get_daily_stock_data(SYMBOL)
    try:
        percentage_change = AlphaVantageAPI.calculate_percentage_change(data)
        direction = AlphaVantageAPI.get_price_change_direction(data)

        # Check if the stock price changed by more than 5%
        if abs(percentage_change) >= PERCENTAGE_CHANGE:
            articles = news_api.get_company_news(COMPANY_NAME)
            if articles:
                headline = articles[0]['title']
                brief = articles[0]['description']
                # Send message via Twilio API
                twilio_api.send_message(TO_NUMBER, FROM_NUMBER, SYMBOL, percentage_change, direction, headline, brief)
            else:
                print("No news articles found")
        else:
            print("No significant change")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
