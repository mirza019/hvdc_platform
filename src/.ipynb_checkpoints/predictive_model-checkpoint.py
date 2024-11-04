# predictive_model.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

def train_model(data):
    X = data[['voltage', 'current']]
    y = data['fault']  # Target: 1 if fault, 0 if normal

    # Split and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Test the model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    return model

# Assume historical data with a fault column
data = pd.DataFrame({
    'voltage': np.random.normal(500, 10, 1000),
    'current': np.random.normal(1.5, 0.1, 1000),
    'fault': np.random.choice([0, 1], 1000)
})
model = train_model(data)
