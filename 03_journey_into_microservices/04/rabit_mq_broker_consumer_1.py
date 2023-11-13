import pika


class Microservice1:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='broker', exchange_type='direct')
        self.channel.queue_declare(queue='microserviciu1')
        self.channel.queue_bind(exchange='broker', queue='microserviciu1', routing_key='microserviciu1')

    def receive_request(self):
        def callback(ch, method, properties, body):
            request = body.decode('utf-8')
            print(f"Microserviciul #1 a primit o cerere: '{request}'")

        self.channel.basic_consume(queue='microserviciu1',
                                   on_message_callback=callback,
                                   auto_ack=True)

        print("Microserviciul #1 așteaptă cereri. Apăsați CTRL+C pentru a opri.")
        self.channel.start_consuming()


microservice1 = Microservice1()
microservice1.receive_request()
