import time


class Microservice1:
    def send_request_to_broker(self, broker):
        response = broker.process_request("Cerere de la Microserviciul #1")
        print(f"Microserviciul #1 a primit un răspuns de la broker: {response}")


class Microservice2:
    def process_request(self, request):
        print(f"Microserviciul #2 a primit o cerere de la broker: {request}")
        time.sleep(2)
        return "Răspuns de la Microserviciul #2"


class Microservice3:
    def process_request(self, request):
        print(f"Microserviciul #3 a primit o cerere de la broker: {request}")
        time.sleep(1)
        return "Răspuns de la Microserviciul #3"


# Broker
class Broker:
    def process_request(self, request):
        print(f"Brokerul a primit o cerere de la Microserviciul #1: {request}")

        microservice2 = Microservice2()
        response_from_microservice2 = microservice2.process_request(request)

        microservice3 = Microservice3()
        response_from_microservice3 = microservice3.process_request(response_from_microservice2)

        return response_from_microservice3


microservice1 = Microservice1()
broker = Broker()

microservice1.send_request_to_broker(broker)
