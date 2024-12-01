from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(entries):
    """Perform sentiment analysis on journal entries."""
    analyzer = SentimentIntensityAnalyzer()
    results = []

    for entry in entries:
        scores = analyzer.polarity_scores(entry["entry"])
        sentiment = (
            "positive" if scores["compound"] >= 0.05 else
            "negative" if scores["compound"] <= -0.05 else
            "neutral"
        )
        results.append({
            "date": entry["date"],
            "entry": entry["entry"],
            "sentiment": sentiment,
            "scores": scores
        })

    return results

def summarize_sentiments(results):
    """Summarize sentiments across entries."""
    total_entries = len(results)
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
    
    for result in results:
        sentiment_counts[result["sentiment"]] += 1
    
    summary = {
        "positive_percent": (sentiment_counts["positive"] / total_entries) * 100,
        "negative_percent": (sentiment_counts["negative"] / total_entries) * 100,
        "neutral_percent": (sentiment_counts["neutral"] / total_entries) * 100
    }
    return summary
