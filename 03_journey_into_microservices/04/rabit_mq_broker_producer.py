import pika


class Broker:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='broker', exchange_type='direct')

    def send_request(self, request, routing_key):
        self.channel.basic_publish(exchange='broker',
                                   routing_key=routing_key,
                                   body=request)
        print(f"Brokerul a trimis o cerere: '{request}' cu cheia de rutare: '{routing_key}'")

    def close_connection(self):
        self.connection.close()


broker = Broker()
broker.send_request("Cerere de la Broker", "microserviciu1")
broker.close_connection()
