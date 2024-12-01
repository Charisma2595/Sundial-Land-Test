import pandas as pd
from utils.data_loader import load_activity_data
from utils.model_loader import train_regression_model
from utils.recommendation_utils import generate_fitness_suggestions

def main():
    # Load data
    file_path = "data/activity_data.csv"
    data = load_activity_data(file_path)
    
    # Process data for a single user 
    user_data = data[data["user_id"] == 1]
    model = train_regression_model(user_data)
    
    suggestions = generate_fitness_suggestions(model, user_data)
    
    print("Fitness Tracking Agent Results:")
    print(suggestions)

if __name__ == "__main__":
    main()
