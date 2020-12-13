import datetime

from aiohttp import web
from http import HTTPStatus

from service.models import Message, Event


class BaseHttpException(Exception):
    pass


class BadRequest(BaseHttpException):
    status = HTTPStatus.BAD_REQUEST


def build_event(req_data: dict) -> Message:
    if 'message' not in req_data:
        raise BadRequest

    methods = req_data.get('methods', ['telegram'])
    message = req_data['message']
    return Event(
        methods=methods,
        message=Message(
            title=message.get('title', 'Unknown'),
            source=message.get('source', 'Undefined'),
            datetime=message.get('datetime', datetime.datetime.now()),
            text=message.get('text', '-'),
        )
    )


async def ping(request:web.Request):
    return web.Response(text='PONG')


async def message(request: web.Request):
    req_data = await request.json()
    event = build_event(req_data)
    try:
        await request.app.telegram_sender.send_message(
            message=event.message
        )
    except Exception as exc:
        print(f'could not send message: {exc}')
        return web.json_response({'status': 'failed'})
    
    return web.json_response({'status': 'sent'})
