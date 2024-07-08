# Stock Price Alert System

This project monitors the stock price of a specified company and sends a WhatsApp message if the stock price changes by more than 5% in a day. It also fetches the latest news headline related to the company and includes it in the message.

## Features

- Monitors daily stock prices using the Alpha Vantage API.
- Fetches relevant news articles using the News API.
- Sends WhatsApp notifications using the Twilio API.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.6 or later installed on your machine.
- Accounts and API keys for Alpha Vantage, News API, and Twilio.

## API Registration

### Alpha Vantage API

1. Visit the [Alpha Vantage website](https://www.alphavantage.co/).
2. Sign up for a free API key.
3. Note down your API key.

### News API

1. Visit the [News API website](https://newsapi.org/).
2. Sign up for a free API key.
3. Note down your API key.

### Twilio API

1. Visit the [Twilio website](https://www.twilio.com/).
2. Sign up for an account and verify your phone number.
3. Note down your Account SID and Auth Token.
4. Create a new WhatsApp Sandbox (you’ll get a number to send messages from).

## Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables. Replace the placeholder values with your actual API keys, account SID, auth token, and phone numbers:

```plaintext
AV_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key
TWILIO_SID=your_twilio_sid
TWILIO_TOKEN=your_twilio_auth_token
TO_NUMBER=whatsapp:your_phone_number
FROM_NUMBER=whatsapp:your_twilio_sandbox_number
```

## Installation

1. Clone the repository
```plaintext
git clone https://github.com/Akos24/stock-price-alert.git
cd stock-price-alert
```

2. Create a virtual environment and activate it:
```plaintext
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
```plaintext
pip install -r requirements.txt
```

## Running the project
After setting up the environment variables and installing the dependencies, you can run the project using the following command:
```plaintext
python main.py
```

## Project Structure
```plaintext
.
├── alphavantage_api.py
├── news_api.py
├── twilio_api.py
├── main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

- alphavantage_api.py: Contains the AlphaVantageAPI class for fetching stock data.
- news_api.py: Contains the NewsAPI class for fetching news articles.
- twilio_api.py: Contains the TwilioApi class for sending WhatsApp messages.
- main.py: The main script that ties everything together.

## Customization
To monitor a different stock or company, change the values of the SYMBOL and COMPANY_NAME variables in main.py:
```python
SYMBOL = "TSLA"  # Change to the desired stock symbol
COMPANY_NAME = "Tesla Inc."  # Change to the desired company name
```

You can also change the lower bound of the percentage where you get alerts:
```python
PERCENTAGE_CHANGE = 5  # The lower bound of the change of percentage where the app sends alerts
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

### Explanation

- **Project Overview**: Describes the purpose and features of the project.
- **Prerequisites**: Lists the necessary tools and accounts.
- **API Registration**: Provides instructions for obtaining API keys.
- **Environment Variables**: Explains how to set up the `.env` file.
- **Installation**: Step-by-step instructions for setting up the project.
- **Running the Project**: How to execute the script.
- **Project Structure**: Describes the files and their purposes.
- **Customization**: How to monitor different stocks or companies.
- **License**: Information about the project's license.

This README should provide clear guidance on how to set up and use your project.