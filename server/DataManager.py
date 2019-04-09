from sync.data_manager import DataManager
import logging
import asyncio
from .taskmanager import TaskManager

logger = logging.getLogger(__name__)


class ServerDataManager(DataManager):
    def __init__(self, ws):
        super().__init__(ws)
        self.taskmanager = TaskManager

    async def watch_layers(self):
        while True:
            logger.debug("Scanning layer images...")
            for uuid, image in self.images.items():
                image.update()

            await asyncio.sleep(2)

    async def recv_recompute(self, uuid):
        logger.debug("Scheduling recompute for {}".format(uuid))
        image = self.images[uuid]
        self.taskmanager.schedule_compute(image, image.slots)