class Microservice1:
    def communicate_with_3(self):
        try:
            response = microservice3.do_something()
            print(f"Microserviciul #1 a primit un răspuns de la Microserviciul #3: {response}")
        except MicroserviceError as e:
            print(f"Microserviciul #1 a întâmpinat o eroare de la Microserviciul #3: {e}")


class Microservice2:
    def communicate_with_3_and_4(self):
        try:
            response_from_3 = microservice3.do_something()
            print(f"Microserviciul #2 a primit un răspuns de la Microserviciul #3: {response_from_3}")

            response_from_4 = microservice4.do_something()
            print(f"Microserviciul #2 a primit un răspuns de la Microserviciul #4: {response_from_4}")
        except MicroserviceError as e:
            print(f"Microserviciul #2 a întâmpinat o eroare de la unul dintre Microserviciile #3 sau #4: {e}")


class Microservice3:
    def do_something(self):
        raise MicroserviceError("Eroare în Microserviciul #3")


class Microservice4:
    def communicate_with_3(self):
        try:
            response = microservice3.do_something()
            print(f"Microserviciul #4 a primit un răspuns de la Microserviciul #3: {response}")
        except MicroserviceError as e:
            print(f"Microserviciul #4 a întâmpinat o eroare de la Microserviciul #3: {e}")


class MicroserviceError(Exception):
    pass


microservice1 = Microservice1()
microservice2 = Microservice2()
microservice3 = Microservice3()
microservice4 = Microservice4()

microservice1.communicate_with_3()
microservice2.communicate_with_3_and_4()
microservice4.communicate_with_3()
