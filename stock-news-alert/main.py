import requests
from twilio.rest import Client

STOCK_NAME = "MSFT"
COMPANY_NAME = "MICROSOFT CORPORATION"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


STOCK_API_KEY = "your_alpha_vantage_api_key"
NEWS_API_KEY = "your_news_api_key"
TWILIO_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME ,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]
print(yesterday_closing)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing)

difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
print(difference)

diff_percentage = (difference/float(yesterday_closing))*100
print(diff_percentage)

if diff_percentage>2:
    news_parameter= {
       "apiKey": NEWS_API_KEY,
       "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params = news_parameter)
    articles = news_response.json()["articles"]
    three_articles= articles[:3]
    print(three_articles)

    article_list = [f"Headline:{article["title"]} \nBrief: {article ["description"]} " for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in article_list:
        message = client.messages.create(
            body= article,
            from_="+12..........",
            to= "+91.........."
        )

