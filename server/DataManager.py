from sync.data_manager import DataManager
import logging
import asyncio
logger = logging.getLogger(__name__)


class ServerDataManager(DataManager):
    async def watch_layers(self):
        while True:
            logger.debug("Scanning layer images...")
            for uuid, image in self.images.items():
                image.update()

            await asyncio.sleep(2)
