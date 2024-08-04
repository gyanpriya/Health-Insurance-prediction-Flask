from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

# Initialize the Random Forest Regressor
rf = RandomForestRegressor()

# Initialize the Gradient Boosting Regressor
gb = GradientBoostingRegressor()

# Define the parameter grid for Random Forest
param_grid_rf = {
    'n_estimators': [100, 200, 300, 400, 500],
    'max_depth': [None, 10, 20, 30, 40, 50],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

param_grid_gb = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

def optimize_model(X_train, y_train, X_test, y_test):
    # Randomized Search for Random Forest
    random_search_rf = RandomizedSearchCV(estimator=rf, param_distributions=param_grid_rf, n_iter=50, cv=5, scoring='neg_mean_absolute_error', n_jobs=-1, verbose=2, random_state=42)
    random_search_rf.fit(X_train, y_train)

    print("Best parameters for Random Forest (Randomized Search):", random_search_rf.best_params_)
    best_rf_random = random_search_rf.best_estimator_

    # Evaluate the model
    y_pred_rf_random = best_rf_random.predict(X_test)
    print("Random Forest (Randomized Search) - MAE:", mean_absolute_error(y_test, y_pred_rf_random))
    print("Random Forest (Randomized Search) - RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_rf_random)))
    print("Random Forest (Randomized Search) - R2 Score:", r2_score(y_test, y_pred_rf_random))

    # Randomized Search for Gradient Boosting
    random_search_gb = RandomizedSearchCV(estimator=gb, param_distributions=param_grid_gb, n_iter=50, cv=5, scoring='neg_mean_absolute_error', n_jobs=-1, verbose=2, random_state=42)
    random_search_gb.fit(X_train, y_train)

    print("Best parameters for Gradient Boosting (Randomized Search):", random_search_gb.best_params_)
    best_gb_random = random_search_gb.best_estimator_

    # Evaluate the model
    y_pred_gb_random = best_gb_random.predict(X_test)
    print("Gradient Boosting (Randomized Search) - MAE:", mean_absolute_error(y_test, y_pred_gb_random))
    print("Gradient Boosting (Randomized Search) - RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_gb_random)))
    print("Gradient Boosting (Randomized Search) - R2 Score:", r2_score(y_test, y_pred_gb_random))
