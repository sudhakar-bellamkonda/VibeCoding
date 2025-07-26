from collections import defaultdict
from typing import Dict, Set, List
import time
import pandas as pd
from typing import Optional

class Tracker:
    """
    Tracks user interactions with accounts and computes performance metrics.
    """
    def __init__(self):
        self.user_interactions: Dict[str, Set[str]] = defaultdict(set)

    def track_user_interaction(self, user_id: str, account_id: str) -> None:
        """Record that a user has interacted with an account."""
        self.user_interactions[user_id].add(account_id)

    def get_user_performance(self, user_id: str) -> int:
        """Return the number of unique accounts a user has touched."""
        return len(self.user_interactions.get(user_id, set()))

# Expanded sample data for demonstration
sample_data: List[Dict[str, str]] = [
    {"user": "Alice", "account": "A001"},
    {"user": "Bob", "account": "A002"},
    {"user": "Alice", "account": "A003"},
    {"user": "Bob", "account": "A001"},
    {"user": "Alice", "account": "A002"},
    {"user": "Charlie", "account": "A004"},
    {"user": "Charlie", "account": "A005"},
    {"user": "Charlie", "account": "A001"},
    {"user": "Diana", "account": "A002"},
    {"user": "Diana", "account": "A003"},
    {"user": "Diana", "account": "A004"},
    {"user": "Eve", "account": "A005"},
    {"user": "Eve", "account": "A001"},
    {"user": "Eve", "account": "A002"},
    {"user": "Eve", "account": "A003"},
]

def summarize_user_performance(data: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Given a list of user-account interactions, return a dict mapping each user
    to the number of unique accounts they have touched.
    """
    performance: Dict[str, Set[str]] = defaultdict(set)
    for entry in data:
        performance[entry["user"]].add(entry["account"])
    return {user: len(accounts) for user, accounts in performance.items()}

def old_user_performance(data: List[Dict[str, str]]) -> Dict[str, int]:
    performance = {}
    for entry in data:
        user = entry["user"]
        account = entry["account"]
        if user not in performance:
            performance[user] = set()
        performance[user].add(account)
    return {user: len(accounts) for user, accounts in performance.items()}

def benchmark_performance(data: List[Dict[str, str]], repeat: int = 10000):
    start = time.time()
    for _ in range(repeat):
        old_user_performance(data)
    old_time = time.time() - start

    start = time.time()
    for _ in range(repeat):
        summarize_user_performance(data)
    new_time = time.time() - start

    print(f"Old method time: {old_time:.4f} seconds for {repeat} runs")
    print(f"New method time: {new_time:.4f} seconds for {repeat} runs")
    print(f"Performance improvement: {((old_time - new_time) / old_time * 100):.2f}% faster")

def read_user_data_from_csv(csv_path: str) -> Optional[list]:
    """
    Reads user-account interaction data from a CSV file and returns a list of dicts.
    The CSV should have columns: user, account
    """
    try:
        df = pd.read_csv(csv_path)
        # Ensure required columns exist
        if 'user' in df.columns and 'account' in df.columns:
            return df[['user', 'account']].to_dict(orient='records')
        else:
            print("CSV must contain 'user' and 'account' columns.")
            return None
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None