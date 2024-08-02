#model_training.py
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor

def LR_model(X_train,y_train):
    LR_model = LinearRegression()
    LR_model.fit(X_train,y_train)
    return LR_model

def RF_model(X_train,y_train):
    RF_model = RandomForestRegressor(random_state=42)
    RF_model.fit(X_train,y_train)
    return RF_model

def DT_model(X_train,y_train):
    DT_model = DecisionTreeRegressor(random_state=42)
    DT_model.fit(X_train,y_train)
    return DT_model

def SV_model(X_train,y_train):
    SV_model = SVR()
    SV_model.fit(X_train,y_train)
    return SV_model

def GB_model(X_train,y_train):
    GB_model = GradientBoostingRegressor(random_state=42)
    GB_model.fit(X_train,y_train)
    return GB_model

def XGB_model(X_train,y_train):
    XGB_model = XGBRegressor()
    XGB_model.fit(X_train,y_train)
    return XGB_model

