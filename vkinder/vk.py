
import vk

APP_ID = 6120276
VERSION = 5.92
MALE = 2
FEMALE = 1

def search(login, password, fields, age_min, age_max, sex) -> list:
    """	
	login: ввод логина пользователя
	пароль: Пароль пользователя
	поля: поля для использования в качестве фильтра общих свойств
	age_min: минимальный возраст кандидата
	age_max: максимальный возраст кандидата
	пол: пол требуемого кандидата (мужчина/женщина)
	возврат: список кандидатов	
    """
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password
                             )

    vkapi = vk.API(session)

    return vkapi.users.search(
        v=VERSION,
        count=1000,
        sex=sex,
        age_from=age_min,
        fields=','.join(fields),
        age_to=age_max,
    )['items']


def get_photos(login, password, owner_id) -> list:
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password
                             )

    vkapi = vk.API(session)

    photos_response = vkapi.photos.get(
        v=VERSION,
        count=1000,
        album_id='profile',
        extended=1,
        owner_id=owner_id,
    )['items']

    return photos_response
