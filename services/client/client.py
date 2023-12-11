"""This module contains the client code for the MNIST service"""

import asyncio
import logging
import os
import grpc
from proto import mnist_pb2_grpc
from proto import mnist_pb2

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

MNIST_SERVER_URL = os.environ.get("MNIST_SERVER_URL", "localhost:50051")


def handle_response(response: mnist_pb2.Sample) -> None:
    """This function handles the response from the server"""
    logger.info("MNIST client received: %s", str(response.label))


async def run() -> None:
    """This is the main function that runs the client""" 
    async with grpc.aio.insecure_channel(MNIST_SERVER_URL) as channel:
        stub = mnist_pb2_grpc.MnistServiceStub(channel)
        try:
            async for response in stub.GetTrainingSamples(mnist_pb2.DataRequest()):
                handle_response(response)
        except grpc.aio.AioRpcError as e:
            logger.error(e)

if __name__ == "__main__":
    try:
        logging.basicConfig()
        asyncio.run(run())
    except KeyboardInterrupt:
        pass
