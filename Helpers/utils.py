import matplotlib.pyplot as plt
import seaborn as sns
def plot_histogram(data, column):
    """
    This function takes a dataframe and a numerical column name as input
    and creates a histogram of the column.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=False)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_value_counts(data, column):
    """
    This function takes a dataframe and a categorical column name as input
    and creates a bar chart of the value counts for the column.
    """
    plt.figure(figsize=(10, 6))
    value_counts = data[column].value_counts()
    sns.barplot(x=value_counts.index, y=value_counts.values)
    plt.title(f'Value Counts of {column}')
    plt.xlabel(column)
    plt.xticks(rotation=90)
    plt.ylabel('Counts')
    plt.show()