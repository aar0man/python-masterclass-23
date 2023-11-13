import random

import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)


def should_fail():
    return random.random() < 0.5


@breaker
def call_external_service():
    if should_fail():
        raise pybreaker.CircuitBreakerError("Solicitatea a eșuat.")
    return "Răspuns de la serviciul extern."

try:
    result = call_external_service()
    print(result)
except pybreaker.CircuitBreakerError as e:
    print(f"Eroare de Circuit Breaker: {e}")
