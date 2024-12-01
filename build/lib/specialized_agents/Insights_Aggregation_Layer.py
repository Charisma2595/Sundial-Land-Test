from utils.data_loader import load_all_outputs
from utils.correlation_analyzer import correlate_insights
from utils.recommendation_utils import generate_holistic_feedback

def main():
    print("Loading agent outputs...")
    agent_outputs = load_all_outputs()

    print("Analyzing correlations...")
    correlations = correlate_insights(agent_outputs)

    print("Generating holistic feedback...")
    feedback = generate_holistic_feedback(agent_outputs, correlations)

    # Display results
    print("\n--- Holistic Feedback ---")
    for key, value in feedback.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
