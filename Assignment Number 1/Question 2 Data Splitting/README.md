
# Question
2. Data Splitting:
   - Split the Iris dataset into training and testing sets using an 80-20 split.
   - Print the number of samples in both the training and testing sets.




## Solution
Data splitting is a critical step in machine learning, where the dataset is divided into two parts: a training set and a testing set. This division allows a model to be trained on one subset of the data and then evaluated on another, helping to assess the model's performance on unseen data.

In this context, the Iris dataset, a well-known dataset in machine learning, is used to demonstrate the process. The Iris dataset consists of 150 samples of iris flowers, with 50 samples for each of the three species: Iris setosa, Iris versicolor, and Iris virginica. Each sample includes four features: sepal length, sepal width, petal length, and petal width, which are used to predict the species of the iris flower.

The goal is to split this dataset into training and testing sets using an 80-20 split. This means that 80% of the data (120 samples) will be used for training the model, while the remaining 20% (30 samples) will be reserved for testing the model's performance.

To achieve this, the `train_test_split` function from the `scikit-learn` library is used. This function shuffles the dataset and then divides it according to the specified ratio. The `random_state` parameter ensures that the data is split in a reproducible way, meaning the same split will be generated each time the code is run.

Once the split is done, the number of samples in both the training and testing sets is printed. This confirms that the dataset has been properly divided, with 120 samples allocated for training and 30 for testing. This step is crucial as it prepares the dataset for the subsequent phases of model training and evaluation, ensuring that the model's performance is rigorously tested on data it has not seen before.
## Here is the algorithm to split the Iris dataset into training and testing sets using an 80-20 split, followed by printing the number of samples in each set:



1. **Install Required Library (if not already installed):**
   - Ensure that `scikit-learn` is installed using the command: `pip install scikit-learn`.

2. **Import the Required Libraries:**
   - Import the `train_test_split` function from `sklearn.model_selection`.
   - Import the Iris dataset using `load_iris` from `sklearn.datasets`.

3. **Load the Iris Dataset:**
   - Load the dataset into variables:
     - `X`: for the features (sepal length, sepal width, petal length, petal width).
     - `y`: for the target labels (Iris species).

4. **Split the Dataset into Training and Testing Sets:**
   - Use `train_test_split` to divide the dataset:
     - Set `test_size=0.2` to allocate 20% of the data for testing.
     - Use `random_state=42` to ensure reproducibility of the split.

5. **Store the Results:**
   - Store the training data in `X_train` and `y_train`.
   - Store the testing data in `X_test` and `y_test`.

6. **Print the Number of Samples in Each Set:**
   - Print the length of `X_train` to show the number of training samples.
   - Print the length of `X_test` to show the number of testing samples.


## Certainly! Below is the code to split the Iris dataset into training and testing sets using an 80-20 split, along with step-by-step explanations.

### Step 1: Install the Necessary Library
First, ensure that you have `scikit-learn` installed. If it's not installed, you can install it using the following command:
```bash
pip install scikit-learn
```

### Step 2: Import Required Libraries
Next, import the necessary functions from `scikit-learn`:
```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
```
- **`train_test_split`**: This function will help split the dataset into training and testing sets.
- **`load_iris`**: This function loads the Iris dataset, which is a classic dataset for classification tasks.

### Step 3: Load the Iris Dataset
Load the Iris dataset and separate it into features (`X`) and target labels (`y`):
```python
iris = load_iris()
X = iris.data  # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Labels: Species of Iris (Setosa, Versicolor, Virginica)
```
- **`X`** contains the features that will be used to train the model.
- **`y`** contains the corresponding labels that the model will predict.

### Step 4: Split the Dataset into Training and Testing Sets
Use `train_test_split` to split the dataset:
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
- **`test_size=0.2`**: Specifies that 20% of the data should be used as the testing set, while 80% will be used for training.
- **`random_state=42`**: Ensures that the split is reproducible, meaning the same split will occur each time the code is run.

### Step 5: Print the Number of Samples in Training and Testing Sets
Finally, print the number of samples in each set to confirm the split:
```python
print("Number of samples in the training set:", len(X_train))
print("Number of samples in the testing set:", len(X_test))
```
- **`len(X_train)`** and **`len(X_test)`** give the number of samples in the training and testing sets, respectively.

### Full Code Example
```python
# Step 1: Install Necessary Libraries
# pip install scikit-learn

# Step 2: Import Required Libraries
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Step 3: Load the Iris Dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Step 4: Split the Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Print the Number of Samples in Training and Testing Sets
print("Number of samples in the training set:", len(X_train))
print("Number of samples in the testing set:", len(X_test))
```

### Expected Output
When you run the code, it should output:
```
Number of samples in the training set: 120
Number of samples in the testing set: 30
```

This output confirms that the Iris dataset has been successfully split into 120 training samples and 30 testing samples, maintaining the 80-20 split.

## Explanation of the Code:
1).Install Necessary Libraries:

 You can install scikit-learn using the command pip install scikit-learn. This library provides tools for data preprocessing, model selection, and evaluation.

2).Importing Required Libraries:

  train_test_split: This function is used to split the dataset into training and testing sets.
  load_iris: This function loads the Iris dataset, which is a popular dataset for classification tasks.

3).Loading the Iris Dataset:

  The Iris dataset is loaded into variables X (features) and y (labels).
4).Splitting the Dataset:

  The dataset is split into training and testing sets using the train_test_split function.
     test_size=0.2: This means that 20% of the dataset is used for testing, and 80% is used for training.
     random_state=42: This is a seed for the random number generator, ensuring that the results are reproducible.

5).Printing the Number of Samples:

  The code prints the number of samples in both the training and testing sets to confirm the correct split.
# Hi, I'm Aniruddha Singh! 👋


## 🚀 About Me
I'm 2nd Year Student..

