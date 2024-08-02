from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd

def process_data(df, cat_features, num_features, target):
    # Separate features and target
    X = df.drop(columns=[target])
    y = df[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Preprocessing for numerical features 
    num_transformer = Pipeline(steps=[('scaler', StandardScaler())])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(transformers=[('num', num_transformer, num_features),('cat', 'passthrough', cat_features)])

    # Preprocess the training data
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # Convert to DataFrame for better readability (optional)
    X_train_df = pd.DataFrame(X_train, columns=num_features + cat_features)
    X_test_df = pd.DataFrame(X_test, columns=num_features + cat_features)

    return X_train_df, X_test_df, y_train, y_test