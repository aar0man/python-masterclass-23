import pika


class Mediator:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='cereri')
        self.channel.queue_declare(queue='raspunsuri')

    def process_requests(self):
        def callback(ch, method, properties, body):
            request = body.decode('utf-8')
            print(f"Mediatorul a primit o cerere: '{request}'")

            response = self.process_request(request)

            self.channel.basic_publish(exchange='',
                                       routing_key='raspunsuri',
                                       body=response)
            print(f"Mediatorul a trimis un răspuns: '{response}'")

        self.channel.basic_consume(queue='cereri',
                                   on_message_callback=callback,
                                   auto_ack=True)

        print("Mediatorul așteaptă cereri. Apăsați CTRL+C pentru a opri.")
        self.channel.start_consuming()

    def process_request(self, request):
        if request == "Cerere de la Microserviciul #1":
            return "Răspuns la cerere pentru Microserviciul #1"
        else:
            return "Cerere necunoscută"


mediator = Mediator()
mediator.process_requests()
