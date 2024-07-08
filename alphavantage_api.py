import requests


class AlphaVantageAPI:
    """
    A class to interact with the Alpha Vantage API to get stock data.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def get_daily_stock_data(self, symbol: str) -> dict:
        """
        Get daily stock data for the given symbol.

        :param symbol: Stock symbol to retrieve data for.
        :return: JSON response with daily stock data.
        """
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def calculate_percentage_change(data: dict) -> float:
        """
        Calculate the percentage change in stock price between the last two days.

        :param data: JSON response with daily stock data.
        :return: Percentage change in stock price.
        """
        time_series = data["Time Series (Daily)"]
        dates = list(time_series.keys())
        if len(dates) < 2:
            raise ValueError("Not enough data to calculate the percentage change.")

        latest_close = float(time_series[dates[0]]["4. close"])
        previous_close = float(time_series[dates[1]]["4. close"])

        percentage_change = ((latest_close - previous_close) / previous_close) * 100
        return percentage_change

    @staticmethod
    def get_price_change_direction(data: dict) -> int:
        """
        Determine the direction of the stock price change between the last two days.

        :param data: JSON response with daily stock data.
        :return: 1 if the price increased, -1 if the price decreased, 0 if no change.
        """
        time_series = data["Time Series (Daily)"]
        dates = list(time_series.keys())
        if len(dates) < 2:
            raise ValueError("Not enough data to determine the price change direction.")

        latest_close = float(time_series[dates[0]]["4. close"])
        previous_close = float(time_series[dates[1]]["4. close"])

        if latest_close > previous_close:
            return 1
        elif latest_close < previous_close:
            return -1
        else:
            return 0
