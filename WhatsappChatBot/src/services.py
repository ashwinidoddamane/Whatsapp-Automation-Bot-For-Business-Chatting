import os
import json
import random
import requests
import datetime

def get_date():
	dt = datetime.datetime.now()
	dt = dt.date()
	return dt.strftime('%B %d, %Y')

def get_time():
	dt = datetime.datetime.now()
	dt = dt.time()
	return dt.strftime('%I:%M %p')

def get_joke():
	url = 'https://rapidapi.com/collection/jokes'
	r = requests.get(url)
	data = r.json()
	return data['joke']

def get_quote():
	url = 'https://api.quotable.io/random'
	output = ''

	r = requests.get(url)
	quote = r.json()
	output += quote['content'] + '\n'
	output += f"     -{quote['author']}"

	return output

def fetch_apikey(api):
	with open('data/credentials.json') as f:
		data = json.load(f)
	key = data.get(api, None)

	return data[api]

def chatbot(api_key, query):
	url = f"http://api.wolframalpha.com/v1/result?appid={api_key}&i={query}%3f"
	r = requests.get(url, timeout=30)
	data = r.text
	
	if data == 'Wolfram|Alpha did not understand your input':
		return 'Couldn\'t understand the query'
	else:
		return data

def get_current_affairs():
    # Using a free current affairs API
    url = 'https://newsapi.org/v2/top-headlines'
    params = {'country': 'us', 'category': 'general', 'apiKey': 'your_news_api_key'}  # Replace with your News API key
    r = requests.get(url, params=params)
    news_data = r.json()
    news_headlines = [article['title'] for article in news_data.get('articles', [])]
    return news_headlines

def get_news():
    # Using a free news API
    url = 'https://newsapi.org/v2/top-headlines'
    params = {'country': 'us', 'apiKey': 'your_news_api_key'}  # Replace with your News API key
    r = requests.get(url, params=params)
    news_data = r.json()
    news_headlines = [article['title'] for article in news_data.get('articles', [])]
    return news_headlines

def get_general_knowledge():
    # Using web scraping for general knowledge
    url = 'https://www.gktoday.in/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    gk_elements = soup.find_all('h2', class_='post-title') 
    gk_headlines = [element.text.strip() for element in gk_elements]
    return gk_headlines

def get_sports_news():
    # Using a free sports news API
    url = 'https://newsapi.org/v2/top-headlines'
    params = {'country': 'us', 'category': 'sports', 'apiKey': 'your_news_api_key'}  # Replace with your News API key
    r = requests.get(url, params=params)
    sports_data = r.json()
    sports_headlines = [article['title'] for article in sports_data.get('articles', [])]
    return sports_headlines
