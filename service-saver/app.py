from __future__ import print_function

import grpc
import products_pb2
import products_pb2_grpc
from app_saver import insert_into_table


def run():
    print("[ - ]  Will try to receive data ...")
    with grpc.insecure_channel('service-parser:50051') as channel:
        stub = products_pb2_grpc.ProductsStub(channel)
        responses = stub.SendProduct(products_pb2.SendProductRequest())
        for response in responses:
            print(f"[ √ ]  Saver client received: {response.products[0].name}")
            data = {
                'name': response.products[0].name,
                'price': response.products[0].price,
                'articul': response.products[0].articul,
                'description': response.products[0].description,
            }
            insert_into_table(data, 'Smartphones')


if __name__ == '__main__':
    run()