"""This module represents the MNIST Streaming server"""

import os
from concurrent import futures
import logging
import signal
import grpc
import grpc.experimental

from proto import mnist_pb2_grpc
from service import Mnist

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

PORT = os.environ.get("PORT", "50051")


def serve() -> grpc.Server:
    """This function starts the server"""
    try:
        server_instance = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        mnist_pb2_grpc.add_MnistServiceServicer_to_server(Mnist(), server_instance)
        logger.info("Starting MNIST Service in port %s", PORT)
        server_instance.add_insecure_port("[::]:" + PORT)
        server_instance.start()
        server_instance.wait_for_termination()
        return server_instance
    except grpc.aio.AioRpcError as e:
        logger.error(e)
        return None


if __name__ == "__main__":
    try:
        logging.basicConfig()
        server = serve()
        signal.signal(signal.SIGINT, lambda s, f: server.stop(0))
    except KeyboardInterrupt:
        pass
