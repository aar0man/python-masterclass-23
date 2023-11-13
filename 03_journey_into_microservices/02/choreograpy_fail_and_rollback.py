import random


class OrderService:
    def create_order(self, user_id, product_id):
        order_id = self.create_order_in_db(user_id, product_id)
        inventory_service.reserve_product(product_id, order_id)

        try:
            payment_service.process_payment(order_id)
            self.confirm_order(order_id)
        except PaymentFailedException:
            inventory_service.rollback_reservation(order_id)
            self.cancel_order(order_id)
            notification_service.notify_customer(order_id, "Plata a eșuat. Comanda a fost anulată.")

    def create_order_in_db(self, user_id, product_id):
        order_id = 1
        return order_id

    def cancel_order(self, order_id):
        return "Order status reverted"

    def confirm_order(self, order_id):
        notification_service.notify_customer(order_id, "Plata a fost acceptată.")


class InventoryService:
    def reserve_product(self, product_id, order_id):
        self.reserve_product_in_db(product_id, order_id)

    def rollback_reservation(self, order_id):
        self.cancel_reservation_in_db(order_id)

    def reserve_product_in_db(self, product_id, order_id):
        return True

    def cancel_reservation_in_db(self, order_id):
        return "Product status changed"


class PaymentService:
    def process_payment(self, order_id):
        if random.random() < 0.7:
            raise PaymentFailedException("Plata a eșuat.")


class NotificationService:
    def notify_customer(self, order_id, message):
        self.send_notification(order_id, message)

    def send_notification(self, order_id, message):
        return True


class PaymentFailedException(Exception):
    pass


order_service = OrderService()
inventory_service = InventoryService()
payment_service = PaymentService()
notification_service = NotificationService()

user_id = 123
product_id = 456
order_service.create_order(user_id, product_id)
