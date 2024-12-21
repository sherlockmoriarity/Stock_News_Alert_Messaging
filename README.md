# Stock_News_Alert_Messaging


Introduction

This project is a stock trading news alert messenger that monitors stock prices and sends timely alerts about relevant company news based on significant price changes.It is optimized for faster messaging using Twilio, ensuring traders receive crucial updates promptly.

⚙️ Tech Stack
>Alpha Vantage API:Used to get real-time stock prices of companies.
>
>News API:Used to fetch news related to the particular company.
>
>Twilio API:Used to send alerts to users.


🔋 Features

👉Real-Time Monitoring:Continuously tracks stock prices to detect significant changes.

👉News Integration:Fetches and filters news articles related to stock price movements.

👉Fast Alerts:Utilizes Twilio for instant messaging, delivering news alerts quickly.

👉User Customization: Allows users to set thresholds for price changes and select preferred communication channels.


🤸 Quick Start

Prerequisites

Make sure you have the following installed on your machine:

Git
Python

🚨Cloning the Repository

1. Clone the repository:
    bash
    git clone https://github.com/sherlockmoriarity/Stock-News-Alert-Messaging.git
    cd Stock-News-Alert-Messaging

2. Install the required dependencies:
    pip install requests
    pip install twilio

4. Set up environment variables for the APIs:
    
    export ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
    export NEWS_API_KEY=your_news_api_key
    export TWILIO_ACCOUNT_SID=your_twilio_account_sid
    export TWILIO_AUTH_TOKEN=your_twilio_auth_token
    
🤖Running the Project:

1. Run the script to start monitoring stock prices and receiving alerts:
    
    python main.py
    

2. Configure your preferences for stock price thresholds and communication channels in the `config.py` file.

