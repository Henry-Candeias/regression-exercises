import seaborn as sns
import matplotlib.pyplot as plt



def plot_variable_pairs(df):
    """
    Generate a pair plot for visualizing relationships between numerical variables in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing numerical variables.

    Returns:
    - None (Displays the pair plot)

    Example:
    plot_variable_pairs(df)

    This function uses Seaborn's pairplot to create scatterplots for each pair of numerical variables in the DataFrame.
    The diagonal shows the distribution of each variable, and the scatterplots show the relationships between pairs of variables.
    Additionally, a linear regression line is fit to each scatterplot to visualize trends.

    Args:
    - df (pd.DataFrame): The input DataFrame containing numerical variables.

    Returns:
    - None (Displays the pair plot)

    """
    sns.pairplot(data=df, kind='reg', corner=True)
    return plt.show()



def plot_categorical_and_continuous_vars (df, cat_col, cont_col):
    """
    Generate three different plots for visualizing the relationship between a categorical variable and a continuous variable.

    Parameters:
    - train (pd.DataFrame): The input DataFrame containing the data.
    - cat_col (str): The name of the categorical column.
    - cont_col (str): The name of the continuous column.

    Returns:
    - None (Displays the plots)

    Example:
    plot_categorical_and_continuous_vars(train, 'county', 'bedrooms')

    This function creates three different plots to visualize the relationship between a categorical variable and a continuous variable:
    1. Boxplot: Displays the distribution of the continuous variable for each category.
    2. Violinplot: Similar to a boxplot but provides additional information about the distribution.
    3. Barplot: Displays the average or aggregated value of the continuous variable for each category.

    Args:
    - train (pd.DataFrame): The input DataFrame containing the data.
    - cat_col (str): The name of the categorical column.
    - cont_col (str): The name of the continuous column.

    Returns:
    - None (Displays the plots)

    """
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
    sns.boxplot(x=cat_col, y=cont_col, data=df, ax=axes[0])
    axes[0].set_title('Boxplot')

    sns.violinplot(x=cat_col, y=cont_col, data=df, ax=axes[1])
    axes[1].set_title('Violinplot')

    sns.barplot(x=cat_col, y=cont_col, data=df, ax=axes[2])
    axes[2].set_title('Barplot')
    
    return plt.show()