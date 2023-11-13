import time
import random

class Microservice1:
    def communicate_with_1_and_3(self):
        try:
            start_time = time.time()
            response_from_1 = self.get_data_from_microservice1()
            end_time = time.time()
            print(f"Microserviciul #1 a primit un răspuns de la Microserviciul #1: {response_from_1}")
            print(f"Timpul de răspuns al Microserviciului #1: {end_time - start_time:.4f} sec")

            start_time = time.time()
            response_from_3 = self.get_data_from_microservice3()
            end_time = time.time()
            print(f"Microserviciul #1 a primit un răspuns de la Microserviciul #3: {response_from_3}")
            print(f"Timpul de răspuns al Microserviciului #3: {end_time - start_time:.4f} sec")
        except MicroserviceError as e:
            print(f"Microserviciul #1 a întâmpinat o eroare în comunicarea cu unul dintre Microserviciile #1 sau #3: {e}")

    def get_data_from_microservice1(self):
        time.sleep(random.uniform(0.1, 0.5))
        return "Date de la Microserviciul #1"

    def get_data_from_microservice3(self):
        # Simulare: Obținerea datelor de la Microserviciul #3 cu întârziere
        time.sleep(random.uniform(0.3, 1.0))
        return "Date de la Microserviciul #3"

class Microservice2:
    def communicate_with_3_and_4(self):
        try:
            start_time = time.time()
            response_from_3 = self.get_data_from_microservice3()
            end_time = time.time()
            print(f"Microserviciul #2 a primit un răspuns de la Microserviciul #3: {response_from_3}")
            print(f"Timpul de răspuns al Microserviciului #3 în Microserviciul #2: {end_time - start_time:.4f} sec")

            start_time = time.time()
            response_from_4 = self.get_data_from_microservice4()
            end_time = time.time()
            print(f"Microserviciul #2 a primit un răspuns de la Microserviciul #4: {response_from_4}")
            print(f"Timpul de răspuns al Microserviciului #4 în Microserviciul #2: {end_time - start_time:.4f} sec")
        except MicroserviceError as e:
            print(f"Microserviciul #2 a întâmpinat o eroare în comunicarea cu unul dintre Microserviciile #3 sau #4: {e}")

    def get_data_from_microservice3(self):
        time.sleep(random.uniform(0.3, 1.0))
        return "Date de la Microserviciul #3"

    def get_data_from_microservice4(self):
        time.sleep(random.uniform(0.2, 0.7))
        return "Date de la Microserviciul #4"

class Microservice3:
    def get_data(self):
        time.sleep(random.uniform(0.3, 1.0))
        return "Date de la Microserviciul #3"

class Microservice4:
    def communicate_with_3(self):
        try:
            start_time = time.time()
            response_from_3 = self.get_data_from_microservice3()
            end_time = time.time()
            print(f"Microserviciul #4 a primit un răspuns de la Microserviciul #3: {response_from_3}")
            print(f"Timpul de răspuns al Microserviciului #3 în Microserviciul #4: {end_time - start_time:.4f} sec")
        except MicroserviceError as e:
            print(f"Microserviciul #4 a întâmpinat o eroare în comunicarea cu Microserviciul #3: {e}")

    def get_data_from_microservice3(self):
        time.sleep(random.uniform(0.3, 1.0))
        return "Date de la Microserviciul #3"

class MicroserviceError(Exception):
    pass

microservice1 = Microservice1()
microservice2 = Microservice2()
microservice4 = Microservice4()

microservice1.communicate_with_1_and_3()
microservice2.communicate_with_3_and_4()
microservice4.communicate_with_3()
