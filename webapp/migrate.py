from webapp.integrations.postgres import engine
from webapp.models import meta


async def migrate() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(meta.metadata.create_all)
