class AccountService:
    def create_account(self, user_id, account_type):
        pass

    def get_account_balance(self, account_id):
        pass


class TransactionService:
    def initiate_transaction(self, from_account_id, to_account_id, amount):
        pass

    def get_transaction_history(self, account_id):
        pass


class ReportingService:
    def generate_balance_report(self, account_id):
        pass

    def generate_transaction_report(self, account_id):
        pass
