from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import numpy as np
import pandas as pd


def LinearRegressionReport(X_train_converted, X_test_converted, y_train, y_test):
    cv_num = []
    mean_of_rmse_train = []
    std_of_rmse_train = []
    rmse_test_ls = []
    rmse_train_test_gap = []
    
    
    
    
    for i in range(2,11):
        # train
        lr = LinearRegression()
        scores_train = cross_val_score(lr, X_train_converted, y_train,
                                       scoring='neg_mean_squared_error', cv=i)
        lr_rmse_scores_train = np.sqrt(-scores_train)        
        # test
        lr = LinearRegression()
        lr.fit(X_train_converted, y_train)
        y_pred = lr.predict(X_test_converted)
        rmse_test = np.sqrt(mean_squared_error(y_test, y_pred))

        
        cv_num.append(i)
        mean_of_rmse_train.append(np.round(lr_rmse_scores_train.mean(), 6))
        std_of_rmse_train.append(np.round(lr_rmse_scores_train.std(), 6))
        rmse_test_ls.append(np.round(rmse_test, 6))
        rmse_train_test_gap.append(np.round(abs(lr_rmse_scores_train.mean() - rmse_test), 6))
        
        
    result = pd.DataFrame({
        "cv_num": cv_num, "mean_of_rmse_train": mean_of_rmse_train, 
        "std_of_rmse_train": std_of_rmse_train, "rmse_test": rmse_test_ls,
        "rmse_train_test_gap": rmse_train_test_gap,
    })
    return result