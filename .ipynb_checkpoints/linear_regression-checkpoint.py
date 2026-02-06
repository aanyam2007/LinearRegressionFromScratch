{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "796441a7-7380-425d-a51d-d965f4800a7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "501e1e1a-09a5-405c-9ce8-2bcd2dada8b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2afc996f-0f74-4a9f-aae2-e4112e360a68",
   "metadata": {},
   "outputs": [],
   "source": [
    "class LinearRegression:\n",
    "    def __init__(self,lr=0.001,iter=1000):\n",
    "        self.lr=lr\n",
    "        self.iter=iter\n",
    "        self.w=None\n",
    "        self.b=None\n",
    "\n",
    "    def fit(self,x,y):\n",
    "        samples,features=x.shape\n",
    "\n",
    "        # initialize parameters\n",
    "        self.w=np.zeros(features)\n",
    "        self.b=0\n",
    "\n",
    "        #gradient descent\n",
    "        for i in range(self.iters):\n",
    "            y_pred=np.dot(x, self.w)+self.b\n",
    "\n",
    "            # gradients\n",
    "            dw=(1/samples)*np.dot(x.T,(y_pred-y))\n",
    "            db=(1/samples)*np.sum(y_pred-y)\n",
    "\n",
    "            # update parameters\n",
    "            self.w-=self.lr*dw\n",
    "            self.b-=self.lr*db\n",
    "\n",
    "    def predict(self,x):\n",
    "        return np.dot(x,self.w)+self.b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9bceafeb-167a-4a22-97f6-c8051f61980a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
