"""The implementation of the MNIST service"""

import logging
from data_generator import MNISTGenerator
from proto import mnist_pb2_grpc
from proto import mnist_pb2

logger = logging.getLogger(__name__)

class Mnist(mnist_pb2_grpc.MnistService):
    """This class represents the MNIST service"""

    def GetTrainingSamples(
        self, _, __
    ):
        """This function returns the MNIST training samples"""
        logger.info("GetTrainingSamples")
        generator = MNISTGenerator()
        try:
            for sample in generator:
                yield mnist_pb2.Sample(image=bytes(sample.image), label=sample.label)
        except Exception as e:
            logger.error(e)