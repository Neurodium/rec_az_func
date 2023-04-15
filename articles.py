import requests
import os

api_url = "https://rec-articles.herokuapp.com/api/"

def get_rec_articles(user_id):
    raw_data = requests.get(url=api_url+str(user_id)).json()
    results = [(article_id, rating) for article_id, rating in raw_data['pred'].items()]
    results.sort(key=lambda a: a[1])
    return results


