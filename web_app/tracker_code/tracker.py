import asyncio
import logging
import time

from aiohttp import ClientSession

from pytile import async_login
from pytile.errors import TileError

_LOGGER = logging.getLogger(__name__)

TILE_EMAIL = "aki.nisha.55@gmail.com"
TILE_PASSWORD = "seacole55"  # noqa: S105


async def main() -> None:
    """Run."""
    logging.basicConfig(level=logging.INFO)
    async with ClientSession() as session:
        try:
            api = await async_login(TILE_EMAIL, TILE_PASSWORD, session)
            tiles = await api.async_get_tiles()
            #_LOGGER.info("Tile Count: %s", len(tiles))
            time.sleep(0)
            for tile in tiles.values():
                #_LOGGER.info("UUID: %s", tile.uuid)
                #_LOGGER.info("Name: %s", tile.name)
                #_LOGGER.info("Type: %s", tile.kind)
                _LOGGER.info("Latitude: %s", tile.latitude)
                _LOGGER.info("Longitude: %s", tile.longitude)
                _LOGGER.info("Last Timestamp: %s", tile.last_timestamp)

                #Code to save location data
                f=open('data/tracking_logs.txt','a')
                f.write(f"Latitude: {tile.latitude} \n Longitude: {tile.longitude} \n Last Timestamp:  {tile.last_timestamp}")
                f.close()

        except TileError as err:
                _LOGGER.info(err)
                asyncio.run(main())
