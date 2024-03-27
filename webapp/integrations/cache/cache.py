from typing import Any, List

import orjson
from pydantic import parse_obj_as

from conf.config import settings
from webapp.integrations.cache.key_builder import get_cache_key
from webapp.integrations.cache.redis import get_redis
from webapp.schema.shop.cart import CartItem


async def redis_set(user_id: int, payload: Any) -> None:
    redis = get_redis()

    redis_key = await get_cache_key(user_id)
    await redis.set(redis_key, orjson.dumps(payload))
    await redis.expire(redis_key, settings.FILE_EXPIRE_TIME)


async def redis_set_products(user_id: int, payload: Any) -> None:
    redis = get_redis()

    redis_key = await get_cache_key(user_id)
    await redis.set(redis_key, orjson.dumps([i.dict() for i in parse_obj_as(List[CartItem], payload)]))
    await redis.expire(redis_key, settings.FILE_EXPIRE_TIME)


async def redis_get(user_id: int) -> dict[str, str]:
    redis = get_redis()
    redis_key = await get_cache_key(user_id)
    cache = await redis.get(redis_key)
    if cache is None:
        return {}
    return orjson.loads(cache)


async def redis_drop_key(user_id: int) -> None:
    redis = get_redis()
    redis_key = await get_cache_key(user_id)
    await redis.delete(redis_key)
