import os
import requests
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def weather_fetch(city: str) -> dict:
    """Fetches the current weather for a given city."""
    if not WEATHER_API_KEY:
        return "Weather API key not found."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url)

    if res.status_code != 200:
        return f"Failed to fetch weather: {res.text}"

    data = res.json()
    return data
    # desc = data['weather'][0]['description']
    # temp = data['main']['temp']
    # return f"The weather in {city} is {desc} with a temperature of {temp}°C."




NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def news_fetch(topic: str) -> str:
    """Fetches top news headlines about a given topic."""
    if not NEWS_API_KEY:
        return "News API key not found."

    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&pageSize=3&apiKey={NEWS_API_KEY}"
    res = requests.get(url)

    if res.status_code != 200:
        return f"Failed to fetch news: {res.text}"

    articles = res.json().get("articles", [])
    if not articles:
        return "No news articles found."

    headlines = [f"- {a['title']} ({a['source']['name']})" for a in articles]
    return "Recent news articles:\n" + "\n".join(headlines)





def spacex_launch_fetch(_: str = "") -> dict:
    """Fetches upcoming SpaceX launch info from the public API."""
    url = "https://api.spacexdata.com/v4/launches/next"
    res = requests.get(url)

    if res.status_code != 200:
        return f"Failed to fetch SpaceX data: {res.text}"

    data = res.json()
    return data
    # name = data.get("name")
    # date = data.get("date_utc")
    # details = data.get("details", "No details provided.")

    # return f"Next SpaceX launch: {name}\nDate: {date}\nDetails: {details}"





def coingecko_fetch(coin: str) -> str:
    """Fetches current price and market info for a given cryptocurrency from CoinGecko."""
    coin = coin.lower()
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_market_cap=true"
    res = requests.get(url)

    if res.status_code != 200:
        return f"Failed to fetch crypto data: {res.text}"

    data = res.json()
    if coin not in data:
        return "Coin not found."

    price = data[coin]["usd"]
    market_cap = data[coin].get("usd_market_cap", "N/A")
    return f"{coin.capitalize()} price: ${price} (Market Cap: ${market_cap:.2f})"


def get_current_time():
    """
    Returns the current system time as a string in ISO 8601 format.
    Useful for agents that need the current timestamp.
    """
    return datetime.now().isoformat()
