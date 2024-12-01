import os
from utils.data_loader import load_journal_data, preprocess_entries
from utils.sentiment_analysis import analyze_sentiment, summarize_sentiments
from utils.recommendation_utils import generate_feedback

def main():
    data_path = os.path.join("data", "journal_entries.json")

    print("Loading journal data...")
    data = load_journal_data(data_path)
    entries = preprocess_entries(data)

    print("Performing sentiment analysis...")
    sentiment_results = analyze_sentiment(entries)
    summary = summarize_sentiments(sentiment_results)

    print("Generating feedback...")
    feedback = generate_feedback(summary)

    # Display results
    print("\nSentiment Analysis Results:")
    for result in sentiment_results:
        print(f"Date: {result['date']}, Sentiment: {result['sentiment']}, Entry: {result['entry']}")

    print("\nSentiment Summary:")
    print(f"Positive: {summary['positive_percent']:.2f}%, Negative: {summary['negative_percent']:.2f}%, Neutral: {summary['neutral_percent']:.2f}%")

    print("\nFeedback:")
    print(feedback)

if __name__ == "__main__":
    main()
