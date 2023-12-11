# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import mnist_pb2 as mnist__pb2


class MnistServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTrainingSamples = channel.unary_stream(
                '/MnistService/GetTrainingSamples',
                request_serializer=mnist__pb2.DataRequest.SerializeToString,
                response_deserializer=mnist__pb2.Sample.FromString,
                )


class MnistServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTrainingSamples(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MnistServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTrainingSamples': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTrainingSamples,
                    request_deserializer=mnist__pb2.DataRequest.FromString,
                    response_serializer=mnist__pb2.Sample.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MnistService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MnistService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTrainingSamples(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/MnistService/GetTrainingSamples',
            mnist__pb2.DataRequest.SerializeToString,
            mnist__pb2.Sample.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
