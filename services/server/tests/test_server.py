import pytest
import sys
import grpc
import os 

sys.path.append('../server')

from proto import mnist_pb2
from proto import mnist_pb2_grpc
from server import Mnist
import grpc_testing

from concurrent import futures

port = os.environ.get("PORT", "50051")

@pytest.fixture(scope='module')
def grpc_add_to_server():
    return mnist_pb2_grpc.add_MnistServiceServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from server import Mnist

    return Mnist()


@pytest.fixture(scope='module')
def grpc_stub(grpc_channel):
    return mnist_pb2_grpc.MnistServiceStub(grpc_channel)


def test_server_streaming(grpc_stub):
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mnist_pb2_grpc.add_MnistServiceServicer_to_server(Mnist(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()

    # Create a gRPC channel to the server
    channel = grpc.insecure_channel('localhost:' + port)

    # Create a gRPC stub using the channel
    stub = mnist_pb2_grpc.MnistServiceStub(channel)

    # Call the server-side streaming RPC using the stub
    responses = stub.GetTrainingSamples(mnist_pb2.DataRequest())

    # Check the received messages
    for response in responses:
        # Check label is number between 0 and 9
        assert response.label == int(response.label) and response.label >= 0 and response.label <= 9
        
        # check image is 28x28
        assert len(response.image) == 28*28

    server.stop(0)