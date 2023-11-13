import pika


class Microservice1:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='cereri')

    def send_request(self, request):
        self.channel.basic_publish(exchange='',
                                   routing_key='cereri',
                                   body=request)
        print(f"Microserviciul #1 a trimis o cerere: '{request}'")

    def close_connection(self):
        self.connection.close()


microservice1 = Microservice1()
microservice1.send_request("Cerere de la Microserviciul #1")
microservice1.close_connection()
