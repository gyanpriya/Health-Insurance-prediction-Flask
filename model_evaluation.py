#model_evaluation.py
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

def evaluate_model(model, X_test, y_test):
    n = len(y_test)
    p = X_test.shape[1]
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    return mae, rmse, r2, adjusted_r2