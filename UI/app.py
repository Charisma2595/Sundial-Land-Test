import streamlit as st
import json
import matplotlib.pyplot as plt
import os
from utils.correlation_analyzer import correlate_insights
from utils.recommendation_utils import generate_holistic_feedback


def load_agent_data():
    data_dir = 'data/agent_outputs/'

    with open(os.path.join(data_dir, 'fitness_agent_output.json')) as f:
        fitness_data = json.load(f)

    with open(os.path.join(data_dir, 'sleep_agent_output.json')) as f:
        sleep_data = json.load(f)

    with open(os.path.join(data_dir, 'sentiment_agent_output.json')) as f:
        sentiment_data = json.load(f)

    return fitness_data, sleep_data, sentiment_data

def plot_sleep_trend(sleep_trend):
    """Plot the weekly sleep trend."""
    st.subheader("Sleep Trend")
    
    if len(sleep_trend) == 0:
        st.warning("No sleep trend data available.")
        return

    plt.figure(figsize=(10, 6))
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][:len(sleep_trend)]
    plt.plot(sleep_trend, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)
    plt.title('Weekly Sleep Trend', fontsize=14)
    plt.xlabel('Day of the Week', fontsize=12)
    plt.ylabel('Sleep Hours', fontsize=12)
    plt.xticks(range(len(sleep_trend)), days, fontsize=10)
    plt.grid(True)
    st.pyplot(plt)

def plot_fitness_trend(fitness_trend):
    """Plot the weekly fitness trend (steps)."""
    st.subheader("Fitness Trend")
    
    if len(fitness_trend) == 0:
        st.warning("No fitness trend data available.")
        return

    plt.figure(figsize=(10, 6))
    num_points = len(fitness_trend)
    if num_points <= 7:
        labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][:num_points]
    else:
        labels = [f"Week {i+1}" for i in range(num_points)]

    plt.plot(fitness_trend, marker='s', color='g', linestyle='-', linewidth=2, markersize=8)
    plt.title('Weekly Fitness Trend (Steps)', fontsize=14)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Steps', fontsize=12)
    plt.xticks(range(num_points), labels, rotation=45, fontsize=8)
    plt.grid(True)
    st.pyplot(plt)

def plot_sentiment_trend(sentiment_data):
    """Plot sentiment over the past week."""
    st.subheader("Sentiment Trend")
    
    if len(sentiment_data["sentiment_analysis_results"]) == 0:
        st.warning("No sentiment trend data available.")
        return

    # Prepare sentiment data for plotting
    dates = [entry["date"] for entry in sentiment_data["sentiment_analysis_results"]]
    sentiments = [entry["sentiment"] for entry in sentiment_data["sentiment_analysis_results"]]

    sentiment_map = {'positive': 1, 'negative': -1, 'neutral': 0}
    sentiment_values = [sentiment_map[sentiment] for sentiment in sentiments]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, sentiment_values, marker='o', color='m', linestyle='-', linewidth=2, markersize=8)
    plt.title('Weekly Sentiment Trend', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sentiment Value', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)

def display_correlation_section(correlations):
    """Display detected correlations."""
    if correlations:
        st.subheader("Correlations Detected:")
        for correlation in correlations:
            st.markdown(f"- {correlation}")
    else:
        st.subheader("No Significant Correlations Detected")

def display_recommendations_section(feedback):
    """Display holistic feedback."""
    st.subheader("Holistic Feedback:")
    for key, value in feedback.items():
        st.markdown(f"**{key.capitalize()}:** {value}")

def main():
    st.title("User Insights Dashboard")

    st.info("Loading data...")
    fitness_data, sleep_data, sentiment_data = load_agent_data()

    # Combine agent data into a single dictionary
    agent_outputs = {
        "fitness": fitness_data,
        "sleep": sleep_data,
        "sentiment": sentiment_data,
    }

    
    st.subheader("User Data Overview")
    st.write("**Sleep Data**:")
    st.write(f"Average Sleep Duration: {agent_outputs['sleep']['analysis']['average_sleep_duration']:.2f} hours")
    st.write(f"Sleep Disturbances: {agent_outputs['sleep']['analysis']['average_disturbances']}")
    
    st.write("**Fitness Data**:")
    st.write(f"Predicted Average Steps: {agent_outputs['fitness']['current_trend'][-1]:.0f}")

    st.write("**Sentiment Data**:")
    sentiment_summary = agent_outputs['sentiment']['sentiment_summary']
    st.write(f"Positive Sentiment: {sentiment_summary['positive']}")
    st.write(f"Negative Sentiment: {sentiment_summary['negative']}")

    
    plot_sleep_trend(agent_outputs['sleep']['analysis']['current_trend'])

    plot_fitness_trend(agent_outputs['fitness']['current_trend'])

    plot_sentiment_trend(agent_outputs['sentiment'])


    st.info("Analyzing correlations...")
    correlations = correlate_insights(agent_outputs)
    display_correlation_section(correlations)

    st.info("Generating holistic feedback...")
    feedback = generate_holistic_feedback(agent_outputs, correlations)
    display_recommendations_section(feedback)

if __name__ == "__main__":
    main()
