import grpc
import logging
from concurrent.futures import ThreadPoolExecutor

import stream_pb2
import stream_pb2_grpc

class StreamService(stream_pb2_grpc.StreamServiceServicer) :
    
    def StreamFunc(self, request_iterator, context):
        for request in  request_iterator:
            print("Received\n----------")
            print(request)
            response =  stream_pb2.StreamRes(s=request.q)
            yield response

def serve(address: str) -> None:
    server = grpc.server(ThreadPoolExecutor())
    stream_pb2_grpc.add_StreamServiceServicer_to_server(
        StreamService(), server)
    server.add_insecure_port(address)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve('[::]:50051')