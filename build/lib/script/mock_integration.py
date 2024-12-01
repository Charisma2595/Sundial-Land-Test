import json
import os


class MockDataIntegration:
    def __init__(self, mock_data_path):
        self.mock_data_path = mock_data_path

    def load_data(self):
        try:
            print(f"Loading mock data from: {self.mock_data_path}")
            with open(self.mock_data_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Mock dataset not found at {self.mock_data_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def normalize_data(self, mock_data):
        try:
            normalized_data = {
                "user_id": mock_data["user_id"],
                "metrics": []
            }
            for metric in mock_data["metrics"]:
                # Handle missing keys 
                normalized_entry = {
                    "date": metric["date"],
                    "steps": int(metric["steps"]) if isinstance(metric["steps"], str) else metric["steps"],
                    "heart_rate": int(metric["heart_rate"]) if isinstance(metric["heart_rate"], str) else metric["heart_rate"],
                    "sleep_hours": metric.get("sleep_hours", None), 
                    "hrv": metric.get("hrv", None)
                }
                normalized_data["metrics"].append(normalized_entry)

            # Save to JSON
            output_path = os.path.join("data", "normalized_mock_data.json")
            with open(output_path, "w") as f:
                json.dump(normalized_data, f, indent=4)

            print(f"Mock data normalized and saved to {output_path}")
            return normalized_data

        except Exception as e:
            print(f"Error normalizing data: {e}")
            return None



if __name__ == "__main__":
    mock_data_path = os.path.abspath(os.path.join("data", "mock_dataset.json"))

    # Initialize and process the mock data
    integration = MockDataIntegration(mock_data_path)
    mock_data = integration.load_data()

    if mock_data:
        integration.normalize_data(mock_data)
