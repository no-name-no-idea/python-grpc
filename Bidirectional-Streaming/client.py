import grpc
import logging
import time
import csv
import numpy as np
import random

import stream_pb2
import stream_pb2_grpc

def generate_messages():
    data = []
    while 1:
        data.append(random.randrange(1,10))
        if len(data) >= random.randrange(1,10):
            request = stream_pb2.StreamReq(q=data)    
            time.sleep(1)
            yield request
            data = []
        
        
def main() -> None:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = stream_pb2_grpc.StreamServiceStub(channel)
        for request in stub.StreamFunc(generate_messages()):
            print("Request\n----------")
            print(request)
            
            
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()