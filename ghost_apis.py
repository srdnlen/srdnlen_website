import requests
from datetime import datetime


def get_posts(ghost_api: str, key: str, limit: int, page:int=None) -> list:
    """
    Get posts

    Args:
        ghost_api (str): ghost api to get data
        key (str): api key
        limit (int): limit post number
        page (int): page to display

    Returns:
        list: list of posts
    """
    post_urls = ghost_api + '/posts/'
    params = {'key': key, 'limit': limit}
    if page:
        params['page']=page
    data = requests.get(post_urls, params=params).json()

    for i, p in enumerate(data['posts']):
        data['posts'][i]['published_at'] = datetime.strptime(p['published_at'], "%Y-%m-%dT%H:%M:%S.%f%z")

    return data['posts'], data['meta']


if __name__ == '__main__':
    p = get_posts("http://localhost:2368/ghost/api/content", key="ea9d0432ba13e4e6a8be44c6bc")
    print(p)