import requests
from bs4 import BeautifulSoup
base_url = 'https://gitub.com'

def scrape_topic_repositories(topic, path=None):
    """Get the top repositories for a topic and write them to a CSV file"""
    if path is None:
        path = topic + '.csv'
    topic_page_doc = get_topic_page(topic)
    topic_repositories = get_top_repositories(topic_page_doc)
    write_csv(topic_repositories, path)
    print('Top repositories for topic "{}" written to file "{}"'.format(topic, path))
    return path

def get_top_repositories(doc):
    """Parse the top repositories for a topic given a Beautiful Soup document"""
    article_tags = doc.find_all('article', class_='border rounded color-shadow-small color-bg-secondary my-4')
    topic_repos = [parse_repository(tag) for tag in article_tags]
    return topic_repos

def get_topic_page(topic):
    """Get the web page containing the top repositories for a topic as a Beautiful Soup document"""
    topic_repos_url = 'https://github.com/topics/' + topic
    response = requests.get(topic_repos_url)
    if response.status_code != 200:
        print('Status code:', response.status_code)
        raise Exception('Failed to fetch web page ' + topic_repos_url)
    return BeautifulSoup(response.text)    

def parse_repository(article_tag):
    """Parse information about a repository from an <article> tag"""
    a_tags = article_tag.h1.find_all('a')
    username = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    repo_url = base_url + a_tags[1]['href'].strip()
    stars_tag = article_tag.find('a', class_='social-count float-none')
    star_count = parse_star_count(stars_tag.text.strip())
    return {'repository_name': repo_name, 'owner_username': username, 'stars': star_count, 'repository_url': repo_url}

def parse_star_count(stars_str):
    """Parse strings like 40.3k and get the no. of stars as a number"""
    stars_str = stars_str.strip()
    return int(float(stars_str[:-1]) * 1000) if stars_str[-1] == 'k' else int(stars_str)

def write_csv(items, path):
    """Write a list of dictionaries to a CSV file"""
    with open(path, 'w') as f:
        if len(items) == 0:
            return
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")

import sys

if __name__ == "__main__":
    topic = sys.argv[1]
    scrape_topic_repositories(topic)