# Sundial Land Assesment 

## Overview

This repository contains the code for a proof-of-concept system that demonstrates the ability to process health metrics (e.g., steps, heart rate, sleep data) through independent specialized AI agents(fitness tracking, sleep analysis, journaling sentiment and insight aggregation) to generate actionable insights.


## setup Guide

1. Prerequisites
Before setting up the project, ensure you have the following installed on your system Python 3.9+

2. Clone the Repository
```bash
git clone https://link_to_this_repo
```
3. Create and activate a Virtual Environment

4. Install Dependencies
```bash
pip install -r requirements.txt  
```

## Running the Project

Use the following command to run the AI agents and UI

1. fitness tracking 
```bash
python specialized_agents/fitness_tracking_agent.py  
```
2. sleep analysis 
```bash
python specialized_agents/sleep_analysis_agent.py  
```
3. journaling sentiment 
```bash
python specialized_agents/journaling_sentiment_analysis.py
```
4. insight aggregation 
```bash
python specialized_agents/Insights_Aggregation_Layer.py
```

Use the command bellow to run the ui for display metrics.
```bash
streamlit run UI/app.py
``
