from http import HTTPStatus

from flora_api_client.presentations.main import ApplicationInfoResponse
from flora_api_client.utils.testing import mock
from flora_api_client.presentations.users import (
    RegistrationUserData, User
)
from flora_api_client.presentations.auth import AuthRequest, AuthResponse
from flora_api_client.presentations.users import (
    ConfirmDataForAuthRequest, ConfirmDataForAuthResponse
)


@mock('aiohttp.ClientSession.get',
      body={"version": "1.0.0", "name": "Flora Api"})
async def test_info(async_api_client):
    status, res = await async_api_client.info.get()
    assert status == HTTPStatus.OK
    assert isinstance(res, ApplicationInfoResponse)


@mock('aiohttp.ClientSession.post',
      body={
          "id": 1,
          "roles": ['user'],
          "registration_date": "2021-01-12T12:15:15",
          "name": "Lex",
          "discount": 0,
          "send_sms": True,
          "send_email": True,
          "language": "ru",
          "currency": "rub",
          "is_moderated": False,
          "data_for_auth": [
              {
                  "id": 1,
                  "service": "email",
                  "is_checked": False,
                  "value": "tulov.alex@gmail.com"
              },
              {
                  "id": 2,
                  "service": "phone",
                  "is_checked": False,
                  "value": "77077487125"
              }
          ]
      },
      status=HTTPStatus.CREATED)
async def test_registration_user(async_api_client):
    data = RegistrationUserData("cbvcbv", "77077487125",
                                "tulov.alex@gmail.com",
                                "lex", "ru", "rub", True, True)
    status, res = await async_api_client.users.register(data)
    assert status == HTTPStatus.CREATED
    assert isinstance(res, User)


user_data = {
    "id": 2,
    "roles": ['user', 'partner'],
    "registration_date": "2021-01-12T12:15:15",
    "name": "Lex",
    "discount": 0,
    "send_sms": True,
    "send_email": True,
    "language": "ru",
    "currency": "rub",
    "is_moderated": False,
    "data_for_auth": [
        {
            "id": 1,
            "service": "email",
            "is_checked": False,
            "value": "tulov.alex@gmail.com"
        },
        {
            "id": 2,
            "service": "phone",
            "is_checked": False,
            "value": "77077487125"
        }
    ]
}


@mock('aiohttp.ClientSession.post',
      body=user_data,
      status=HTTPStatus.CREATED)
async def test_registration_partner(async_api_client):
    data = RegistrationUserData("cbvcbv", "77077487125",
                                "tulov.alex@gmail.com",
                                "lex", "ru", "rub", True, True)
    status, res = await async_api_client.partners.register(data)
    assert status == HTTPStatus.CREATED
    assert isinstance(res, User)


@mock('aiohttp.ClientSession.post',
      body={
          "user": user_data,
          "token": "token",
          "long_token": "long_token"
      },
      status=HTTPStatus.OK)
async def test_auth(async_api_client):
    data = AuthRequest("77077487125", "cbvcbv")
    status, res = await async_api_client.auth.authenticate(data)
    assert status == HTTPStatus.OK
    assert isinstance(res, AuthResponse)


@mock('aiohttp.ClientSession.put',
      body={
          "success": True,
      },
      status=HTTPStatus.OK)
async def test_auth_data_confirm(async_api_client):
    data = ConfirmDataForAuthRequest("0123")
    status, res = await async_api_client.data_for_auth.confirm(1, data)
    assert status == HTTPStatus.OK
    assert isinstance(res, ConfirmDataForAuthResponse)
