import pytest
import numpy as np
import pandas as pd
import xgboost as xgb

from ml.model import train_model, compute_model_metrics
from ml.data import process_data

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed

@pytest.fixture
def dummy_data():
    """
    # Numerical Dummy Data to test the prediction shape and if the classifier model is instantiating properly
    """
    X = np.random.rand(10, 5)
    y = np.random.randint(0, 2, 10)
    return X, y
    
@pytest.fixture
def trained_model(dummy_data):
    """
    # Training the dummy_data
    """
    X, y = dummy_data
    return train_model(X, y)

    
@pytest.fixture
def mock_data():
    """
    Utilized Udacity's AI in order to create mock data to test the pipeline
    """
    data = {
        'age': [25, 30, 45, 35, 50],
        'workclass': ['Private', 'Self-emp', 'Private', 'Government', 'Self-emp'],
        'education': ['Bachelors', 'Masters', 'Bachelors', 'HS-grad', 'Masters'],
        'marital-status': ['Single', 'Married', 'Married', 'Single', 'Divorced'],
        'occupation': ['Tech-support', 'Exec-managerial', 'Tech-support', 'Sales', 'Prof-specialty'],
        'relationship': ['Not-in-family', 'Husband', 'Husband', 'Not-in-family', 'Unmarried'],
        'race': ['White', 'Black', 'White', 'White', 'Black'],
        'sex': ['Female', 'Male', 'Male', 'Female', 'Female'],
        'capital-gain': [0, 2000, 0, 1500, 3000],
        'capital-loss': [0, 0, 0, 0, 0],
        'hours-per-week': [40, 50, 60, 30, 45],
        'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'United-States'],
        'salary': ['<=50K', '>50K', '>50K', '<=50K', '>50K']
    }
    return pd.DataFrame(data)

    
def test_trained_model_returns_correct_ml_model(trained_model):
    """
    # Ensuring that model.py's train_model function returns the correct machine learning model of XGBClassifer  
    """
    assert isinstance(trained_model, xgb.XGBClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_predictions_shape(dummy_data, trained_model):
    """
    # Ensuring that model makes predictions without crashing the system and that the predictions are of the correct shape
    """
    X, _ = dummy_data
    preds = trained_model.predict(X)
    assert preds.shape == (10,)


# TODO: implement the third test. Change the function name and input as needed
def test_process_datas_data_type_and_shape(mock_data):
    """
    # Ensuring that both the x and y data subsets are of type numpy array and that they have the correct shape. 
    """
    cat_features = ["workclass", "education", "marital-status", "occupation", "race", "sex", "native-country"]
    

    X, y, encoder, lb = process_data(
        mock_data, 
        categorical_features = cat_features,
        label = "salary",
        training = True
    )

    assert isinstance(X, np.ndarray), "X should be a numpy array"
    assert isinstance(y, np.ndarray), "y should be a numpy array"

    assert X.shape[0] == mock_data.shape[0], "X row count mismatch"
    assert y.shape[0] == mock_data.shape[0], "y row count mismatch"

