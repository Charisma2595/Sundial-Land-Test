import pandas as pd
import json
import os

def load_activity_data(file_path):
    """
    Load activity data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        raise Exception(f"File not found: {e}")



def load_sleep_data(file_path: str) -> pd.DataFrame:
    """
    Load sleep data from a CSV file.
    """
    return pd.read_csv(file_path, parse_dates=["date"])




def load_journal_data(file_path):
    """Load journal data from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)

def preprocess_entries(data):
    """Extract and preprocess journal entries."""
    return [{"date": entry["date"], "entry": entry["entry"]} for entry in data["journal_entries"]]



def load_agent_output(file_path):
    """Load output data from an agent."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)

def load_all_outputs():
    """Load outputs from all agents."""
    base_path = "data/agent_outputs"
    return {
        "fitness": load_agent_output(os.path.join(base_path, "fitness_agent_output.json")),
        "sleep": load_agent_output(os.path.join(base_path, "sleep_agent_output.json")),
        "sentiment": load_agent_output(os.path.join(base_path, "sentiment_agent_output.json"))
    }
