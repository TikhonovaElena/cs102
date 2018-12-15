import datetime as dt
from statistics import median
from typing import Optional

from api import get_friends
from api_models import User


def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"

    people = get_friends(user_id)
    for person in people:
        try:
            bdate = person['bdate'].split('.')
            if len(bdate) == 3:
                bdates.append([
                    int(bdate[0]),
                    int(bdate[1]),
                    int(bdate[2]),
                    ])
        except KeyError:
            pass
    byears = [date[2] for date in bdates]
    return dt.date.today().year - int(median(byears))