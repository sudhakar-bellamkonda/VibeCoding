from typing import List, Set

class User:
    """
    Represents a user and the accounts they have interacted with.
    Optimized for performance and memory usage.
    """
    __slots__ = ["user_id", "username", "accounts"]

    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username
        self.accounts: Set[str] = set()

    def add_account(self, account_id: str) -> None:
        """Add an account to the user's set of touched accounts."""
        self.accounts.add(account_id)

    def get_accounts(self) -> List[str]:
        """Return a list of unique accounts the user has touched."""
        return list(self.accounts)

    def account_count(self) -> int:
        """Return the number of unique accounts the user has touched."""
        return len(self.accounts)

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, username={self.username!r}, accounts={list(self.accounts)!r})"