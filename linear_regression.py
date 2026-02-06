import numpy as np

class LinearRegression:
    def __init__(self,lr=0.001,iter=1000):
        self.lr=lr
        self.iter=iter
        self.w=None
        self.b=None
        self.losses = []

    def fit(self,x,y):
        samples,features=x.shape

        # initialize parameters
        self.w=np.zeros(features)
        self.b=0

        #gradient descent
        for i in range(self.iter):
            y_pred=np.dot(x, self.w)+self.b

            # MSE loss
            loss = np.mean((y_pred - y) ** 2)
            self.losses.append(loss)

            # gradients
            dw=(1/samples)*np.dot(x.T,(y_pred-y))
            db=(1/samples)*np.sum(y_pred-y)

            # update parameters
            self.w-=self.lr*dw
            self.b-=self.lr*db

    def predict(self,x):
        return np.dot(x,self.w)+self.b