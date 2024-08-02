
def calculate_bmi(df):
    df['BMI'] = df['Weight'] / (df['Height'] / 100) ** 2
    return df