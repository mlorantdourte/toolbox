from sklearn.linear_model import LinearRegression
def linear_regression(X,y):
    lr=LinearRegression()
    lr.fit(X,y)
    return lr.score(X,y)