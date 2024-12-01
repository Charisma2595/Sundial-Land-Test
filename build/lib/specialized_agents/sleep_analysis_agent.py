from utils.data_loader import load_sleep_data
from utils.model_loader import train_time_series_model
from utils.recommendation_utils import analyze_sleep_patterns_arima, generate_sleep_suggestions_arima

def main():
    file_path = "data/sleep_data.csv"
    data = load_sleep_data(file_path)

    user_data = data[data["user_id"] == 1]
    model = train_time_series_model(user_data)

    analysis = analyze_sleep_patterns_arima(model, user_data)

    # Generate suggestions
    suggestions = generate_sleep_suggestions_arima(analysis)

    print("Sleep Analysis Agent Results:")
    print({
        "analysis": analysis,
        "suggestions": suggestions,
    })

if __name__ == "__main__":
    main()
