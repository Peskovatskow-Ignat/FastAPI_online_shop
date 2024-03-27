import json
from pathlib import Path
from typing import List

from sqlalchemy import insert

from webapp.integrations.postgres import async_session
from webapp.models.meta import metadata


async def load_data(fixtures: List[str]) -> None:
    for fixture in fixtures:
        fixture_path = Path(fixture)
        model = metadata.tables[fixture_path.stem]
        with open(fixture_path, 'r') as file:
            values = json.load(file)

        async with async_session() as session:
            await session.execute(insert(model).values(values))
            await session.commit()
