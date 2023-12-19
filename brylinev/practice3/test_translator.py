from fastapi.testclient import TestClient
from translate import app

# создаем тестового клиента
client = TestClient(app)


def test_en_ru():
    # отправляем запрос на перевод
    response = client.post(
        "/en-ru/", json={"text": "lesson"})
    # проверяем что нет ошибок и переведенная строка равна ожидаемой
    assert response.status_code == 200
    assert response.json().lower() == "урок"


def test_ru_en():
    # отправляем запрос на перевод
    response = client.post(
        "/ru-en/", json={"text": "урок"})
    # проверяем что нет ошибок и переведенная строка равна ожидаемой
    assert response.status_code == 200
    assert response.json().lower() == "lesson"
