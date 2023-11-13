SERVICE1_URL = "http://localhost:5001"
SERVICE2_URL = "http://localhost:5002"
SERVICE3_URL = "http://localhost:5003"
SERVICE4_URL = "http://localhost:5004"


def service1():
    print("Microserviciul 1: Inițiere proces")


def service2():
    print("Microserviciul 2: Realizare parte a procesului")


def service3():
    print("Microserviciul 3: Realizare parte a procesului (posibilă eroare)")
    raise Exception("Eroare în microserviciul 3")


def service4():
    print("Microserviciul 4: Finalizare proces")


if __name__ == "__main__":
    try:
        service1()
        service2()
        try:
            service3()
        except Exception as e:
            print(f"Microserviciul 3 a eșuat cu eroare: {str(e)}")
        service4()

    except KeyboardInterrupt:
        print("Procesul a fost întrerupt manual.")

