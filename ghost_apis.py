import requests
from datetime import datetime

def _modify_post_data(posts: list) -> list:

    for i, p in enumerate(posts):
        posts[i]['published_at'] = datetime.strptime(p['published_at'], "%Y-%m-%dT%H:%M:%S.%f%z")
        posts[i]['url'] = '/' + posts[i]['url'].split('/')[-2] + '/'
    
    return posts

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

    posts = _modify_post_data(data['posts'])

    return posts, data['meta']

def get_posts_by_id(ghost_api: str, key: str, id: str) -> list:
    """
    Get post by id

    Args:
        ghost_api (str): ghost api to get data
        key (str): api key
        id (str): id of the post

    Returns:
        list: list of posts
    """

    post_urls = ghost_api + '/posts/' + id
    params = {'key': key}

    data = requests.get(post_urls, params=params).json()
    posts = _modify_post_data(data['posts'])
    return posts[0]


if __name__ == '__main__':
    # p = get_posts("http://localhost:2368/ghost/api/content", key="ea9d0432ba13e4e6a8be44c6bc", limit=8)
    # print(p)
    p = get_posts_by_id("http://localhost:2368/ghost/api/content", key="ea9d0432ba13e4e6a8be44c6bc", id="6772cb196c99f41d308f0a51")
    print(p)
