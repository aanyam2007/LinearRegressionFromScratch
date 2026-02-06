# Linear Regression From Scratch (Python)

This project implements **Linear Regression from scratch using NumPy**, without relying on machine learning libraries like `scikit-learn` for training.  
The goal is to demonstrate a clear understanding of the **mathematics, optimization, and implementation** behind linear regression.

---

## Features
- Linear Regression implemented from scratch
- Gradient Descent optimization
- Mean Squared Error (MSE) loss
- **Loss vs Iterations visualization**
- **Comparison with scikit-learn’s LinearRegression**
- Works with single-feature and multi-feature data

---

## Mathematical Formulation

### Model
\[
\hat{y} = Xw + b
\]

### Loss Function (Mean Squared Error)
\[
J(w, b) = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2
\]

### Gradients
\[
dw = \frac{1}{n} X^T(\hat{y} - y)
\]
\[
db = \frac{1}{n} \sum(\hat{y} - y)
\]

---

## Dataset
The **Student Scores dataset** is used to train and evaluate the model.

- Feature: Hours studied
- Target: Exam score
- Samples: 25
- Relationship: Approximately linear

This dataset was chosen because it clearly demonstrates how linear regression fits real-world data.

---

## Training Process
The model is trained using **batch gradient descent**.  
During training, the **Mean Squared Error loss is recorded at each iteration** to visualize convergence.

### Loss vs Iterations
A plot of training loss versus iterations shows that the loss consistently decreases, confirming that gradient descent is working correctly.

---

## Comparison with scikit-learn
To validate correctness, the learned parameters from the from-scratch implementation are compared with `sklearn.linear_model.LinearRegression`.

The weights and bias obtained from both implementations are very close, confirming that the custom implementation is mathematically correct.

---
