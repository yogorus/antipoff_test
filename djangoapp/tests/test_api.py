import pytest
from tests.conftest import api_client
from rest_framework.test import APIClient

# flake8: noqa: f811

URL = "http://localhost:8000/api"


# @pytest.mark.django_db
# @pytest.fixture(scope="session")
# def create_two_cadastrals(api_client):
#     cadastral_number = "13:19:0202001:53"
#     result: list[dict] = []

#     for i in range(1, 3):
#         payload = {
#             "cadastral_number": cadastral_number,
#             "longitude": 170.66666,
#             "latitude": 89.5777,
#         }

#         response = api_client.post(f"{URL}/query/", data=payload, format="json")
#         assert response.status_code == 302
#         result_response = api_client.get(f"{URL}/result/{i}")
#         result_json = result_response.json()

#         result.append(result_json)

#     return result


def test_ping(api_client: APIClient) -> None:
    response = api_client.get(f"{URL}/ping/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_invalid_query_1(api_client: APIClient) -> None:
    payload = {
        "cadastral_number": "13:19:asdfas:53",
        "longitude": 170.66666,
        "latitude": 89.5777,
    }

    response = api_client.post(f"{URL}/query/", data=payload, format="json")
    assert response.status_code == 422


@pytest.mark.django_db
def test_invalid_query_2(api_client: APIClient) -> None:
    payload = {
        "cadastral_number": "13:19:0202001:53",
        "longitude": 190.66666,
        "latitude": 89.5777,
    }

    response = api_client.post(f"{URL}/query/", data=payload, format="json")
    assert response.status_code == 422


@pytest.mark.django_db
def test_invalid_query_3(api_client: APIClient) -> None:
    payload = {
        "cadastral_number": "13:19:0202001:53",
        "longitude": 170.66666,
        "latitude": 99.5777,
    }

    response = api_client.post(f"{URL}/query/", data=payload, format="json")
    assert response.status_code == 422


@pytest.mark.django_db
def test_invalid_query_4(api_client: APIClient) -> None:
    payload = {
        "cadastral_number": "13:19:0202001:53",
        "longitude": "text",
        "latitude": 89.5777,
    }

    response = api_client.post(f"{URL}/query/", data=payload, format="json")
    assert response.status_code == 422


@pytest.mark.django_db
def test_valid_query(api_client: APIClient) -> None:
    payload = {
        "cadastral_number": "13:19:0202001:53",
        "longitude": 170.66666,
        "latitude": 89.5777,
    }

    response = api_client.post(f"{URL}/query/", data=payload, format="json")
    assert response.status_code == 302

    result_response = api_client.get(f"{URL}/result/1/")
    assert result_response.status_code == 200

    result_json = result_response.json()

    assert result_json["cadastral_number"] == payload["cadastral_number"]
    assert result_json["longitude"] == payload["longitude"]
    assert result_json["latitude"] == payload["latitude"]
    assert "status" in result_json
    assert "date" in result_json


@pytest.mark.django_db
def test_history_after_creation(api_client: APIClient) -> None:
    cadastral_number = "13:19:0202001:53"
    # result: list[dict] = []

    for i in range(1, 3):
        payload = {
            "cadastral_number": cadastral_number,
            "longitude": 170.66666,
            "latitude": 89.5777,
        }

        response = api_client.post(f"{URL}/query/", data=payload, format="json")
        assert response.status_code == 302
        # result_response = api_client.get(f"{URL}/result/{i}")

    response = api_client.get(f"{URL}/history/{cadastral_number}/")
    print(f"{URL}/history/{cadastral_number}/")

    assert response.status_code == 200
    response_json = response.json()
    assert len(response_json) == 2
