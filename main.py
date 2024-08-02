from data_load_eda import load_data
from feature_engineering import calculate_bmi
from pre_processing import process_data
from model_training import LR_model,RF_model,DT_model,SV_model,GB_model,XGB_model
from best_model import choose_best_model
import pickle



# load data
file_path = "C:\Insurance cost prediction project\DATA\insurance.csv"
df = load_data(file_path)

# add feature bmi
df = calculate_bmi(df)

# Define the categorical features
cat_features = ['Diabetes', 'BloodPressureProblems', 'AnyTransplants', 'AnyChronicDiseases','KnownAllergies', 'HistoryOfCancerInFamily']

# Define the numerical features
num_features = ['Age', 'Height', 'Weight', 'NumberOfMajorSurgeries']

# Define the target variable
target = 'PremiumPrice'

# Split and process data
X_train, X_test, y_train, y_test = process_data(df, cat_features, num_features, target)

# Train models
models = {
    "Linear Regression": LR_model(X_train, y_train),
    "Random Forest Regression": RF_model(X_train, y_train),
    "Decision Tree Regression": DT_model(X_train, y_train),
    "Support Vector Regression": SV_model(X_train, y_train),
    "Gradient Boosting Regression": GB_model(X_train, y_train),
    "XGBoost Regression": XGB_model(X_train, y_train)
}

# Choose best model
best_model, best_model_name, metrics = choose_best_model(models, X_test, y_test)

print(f"Best Model: {best_model_name}")
print("Metrics:")
for name, metric in metrics.items():
    print(f"{name}:")
    print(f"  MAE: {metric['MAE']}")
    print(f"  RMSE: {metric['RMSE']}")
    print(f"  R2: {metric['R2']}")
    print(f"  Adjusted R2: {metric['Adjusted R2']}")
    print("-" * 40)

# Save the best model to a pickle file
with open('best_model.pkl', 'wb') as f:
    pickle.dump(best_model, f)