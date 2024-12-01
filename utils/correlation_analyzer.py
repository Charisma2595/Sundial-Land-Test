def correlate_insights(agent_outputs):
    """Correlate insights across agents."""
    correlations = []

    # Sleep Data
    average_sleep_hours = agent_outputs["sleep"]["analysis"]["average_sleep_duration"]
    sleep_disturbances = agent_outputs["sleep"]["analysis"]["average_disturbances"]
    poor_sleep_detected = agent_outputs["sleep"]["analysis"]["poor_sleep_detected"]

    # Sentiment Data
    negative_sentiment_percent = float(agent_outputs["sentiment"]["sentiment_summary"]["negative"].strip("%"))

    # Fitness Data
    predicted_average_steps = agent_outputs["fitness"]["current_trend"][-1]

    # Poor Sleep and High Stress
    if average_sleep_hours < 7 and negative_sentiment_percent > 40:
        correlations.append("Reduced sleep duration combined with high negative sentiment may be affecting your overall well-being.")

    if sleep_disturbances > 1.5 and negative_sentiment_percent > 40:
        correlations.append("Frequent sleep disturbances combined with high stress may impact your mental health.")

    # Low Activity and High Stress
    if predicted_average_steps < 10000 and negative_sentiment_percent > 40:
        correlations.append("Moderate physical activity combined with high stress may be worth addressing.")

    # Poor Sleep Detected
    if poor_sleep_detected and negative_sentiment_percent > 40:
        correlations.append("Poor sleep quality combined with high stress levels may affect your productivity and mood.")

    return correlations
