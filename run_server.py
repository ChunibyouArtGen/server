from server.DataManager import DataManager
from sync import init_logging

import asyncio
import websockets
import logging

logger = logging.getLogger()
init_logging(level=logging.DEBUG)

data_manager = None


async def handle_message(ws, path):
    logger.info("Running handler...")
    global data_manager
    if data_manager is None:
        data_manager = DataManager(ws)
        logger.info("Server init complete")

    while True:
        logger.info("Waiting for message...")
        message = await ws.recv()
        logger.info("Got message!")
        await data_manager.channel.process_message(message)


def run_server():
    start_server = websockets.serve(handle_message, "localhost", 8765)
    logger.debug("Starting server...")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    run_server()
