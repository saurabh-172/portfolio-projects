import requests
from bs4 import BeautifulSoup
import pprint


def extract_response(num_pages):
    hn = []
    for i in range(num_pages):
        res = requests.get(f'https://news.ycombinator.com/?p={i+1}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline')
        subtext = soup.select('.subtext')
        hn += create_custom_hn(links, subtext)
    return sort_stories_by_votes(hn)
        
# print(votes[0].get('id'))


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'],reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.find('a').get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'href': href, 'votes': points})
    return hn

pprint.pprint(extract_response(2))