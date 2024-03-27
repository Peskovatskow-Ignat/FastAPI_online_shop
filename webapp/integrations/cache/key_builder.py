from conf.config import settings


async def get_cache_key(user_id: int) -> str:
    return f'{settings.REDIS_SIRIUS_CACHE_PREFIX}:{user_id}'
