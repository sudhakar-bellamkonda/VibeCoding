# Entry point of the application for tracking user performance

from performance.tracker import Tracker, sample_data, summarize_user_performance, benchmark_performance
from performance.tracker import read_user_data_from_csv

def process_and_print_summary(data, source_name: str):
    """Summarizes, prints, and calculates average user performance."""
    if not data:
        print(f"No valid data loaded from {source_name}.")
        return

    results = summarize_user_performance(data)
    print(f"\nResults from {source_name} data:")
    if not results:
        print("No performance data found to summarize.")
        return

    for user, count in results.items():
        print(f"{user} touched {count} unique accounts.")

    avg = sum(results.values()) / len(results)
    print(f"Average performance (unique accounts per user): {avg:.2f}")

def main():
    # Use 'user_data.csv' as the input data file
    csv_path = "user_data.csv"
    csv_data = read_user_data_from_csv(csv_path)
    process_and_print_summary(csv_data, "CSV")
    process_and_print_summary(sample_data, "sample")
    
    # Example usage of Tracker class
    tracker = Tracker()
    tracker.track_user_interaction("user1", "account1")
    tracker.track_user_interaction("user1", "account2")
    performance = tracker.get_user_performance("user1")
    print(f"User performance for user1: {performance}")

    # Print performance improvement
    print("\nBenchmarking performance improvement...")
    benchmark_performance(sample_data, repeat=10000)

if __name__ == "__main__":
    main()