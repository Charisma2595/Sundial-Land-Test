from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def train_regression_model(data):
    """
    Train a regression model to predict weekly activity trends.
    """
    X = data[["week"]]
    y = data["steps"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    print(f"Model trained. MSE: {mse:.2f}")
    return model




def train_time_series_model(user_data: pd.DataFrame):
    """
    Train a time-series model (ARIMA) to detect sleep trends.
    """
    user_data = user_data.sort_values("date")
    sleep_duration = user_data.set_index("date")["sleep_duration"]

    # Fit an ARIMA model
    model = ARIMA(sleep_duration, order=(2, 1, 2)) 
    fitted_model = model.fit()
    return fitted_model
