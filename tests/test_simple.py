import pytest
from aiohttp import web
from service.app import create_app
from service.config import Config

import service.handlers as handlers

# def ping(request):
#     return Response('pong')

# # @pytest.fixture
# async def client(loop, aiohttp_client):
#     app = Application()
#     app.router.add_routes([
#         get('/ping', ping)
#     ])
#     client = await aiohttp_client(app)
#     resp = client.get('/ping')
#     assert resp.status == 200

class MockTelegramSender:
    def __init__(*args, **kwargs):
        pass

    async def send_message(self, message):
        pass


def create_test_config():
    config_json = {
        'CHAT_ID': 1111111,
    }
    return Config.from_json(config_json)


def create_test_secrets():
    secrets = {'TELEGRAM_TOKEN': "111111111:AAAAAAAAAAAAAAAA-AAAAAAAAAAAAA"}
    return secrets


@pytest.fixture
def cli(loop, aiohttp_client, monkeypatch):
    app = create_app(
        secrets=create_test_secrets(), config=create_test_config()
    )

    setattr(app, 'telegram_sender', MockTelegramSender())
    return loop.run_until_complete(aiohttp_client(app))


async def test_ping(cli):
    resp = await cli.get('/v1/ping')
    assert resp.status == 200
    assert await resp.text() == 'PONG'


async def test_message(cli, ):
    resp = await cli.post('/v1/message', json={'methods': ['telegram'], 'message': {}})
    assert resp.status == 200
    assert await resp.json() == {'status': 'sent'}