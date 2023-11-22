import asyncio
import json

from app.conf.db import async_session, engine
from app.models.field import Field, metadata


async def main():
    async_session.configure(bind=engine)
    metadata.bind = engine
    async with async_session() as session:
        with open('scripts/fr-subset.geojsons') as f:
            objects_to_add = []
            for index, line in enumerate(f):
                line = json.loads(line)
                prop = line['properties']

                obj = Field(
                    id=prop['id'],
                    crop=prop['crop'],
                    productivity=prop['productivity'],
                    area_ha=float(prop['area_ha']),
                    history=prop['history'],
                    region=prop['region'],
                    score=prop['score'],
                    coordinates=json.dumps(line['geometry']),
                )
                objects_to_add.append(obj)
                if index == 200:
                    break
            session.add_all(objects_to_add)
            await session.commit()

if __name__ == '__main__':
    asyncio.run(main())
