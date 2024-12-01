import pandas as pd
import numpy as np

def generate_synthetic_sleep_data(output_path="data/sleep_data.csv"):
    """
    Generate synthetic sleep data for multiple users.
    """
    np.random.seed(42)  
    user_ids = [1, 2, 3]
    dates = pd.date_range(start="2024-11-01", end="2024-11-30", freq="D")
    
    data = []
    for user_id in user_ids:
        for date in dates:
            sleep_duration = np.random.normal(loc=7, scale=1.5)  
            sleep_duration = max(4, min(sleep_duration, 10))  
            disturbances = np.random.poisson(lam=2)  
            data.append([user_id, date, sleep_duration, disturbances])
    
    df = pd.DataFrame(data, columns=["user_id", "date", "sleep_duration", "disturbances"])
    df.to_csv(output_path, index=False)
    print(f"Synthetic sleep data saved to {output_path}")

if __name__ == "__main__":
    generate_synthetic_sleep_data()
