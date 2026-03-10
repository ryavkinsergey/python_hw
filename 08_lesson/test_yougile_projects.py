import pytest
import uuid
from yougile_api import YougileProjects

URL = "https://ru.yougile.com/api-v2"
TOKEN = "токен"
COMPANY_ID = "ид компании"


@pytest.fixture
def api():
    return YougileProjects(URL, TOKEN, COMPANY_ID)


def unique_name():
    return f"Project_{uuid.uuid4().hex[:6]}"


def test_post_project_positive(api):
    name = unique_name()
    response = api.create_project(name)
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_project_positive(api):
    res = api.create_project(unique_name())
    project_id = res.json()["id"]

    response = api.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_put_project_positive(api):
    res = api.create_project(unique_name())
    project_id = res.json()["id"]

    new_name = "Updated_" + unique_name()
    response = api.update_project(project_id, new_name)
    assert response.status_code == 200

    get_response = api.get_project(project_id)
    assert get_response.json()["title"] == new_name


def test_post_project_negative_empty_title(api):
    response = api.create_project("")
    assert response.status_code >= 400


def test_get_project_negative_not_found(api):
    fake_id = str(uuid.uuid4())
    response = api.get_project(fake_id)
    assert response.status_code == 404


def test_put_project_negative_invalid_id(api):
    response = api.update_project("not-valid-id", "New Name")
    assert response.status_code >= 400
