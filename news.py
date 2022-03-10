from newsapi import newsapi_client
from datetime import date

api = newsapi_client.NewsApiClient(api_key='c934b817dd9e4f71bc26a906d09ec121')
today = date.today()



def get_ap_headlines():
    ap_news = api.get_top_headlines(sources="associated-press")

    f_title = ap_news['articles'][0]['title']
    f_content = ap_news['articles'][0]['content']
    f_link = ap_news['articles'][0]['url']

    s_title = ap_news['articles'][1]['title']
    s_content = ap_news['articles'][1]['content']
    s_link = ap_news['articles'][1]['url']

    return f_title, f_content, f_link, s_title, s_content, s_link

def get_tech_headlines():

    tech_news = api.get_everything(q="technology", from_param=today, to=today)

    f_title = tech_news['articles'][0]['title']
    f_content = tech_news['articles'][0]['content']
    f_link = tech_news['articles'][0]['url']

    s_title = tech_news['articles'][1]['title']
    s_content = tech_news['articles'][1]['content']
    s_link = tech_news['articles'][1]['url']

    return f_title, f_content, f_link, s_title, s_content, s_link

def get_us_headlines():
    us_headlines = api.get_top_headlines(country="us")

    f_title = us_headlines['articles'][0]['title']
    f_content = us_headlines['articles'][0]['content']
    f_link = us_headlines['articles'][0]['url']

    s_title = us_headlines['articles'][1]['title']
    s_content = us_headlines['articles'][1]['content']
    s_link = us_headlines['articles'][1]['url']

    return f_title, f_content, f_link, s_title, s_content, s_link



