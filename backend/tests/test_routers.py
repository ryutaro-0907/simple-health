"""test."""
from api.main import app
from fastapi.testclient import TestClient

from .conftest import temp_db

client = TestClient(app)


@temp_db
def test_create_user():
    """test create_user"""
    data = {
        'username':'test_user',
        'email': 'test@gmail.com',
        'password': 'testpassword'
    }

    response = client.post(
        "/api/users",
        json=data
    )

    assert response.status_code == 200
    content = response.json()
    assert content["username"] == data["username"]
    assert content["email"] == data["email"]
    assert content["password"] == data["password"]

    assert "id" in content


@temp_db
def test_get_records_by_user():
    data1 = client.post('/api/records', json={
        'user_id':0,
        # 'created_at': '2022-01-01',
        'happiness': 5,
        'motivation':5,
        'workout':'yes',
        'helped':'yes',
        'carories':0,
        'steps': 0,
        'meditation':0,
        'study':0,
        'work':0
    }).json()
    data2 = client.post('/api/records', json={
        'user_id':0,
        # 'created_at': '2022-01-02',
        'happiness': 5,
        'motivation':5,
        'workout':'yes',
        'helped':'yes',
        'carories':0,
        'steps': 0,
        'meditation':0,
        'study':0,
        'work':0
    }).json()

    response = client.get("/api/records/0")

    assert response.status_code == 200
    contents = response.json()
    for record in contents:
        if record["id"] == '1':
            assert record["user_id"] == data1["user_id"]
            assert record["happiness"] == data1["happiness"]
            assert record["motivation"] == data1["motivation"]
            assert record["workout"] == data1["workout"]
            assert record["helped"] == data1["helped"]
            assert record["carories"] == data1["carories"]
            assert record["steps"] == data1["steps"]
            assert record["meditation"] == data1["meditation"]
            assert record["study"] == data1["study"]
            assert record["work"] == data1["work"]

        elif record["id"] == '2':
            assert record["user_id"] == data2["user_id"]
            assert record["happiness"] == data2["happiness"]
            assert record["motivation"] == data2["motivation"]
            assert record["workout"] == data2["workout"]
            assert record["helped"] == data2["helped"]
            assert record["carories"] == data2["carories"]
            assert record["steps"] == data2["steps"]
            assert record["meditation"] == data2["meditation"]
            assert record["study"] == data2["study"]
            assert record["work"] == data2["work"]
