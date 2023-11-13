import pika


class Microservice2:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='broker', exchange_type='direct')
        self.channel.queue_declare(queue='microserviciu2')
        self.channel.queue_bind(exchange='broker', queue='microserviciu2', routing_key='microserviciu2')

    def receive_request(self):
        def callback(ch, method, properties, body):
            request = body.decode('utf-8')
            print(f"Microserviciul #2 a primit o cerere: '{request}'")

        self.channel.basic_consume(queue='microserviciu2',
                                   on_message_callback=callback,
                                   auto_ack=True)

        print("Microserviciul #2 așteaptă cereri. Apăsați CTRL+C pentru a opri.")
        self.channel.start_consuming()


microservice2 = Microservice2()
microservice2.receive_request()
