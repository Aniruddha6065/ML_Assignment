
# Question

3. Linear Regression:
   - Use a dataset with the features YearsExperience and Salary.
   - Fit a linear regression model to predict Salary based on YearsExperience.
   - Evaluate the model's performance using Mean Squared Error (MSE) on the test set.



## Solution
Linear Regression is a fundamental statistical method used to model the relationship between a dependent variable (in this case, `Salary`) and one or more independent variables (here, `YearsExperience`). The goal is to predict `Salary` based on the number of years of experience.

To start, we need a dataset containing two columns: `YearsExperience` and `Salary`. First, we load this dataset and then split it into training and testing sets. The training set, usually 80% of the data, is used to build the model, while the test set, the remaining 20%, is reserved for evaluating the model's performance on unseen data.

The linear regression model is then fitted to the training data, finding the best-fitting line that minimizes the error between the predicted and actual salaries. This line is characterized by two parameters: the intercept (where the line crosses the y-axis) and the coefficient (the slope of the line), which represents the change in salary for each additional year of experience.

Once the model is trained, we use it to predict salaries on the test set. The predictions are then compared to the actual salaries in the test set to evaluate the model's performance. One common evaluation metric is the Mean Squared Error (MSE), which measures the average squared difference between the predicted and actual values. A lower MSE indicates a better fit, meaning the model's predictions are closer to the actual values.

## Here's the algorithm to perform linear regression to predict `Salary` based on `YearsExperience`, and to evaluate the model's performance using Mean Squared Error (MSE):

1. **Load the Dataset**:
   - Import the dataset that contains the features `YearsExperience` and `Salary`.

2. **Split the Dataset**:
   - Separate the dataset into features (`X`) and target variable (`y`).
   - Split the data into a training set (typically 80%) and a testing set (20%) using a method like `train_test_split`.

3. **Initialize the Linear Regression Model**:
   - Create an instance of the `LinearRegression` model from the `scikit-learn` library.

4. **Fit the Model**:
   - Train the linear regression model using the training set (`X_train` and `y_train`).

5. **Make Predictions**:
   - Use the trained model to predict `Salary` values for the test set (`X_test`).

6. **Calculate Mean Squared Error (MSE)**:
   - Compare the predicted salaries with the actual salaries in the test set.
   - Compute the Mean Squared Error (MSE) to evaluate the model's accuracy.

7. **Interpret Results**:
   - Analyze the MSE value and the plot to assess the model's performance and accuracy in predicting salaries based on years of experience.