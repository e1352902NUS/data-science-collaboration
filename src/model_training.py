"""Model training utilities."""
<<<<<<< Updated upstream
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    """Train a machine learning model."""
    # Use Random Forest with specific parameters
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
=======
from sklearn.ensemble import GradientBoostingClassifier

def train_model(X_train, y_train):
    """Train a machine learning model."""
    # Use Gradient Boosting for better performance
    model = GradientBoostingClassifier(
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5,
>>>>>>> Stashed changes
        random_state=42
    )
    model.fit(X_train, y_train)
    return model