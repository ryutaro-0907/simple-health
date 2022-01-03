"""test."""
from api.main import app
from fastapi.testclient import TestClient

from .conftest import temp_db

client = TestClient(app)


@temp_db
def test_create_project():
    """プロジェクト情報を登録できる."""
    data = {
        "name": "Hacarus社地盤検査",
        "description": "Hacarus社社屋建設PJ",
        "period": {
            "start_date": "2021-11-17",
            "end_date": "2021-11-17"
        }
    }

    response = client.post(
        "/projects",
        json=data
    )

    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["description"] == data["description"]
    assert content["period"]["start_date"] == data["period"]["start_date"]
    assert content["period"]["end_date"] == data["period"]["end_date"]
    assert "id" in content


@temp_db
def test_get_projects_by_organization():
    """ログイン中の組織のプロジェクト一覧を取得できる."""
    data1 = client.post("/projects", json={
        "name": "Hacarus社地盤検査",
        "description": "Hacarus社社屋建設PJ",
        "period": {
            "start_date": "2021-11-17",
            "end_date": "2021-11-17"
        }
    }).json()
    data2 = client.post("/projects", json={
        "name": "Hacarus社地盤検査2",
        "description": "Hacarus社社屋建設PJ2",
        "period": {
            "start_date": "2021-11-20",
            "end_date": "2021-11-25"
        }
    }).json()

    response = client.get("/projects/inspections")

    assert response.status_code == 200
    content = response.json()
    for c in content:
        project = c["project"]
        # inspections = c["inspections"]
        if project["id"] == data1["id"]:
            assert project["name"] == data1["name"]
            assert project["description"] == data1["description"]
            assert project["period"]["start_date"] == data1["period"]["start_date"]
            assert project["period"]["end_date"] == data1["period"]["end_date"]
            # TODO:
            # assert project["inspections"] == inspections
        elif project["id"] == data2["id"]:
            assert project["name"] == data2["name"]
            assert project["description"] == data2["description"]
            assert project["period"]["start_date"] == data2["period"]["start_date"]
            assert project["period"]["end_date"] == data2["period"]["end_date"]
            # TODO
            # assert project["inspections"] == inspections
