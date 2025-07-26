class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.accounts = []

    def add_account(self, account_id):
        if account_id not in self.accounts:
            self.accounts.append(account_id)

    def get_accounts(self):
        return self.accounts