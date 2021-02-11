import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline


def linear_fit(X,y,dtheta_r):
    model = linear_model.LinearRegression()
    model.fit(X,y)
    y_pred = model.predict(X)
    sqr_err = mean_squared_error(y,y_pred)
    abs_err = mean_absolute_error(y,y_pred)
    abs_err_ar = np.abs(y-y_pred)
    std_err = np.std(abs_err_ar)
    fla = fla_predict(dtheta_r,y,y_pred)
    return model, y_pred, sqr_err, abs_err, abs_err_ar, std_err, model.coef_, model.intercept_, fla


def poly_fit(X,y,dtheta_r):
    model = Pipeline([('poly', PolynomialFeatures(degree=2)),
                      ('linear', LinearRegression())])
    model = model.fit(X,y)
    coef = model.named_steps['linear'].coef_
    intercept = model.named_steps['linear'].intercept_
    y_pred = model.predict(X)
    sqr_err = mean_squared_error(y,y_pred)
    abs_err = mean_absolute_error(y,y_pred)
    abs_err_ar = np.abs(y-y_pred)
    std_err = np.std(abs_err_ar)
    fla = fla_predict(dtheta_r,y,y_pred)
    return model, y_pred, sqr_err, abs_err, abs_err_ar, std_err, coef, intercept, fla