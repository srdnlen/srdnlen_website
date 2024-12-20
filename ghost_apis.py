import requests
from datetime import datetime


def get_posts(ghost_api: str, key: str) -> list:
    """
    Get posts

    Args:
        ghost_api (str): ghost api to get data
        key (str): api key

    Returns:
        list: list of posts
    """
    post_urls = ghost_api + '/posts/'
    params = {'key': key}
    data = requests.get(post_urls, params=params).json()

    posts = list()
    for p in data['posts']:
        post = {
            'class': p['title'],
            'url': '/' + p['url'].split('/')[-2],
            'title': p['title'],
            'primary_tag':{
                'url': '/' + p['url'].split('/')[-2],
                'name': p['title']
            },
            'datetime': datetime.strptime(p['published_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
        }
        if p['excerpt']:
            post['excerpt'] = p['excerpt']
        posts.append(post)

    return posts


if __name__ == '__main__':
    get_posts("http://localhost:2368/ghost/api/content", key="ea9d0432ba13e4e6a8be44c6bc")