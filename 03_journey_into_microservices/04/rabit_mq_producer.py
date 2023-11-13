import pika


class Microservice1:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='mesaje')

    def send_message(self, message):
        self.channel.basic_publish(exchange='',
                                   routing_key='mesaje',
                                   body=message)
        print(f"Microserviciul #1 a trimis un mesaj: '{message}'")

    def close_connection(self):
        self.connection.close()


microservice1 = Microservice1()
microservice1.send_message("Salut, Microserviciul #2!")
microservice1.close_connection()
