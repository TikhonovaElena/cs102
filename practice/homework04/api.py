import requests
import time
import config
from api_models import Message


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос

    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    for attempt in range(max_retries):
        try:
            res = requests.get(url, params=params, timeout=timeout)
            return res
        except requests.exceptions.RequestException:
            if attempt == max_retries - 1:
                raise
            backoff_value = backoff_factor * (2 ** attempt)
            time.sleep(backoff_value)


def get_friends(user_id, fields='bdate'):
    """ Вернуть данных о друзьях пользователя

    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    query_params = {
        'domain' : config.VK_CONFIG['domain'],
        'access_token': config.VK_CONFIG['access_token'],
        'user_id': user_id,
        'fields': fields
    }

    query = "{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.53".format(**query_params)
    response = get(query, query_params)
    response = response.json()
    error = response.get('error')
    if error:
        raise Exception(response['error']['error_msg'])
    return response['response']['items']


def messages_get_history(user_id, offset=0, count=200, amount=5000):
    """ Получить историю переписки с указанным пользователем

    :param user_id: идентификатор пользователя, с которым нужно получить историю переписки
    :param offset: смещение в истории переписки
    :param count: число сообщений, которое нужно получить
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "offset must be positive integer"
    assert count >= 0, "count must be positive integer"
    
    query_params = {
        'domain' : config.VK_CONFIG['domain'],
        'access_token': config.VK_CONFIG['access_token'],
        'user_id': user_id,
        'offset': offset,
        'count': count
    }

    query = "{domain}/messages.getHistory?access_token={access_token}\
&user_id={user_id}&v=5.53".format(**query_params)
    messages = []
    try:
        response = get(query)
        response = response.json()
        error = response.get('error')
        if error:
            raise Exception(response['error']['error_msg'])
        while amount > 0:
            query = "{domain}/messages.getHistory?access_token={access_token}\
&user_id={user_id}&offset={offset}&count={count}\
&v=5.53".format(**query_params)
            response = get(query)
            response = response.json()
            error = response.get('error')
            if error:
                raise Exception(response['error']['error_msg'])
            messages.extend(response['response']['items'])
            amount -= count
            query_params['offset'] += count
            query_params['count'] = min(amount, count)
            time.sleep(0.4)
    finally:
        return [Message(**message) for message in messages]
