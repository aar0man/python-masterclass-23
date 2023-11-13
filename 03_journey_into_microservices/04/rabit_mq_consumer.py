import pika


class Microservice2:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='mesaje')

    def receive_messages(self):
        def callback(ch, method, properties, body):
            print(f"Microserviciul #2 a primit un mesaj: '{body}'")

        self.channel.basic_consume(queue='mesaje',
                                   on_message_callback=callback,
                                   auto_ack=True)

        print("Microserviciul #2 așteaptă mesaje. Apăsați CTRL+C pentru a opri.")
        self.channel.start_consuming()


microservice2 = Microservice2()
microservice2.receive_messages()
