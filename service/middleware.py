from aiohttp import web

import service.handlers as handlers
from service.models import Message


async def send_alert(app, exc):
    try:
        await app.telegram_sender.send_message(
            message=Message.make_alert(exc)
        )
    except Exception as exc:
        # TODO: add logging in the future
        print(exc)


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except handlers.BaseHttpException as err:
        return web.json_response(
            data={'status': err.status},
            status=err.status
        )
    except web.HTTPNotFound as exc:
        raise
    except Exception as exc:
        # selfcheck
        await send_alert(request.app, exc)
        return web.json_response(
            status=500
        )
