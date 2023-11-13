import time


class Microservice1:
    def send_request_to_mediator(self, mediator):
        response = mediator.process_request("Cerere de la Microserviciul #1")
        print(f"Microserviciul #1 a primit un răspuns de la mediator: {response}")


class Microservice2:
    def process_request(self, request):
        print(f"Microserviciul #2 a primit o cerere de la mediator: {request}")
        time.sleep(2)
        return "Răspuns de la Microserviciul #2"


class Microservice3:
    def process_request(self, request):
        print(f"Microserviciul #3 a primit o cerere de la mediator: {request}")
        time.sleep(1)
        return "Răspuns de la Microserviciul #3"


class Mediator:
    def __init__(self):
        self.microservice2 = Microservice2()
        self.microservice3 = Microservice3()

    def process_request(self, request):
        print(f"Mediatorul a primit o cerere: {request}")

        response_from_microservice2 = self.microservice2.process_request(request)

        response_from_microservice3 = self.microservice3.process_request(request)
        combined_response = f"\r\n\r\nRăspuns de la Microserviciul #2: {response_from_microservice2}, \r\nRăspuns de la Microserviciul #3: {response_from_microservice3}"

        return combined_response


microservice1 = Microservice1()
mediator = Mediator()

microservice1.send_request_to_mediator(mediator)
