
# Dataset Exploration: Iris Dataset

In this task, we begin by exploring the Iris dataset, a classic dataset in machine learning and statistics, often used for testing algorithms and understanding basic data analysis. The dataset contains 150 samples of iris flowers, categorized into three species: Iris-setosa, Iris-versicolor, and Iris-virginica. Each sample includes four features: sepal length, sepal width, petal length, and petal width.


## Question
1. Dataset Exploration:
   - Load the Iris dataset from sklearn.datasets.
   - Display the first five rows, the dataset’s shape, and summary statistics (mean, standard deviation, min/max values) for each feature.





## Solution
1. Loading the Iris Dataset:

We load the dataset using the load_iris function from the sklearn.datasets module. This function provides the data in the form of a Bunch object, which is similar to a dictionary and contains the features, target labels, and a description of the dataset.

2. Displaying the First Five Rows:

After loading the dataset, we extract the feature matrix and convert it into a pandas DataFrame for easier manipulation and visualization. We then display the first five rows of this DataFrame, providing a snapshot of the dataset. This step helps us to understand the structure and format of the data, as well as the ranges of the feature values.

3. Dataset Shape:

Next, we examine the shape of the dataset using the .shape attribute. This reveals the number of samples (rows) and features (columns) present in the dataset, providing an initial sense of the dataset's dimensionality.

4. Summary Statistics:

Finally, we compute and display summary statistics for each feature in the dataset. These statistics include the mean, standard deviation, minimum, and maximum values. The mean gives us an idea of the central tendency of the data, while the standard deviation indicates the spread of the feature values. The minimum and maximum values help identify the range of each feature. These statistics are essential for understanding the distribution and variability of the data, which can inform decisions about data preprocessing and model selection in subsequent steps.



