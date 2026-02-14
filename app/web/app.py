from typing import Optional
from aiohttp.web import Application as AiohttpApplication, View as AiohttpView
from aiohttp.web import run_app as aiohttp_run_app, Request as AiohttpRequest
from app.store import CrmAccessor

from app.store import setup_accessors
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    database: dict = {}
    crm_accessor: Optional[CrmAccessor]


app = Application()


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request





def run_app():
    setup_routes(app)
    setup_accessors(app)

    aiohttp_run_app(app)
