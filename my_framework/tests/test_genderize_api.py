import json

from http import HTTPStatus

from automation_lessons.api_collection.name_api import NameAPI
from automation_lessons.data.gender import Gender


def test_get_genderize(env):
    response = NameAPI().get_gender_by_name(env.genderize_url, 'Igor')
    assert response.status_code == HTTPStatus.OK


def test_body_genderize(env, create_gender):
    expected_gender = create_gender
    response = NameAPI().get_gender_by_name(env.genderize_url, 'Igor')
    from_json = json.loads(response.text)
    actual_gender = Gender.create_from_json(**from_json)
    assert actual_gender == expected_gender
