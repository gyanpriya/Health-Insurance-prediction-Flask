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