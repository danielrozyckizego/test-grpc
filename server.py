import asyncio

import grpc
from concurrent import futures
import time

import greeter_pb2
import greeter_pb2_grpc
import sentry_sdk
from sentry_sdk.integrations.grpc import GRPCIntegration


class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(message=f"Hello, {request.name}!")

async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("gRPC server started on port 50051.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    sentry_sdk.init(
        traces_sample_rate=1.0,
        integrations=[GRPCIntegration()],
        debug=True,
    )
    asyncio.run(serve())
