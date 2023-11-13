import random
import time


def perform_operation():
    if random.randint(1, 10) <= 5:
        raise Exception("Operațiunea a eșuat.")
    return "Operațiune reușită."


max_retries = 3

for attempt in range(max_retries):
    try:
        result = perform_operation()
        print(result)
        break
    except Exception as e:
        print(f"Eroare: {e}")
        if attempt < max_retries - 1:
            print("Reîncercare în 2 secunde...")
            time.sleep(2)
