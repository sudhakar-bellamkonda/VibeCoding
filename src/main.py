# Entry point of the application for tracking user performance

from performance.tracker import Tracker, sample_data, summarize_user_performance, benchmark_performance

def main():
    # Show results using sample data
    results = summarize_user_performance(sample_data)
    for user, count in results.items():
        print(f"{user} touched {count} unique accounts.")
    
    # Calculate and print average performance
    if results:
        avg = sum(results.values()) / len(results)
        print(f"Average performance (unique accounts per user): {avg:.2f}")
    else:
        print("No data to calculate average performance.")
    
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