from concurrent import futures
import concurrent
import grpc
import products_pb2
import products_pb2_grpc
from app_parser import retrieve_page


class Products(products_pb2_grpc.ProductsServicer):
    def SendProduct(self, request, context):
        url = 'https://shop.kz/smartfony/'
        url_list = (f'{url}?PAGEN_1={item}' for item in range(1, 6))

        print(' - - - - parser was called - - - - ')

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for url in url_list:
                products = executor.submit(retrieve_page, url)
                for prod in products.result():
                    print(' - - - - sending - - - - ')
                    yield products_pb2.SendProductResponse(
                        products=[products_pb2.Product(
                            name=str(prod['name']), 
                            articul=str(prod['articul']), 
                            price=str(prod['price']), 
                            description=str(prod['description'])
                        )]
                    )

                
def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    products_pb2_grpc.add_ProductsServicer_to_server(Products(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

