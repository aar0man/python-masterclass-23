import pika


class Microservice2:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='raspunsuri')

    def receive_responses(self):
        def callback(ch, method, properties, body):
            response = body.decode('utf-8')
            print(f"Microserviciul #2 a primit un răspuns: '{response}'")

        self.channel.basic_consume(queue='raspunsuri',
                                   on_message_callback=callback,
                                   auto_ack=True)

        print("Microserviciul #2 așteaptă răspunsuri. Apăsați CTRL+C pentru a opri.")
        self.channel.start_consuming()


microservice2 = Microservice2()
microservice2.receive_responses()
