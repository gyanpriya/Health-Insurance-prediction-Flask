#best_model.py
from model_evaluation import evaluate_model

def choose_best_model(models, X_test, y_test):
    best_model = None
    best_score = float('inf')
    best_model_name = ""
    metrics = {}

    for name, model in models.items():
        mae, rmse, r2, adjusted_r2 = evaluate_model(model, X_test, y_test)
        metrics[name] = {'MAE': mae, 'RMSE': rmse, 'R2': r2, 'Adjusted R2': adjusted_r2}

        if rmse < best_score:
            best_score = rmse
            best_model = model
            best_model_name = name

    return best_model, best_model_name, metrics
