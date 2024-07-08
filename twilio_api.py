from twilio.rest import Client


class TwilioApi:
    """
    A class to interact with the Twilio API to send messages.
    """
    def __init__(self, account_sid: str, auth_token: str):
        self.client = Client(account_sid, auth_token)

    def send_message(self, to_number: str, from_number: str, symbol: str, percentage: float, direction: int,
                     headline: str, brief: str) -> None:
        """
        Send a WhatsApp message with the stock price change and a news headline.

        :param to_number: Recipient's phone number.
        :param from_number: Sender's phone number.
        :param symbol: Stock symbol.
        :param percentage: Percentage change in stock price.
        :param direction: Direction of the price change (1 for up, -1 for down).
        :param headline: News article headline.
        :param brief: Brief description of the news article.
        """
        direction_str = "↑" if direction >= 0 else "↓"
        body = f'{symbol} {direction_str} {percentage:.2f}%\nHeadline: {headline}\nBrief: {brief}'
        message = self.client.messages.create(
            from_=from_number,
            body=body,
            to=to_number
        )
        print(message.sid)
