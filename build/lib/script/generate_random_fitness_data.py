import pandas as pd
import numpy as np

def generate_activity_data(num_users=10, weeks=12):
    """
    Generate synthetic activity data for users over multiple weeks.
    """
    data = []
    for user_id in range(1, num_users + 1):
        for week in range(1, weeks + 1):
            steps = np.random.randint(4000, 15000)
            calories = np.random.randint(1500, 3000)
            active_minutes = np.random.randint(30, 180)
            data.append([user_id, week, steps, calories, active_minutes])
    
    df = pd.DataFrame(data, columns=["user_id", "week", "steps", "calories", "active_minutes"])
    df.to_csv("data/activity_data.csv", index=False)
    print("Dataset saved at data/activity_data.csv.")

# Generate the dataset
generate_activity_data()
