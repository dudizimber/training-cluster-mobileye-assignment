
from data_generator import MNISTGenerator
from proto import mnist_pb2_grpc
from proto import mnist_pb2
import logging
logger = logging.getLogger(__name__)

class Mnist(mnist_pb2_grpc.MnistService):
    def GetTrainingSamples(
        self, request, context
    ):
        logger.info("GetTrainingSamples")
        generator = MNISTGenerator()
        try:
            for sample in generator:
                yield mnist_pb2.Sample(image=bytes(sample.image), label=sample.label)
        except Exception as e:
            logger.error(e)
            pass