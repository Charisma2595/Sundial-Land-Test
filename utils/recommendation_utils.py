import pandas as pd

def generate_fitness_suggestions(model, user_data):
    """
    Generate fitness suggestions based on user data and a regression model.
    """
    prediction = model.predict(user_data[["week"]])
    target = prediction.mean() * 1.1  
    
    suggestion = f"Your predicted average steps are {prediction.mean():.0f}. " \
                 f"Try to aim for {target:.0f} steps next week to improve your fitness."
    
    return {
        "current_trend": prediction.tolist(),
        "suggestion": suggestion
    }


def analyze_sleep_patterns_arima(model, user_data: pd.DataFrame):
    """
    Analyze sleep patterns using a trained ARIMA model and historical data.
    """
    forecast = model.forecast(steps=7)

    avg_sleep_duration = user_data["sleep_duration"].mean()
    avg_disturbances = user_data["disturbances"].mean()

    poor_sleep_detected = avg_sleep_duration < 6

    return {
        "current_trend": forecast.tolist(),
        "average_sleep_duration": avg_sleep_duration,
        "average_disturbances": avg_disturbances,
        "poor_sleep_detected": poor_sleep_detected,
    }

def generate_sleep_suggestions_arima(analysis: dict):
    """
    Generate suggestions based on sleep pattern analysis.
    """
    suggestions = []

    if analysis["average_sleep_duration"] < 6:
        suggestions.append("Your average sleep time is below 6 hours. Consider a consistent bedtime routine.")
    else:
        suggestions.append("Great job! Your sleep duration is above 6 hours. Keep up the good work!")

    if analysis["average_disturbances"] > 3:
        suggestions.append("You have frequent sleep disturbances. Reduce screen time before bed or try relaxation techniques.")
    else:
        suggestions.append("Well done! Your sleep disturbances are low. Keep maintaining a peaceful sleep environment!")

    if min(analysis["current_trend"]) < 6:
        suggestions.append("Your predicted sleep duration is below 6 hours. Aim for at least 7 hours nightly.")
    else:
        suggestions.append("Fantastic! Your predicted sleep duration looks good. Keep it up to maintain your health!")

    if analysis["average_sleep_duration"] > 7 and analysis["average_disturbances"] < 2:
        suggestions.append("Excellent! You're on track with your sleep. Keep up the great work for optimal health!")

    return suggestions


def generate_feedback(summary):
    """Generate emotional feedback based on sentiment summary."""
    if summary["negative_percent"] > 50:
        feedback = "Your recent journal entries reflect sadness and anxiety. Would you like some tips for managing negative emotions?"
    elif summary["positive_percent"] > 50:
        feedback = "Your recent journal entries reflect positivity and accomplishment. Keep up the great work!"
    else:
        feedback = "Your recent journal entries reflect a mix of emotions. Would you like to talk more about how you're feeling?"

    return feedback


def generate_holistic_feedback(agent_outputs, correlations):
    """
    Generate holistic feedback based on agent outputs and correlations.
    """
    feedback = {}

    # Sleep feedback
    sleep_suggestions = agent_outputs.get("sleep", {}).get("suggestions", [])
    feedback["sleep"] = " ".join(sleep_suggestions) if sleep_suggestions else "No specific sleep recommendations at this time."

    # Fitness feedback
    fitness_suggestion = agent_outputs.get("fitness", {}).get("suggestion", "No fitness recommendations at this time.")
    feedback["fitness"] = fitness_suggestion

    # Sentiment feedback
    sentiment_feedback = agent_outputs.get("sentiment", {}).get("feedback", "No sentiment-related feedback available.")
    feedback["sentiment"] = sentiment_feedback

    # Correlations feedback
    if correlations:
        feedback["correlations"] = " ".join(correlations)
    else:
        feedback["correlations"] = "No significant correlations detected between your data points."

    return feedback
