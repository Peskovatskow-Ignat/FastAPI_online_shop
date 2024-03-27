from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from webapp.api.v1.auth.router import auth_router
from webapp.api.v1.crud.cart.router import cart_router
from webapp.api.v1.crud.product.router import product_router
from webapp.api.v1.crud.user.router import user_router
from webapp.integrations.start_up_redis import start_redis
from webapp.load_data import load_data
from webapp.migrate import migrate


def setup_routers(app: FastAPI) -> None:
    routers = [user_router, product_router, cart_router, auth_router]
    for router in routers:
        app.include_router(router)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await migrate()
    await load_data(['fixture/shop/shop.user.json'])
    await start_redis()

    yield

    return


def create_app() -> FastAPI:
    app = FastAPI(docs_url='/swagger', lifespan=lifespan)
    setup_routers(app)
    return app
