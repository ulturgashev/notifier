import argparse
import asyncio
import logging
import os

from aiohttp import web
from telegram_sender import TelegramSender

from config import Config
import handlers
import middleware


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class Application(web.Application):
    def __init__(self, loop=None, secrets=None, config=None, **kwargs):
        super().__init__(loop=loop, **kwargs)
        self.config = config
        self.telegram_sender = TelegramSender(
            token=secrets['TELEGRAM_TOKEN'], loop=loop, 
            config=self.config
        )


def _parse_args(description):
    print(description)
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--host')
    parser.add_argument('-p', '--port', type=int)
    return parser.parse_args()


def app_main(description, create_app):
    args = _parse_args(description)

    loop = asyncio.get_event_loop()

    secrets = {'TELEGRAM_TOKEN': os.environ['TELEGRAM_TOKEN']}
    config = Config.from_json('config.json')

    app = create_app(loop=loop, secrets=secrets, config=config)
    web.run_app(app, host=args.host, port=args.port)


def create_app(loop=None, secrets=None, config=None):
    app = Application(loop=loop, secrets=secrets, config=config)

    app.router.add_get('/v1/ping', handlers.ping)
    app.router.add_post('/v1/message', handlers.message)

    app.middlewares.append(middleware.error_middleware)

    return app


if __name__ == '__main__':
    app_main('app', create_app)
