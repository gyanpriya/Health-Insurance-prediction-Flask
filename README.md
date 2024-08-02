# Insurance Cost Prediction Project with Flask

This project aims to predict insurance costs using machine learning models and visualize the results using Flask and Tableau.

## Files and Folders

- **DATA**: Contains dataset files in `.xlsx` and `.csv` formats.
- **Notebook**: Contains `Insurance_cost_EDA.ipynb` which includes basic EDA of the dataset and visualization.
- **Tableau dashboards**: Contains snippets of Tableau dashboards.
- **Templates**: Contains `index.html` for the Flask app.
- **Other Files**:
  - `best_model.pkl`: Pickle file containing the best trained model.
  - `best_model.py`: Python script for loading and using the best model.
  - `data_load_eda.py`: Script for data loading and exploratory data analysis.
  - `feature_engineering.py`: Script for feature engineering.
  - `flaskapp.py`: Main Flask application script.
  - `hypothesis_testing.py`: Script for performing hypothesis testing.
  - `LICENSE.txt`: License file for the project.
  - `main.py`: Main script for running the project.
  - `model_evaluation.py`: Script for model evaluation.
  - `model_training.py`: Script for model training.
  - `pre_processing.py`: Script for data pre-processing.
  - `README.md`: This README file.
  - `requirements.txt`: List of dependencies required for the project.

## Problem Statement

The goal of this project is to predict the insurance costs for individuals based on various features such as age, Height, Weight, Diabetes, Blood Pressure problems, Any Allergies, Any Tranplants done, Any chronic disease and number of surgeries.
Accurately predicting insurance costs can help insurance companies to price their policies more effectively and enable customers to get better insights into their insurance costs.

## Steps Taken to Solve the Problem

### 1. Exploratory Data Analysis (EDA)

- **Data Loading:** Loaded the dataset from `.csv` files in the `DATA` folder.
- **Data Cleaning:** Handled missing values, outliers, and incorrect data types.
- **Visualization:** Used various plots and charts to understand the distribution of features and their relationships with the target variable (insurance cost).

### 2. Hypothesis Testing

- **Feature Relationships:** Conducted hypothesis tests to determine the statistical significance of the relationships between features and the target variable.
- **Correlation Analysis:** Analyzed correlations to identify important features for the prediction model.

### 3. Machine Learning Modeling

- **Pre-processing:** Applied data pre-processing steps including scaling, encoding categorical variables, and feature engineering.
- **Model Training:** Trained multiple models including Linear Regression, Random Forest, and Gradient Boosting.
- **Model Evaluation:** Evaluated models using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared. Selected the best model based on performance metrics.

### Target Metric and Scores

The primary target metric for this project is the Mean Absolute Error (MAE), as it provides a straightforward interpretation of the average error in the predicted insurance costs.


### 4. Deployment

- **Flask App:** Developed a Flask application (`flaskapp.py`) to serve the model and provide an interface for users to input their data and get predictions.
- **Web Interface:** Created an HTML template (`index.html`) for the web interface.
- **Model Integration:** Integrated the trained model (`best_model.pkl`) into the Flask app for real-time predictions.

## Installation

To set up the project, install the necessary packages using pip:

```bash
pip install -r requirements.txt
```

## Running the Flask App
Navigate to the directory containing flaskapp.py:

```bash
cd path/to/your/project
```

### Run the Flask app:

```bash
python flaskapp.py
```

Open your web browser and go to the address provided by Flask (usually http://localhost:5000) to interact with the application.

## Using the Models
The trained models are saved as pickle files (best_model.pkl). These can be loaded in your Python scripts to make predictions on new data.

## Tableau Dashboards
The Tableau dashboard snippets are stored in the Tableau dashboards folder. Please refer to the Tableau links:


- **`Statistics Summary Dashboard`**: https://public.tableau.com/app/profile/gyanpriya.misra/viz/Stats_Dashboard/StatisticsSummaryDashboard
- **`Premium Price Analysis`**: https://public.tableau.com/app/profile/gyanpriya.misra/viz/PremiumPrice_17215660938630/PremiumPriceAnalysis
- **`Risk Factor Analysis`**: https://public.tableau.com/app/profile/gyanpriya.misra/viz/PremiumCost/RiskFactorAnalysis

LICENSE
This project is licensed under the MIT License - see the LICENSE.txt file for details.