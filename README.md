# Industrial_Copper_Modelling

## Introduction
The copper industry deals with sales and pricing data that may suffer from issues such as skewness and noise, impacting manual prediction accuracy. Dealing with these challenges manually can be time-consuming and suboptimal for pricing decisions. Machine learning regression models offer a solution by utilizing techniques like data normalization, feature scaling, and outlier detection, leveraging algorithms robust to skewed and noisy data.

Another challenge in the copper industry is lead capture. Lead classification models evaluate and classify leads based on their likelihood to convert into customers. Providing an application for predicting selling prices and lead classification can significantly benefit such industries, improving customer experience and operational efficiency.

## Problem Statement
The project aims to build machine learning models for predicting the selling price of copper and determining its status as either "won" or "lost". The models will employ advanced techniques such as data normalization, outlier detection and handling, rectification of data in incorrect formats, examination of feature distributions, and utilization of tree-based models, particularly the decision tree algorithm, to accurately predict selling prices and status of copper product.

## Required Libraries
* Streamlit : To Create Graphical user Interface and build web application.
* Pandas : To Clean and maipulate the data.
* NumPy: A library for numerical computations in Python.
* Matplotlib: A plotting library for creating visualizations.
* Seaborn: A data visualization library built on top of Matplotlib.
* Scikit-learn: A machine learning library that provides various regression and classification algorithms & Evaluation Metrices.

## Workflow:
1) Data Understanding: Identify the types of variables (continuous, categorical) and their distributions.
2) Data Preprocessing:
   * Handle missing values with mean/median/mode.
   * Identify Skewness in the dataset and treat skewness with appropriate data transformations, such as log transformation(which is best suited to transform target variable-train, predict and then reverse transform it back to original scale) to handle high skewness in continuous variables.
   * Encode categorical variables using suitable techniques, such as one-hot encoding, label encoding, or ordinal encoding, based on their nature and relationship with the target variable.
3) EDA: Try visualizing outliers and skewness(before and after treating skewness) using Seaborn’s boxplot & histplot.
4) Feature Engineering: Engineering new features if applicable, such as aggregating or transforming existing features to create more informative representations of the data. And drop highly correlated columns using SNS HEATMAP.
5) Model Building and Evaluation:
   * Splitting the dataset into training and testing/validation sets.
   * Training and evaluating with regression & classification model of DecisionTrees, and using appropriate evaluation metrics such as MSE, R-squared for regression model & accuracy, precision, recall, F1 score, and AUC curve for classification models.
   * Optimizing model hyperparameters using techniques such as cross-validation and grid search to find the best-performing model.
   * Interpreting the model results and assess its performance based on the defined problem statement.
6) Model GUI: Using streamlit module, create interactive page with:
   * Task input( Regression or Classification) and
   * Creating an input field where you can enter each column value except ‘Selling_Price’ for regression model and  except ‘Status’ for classification model.
   * Performing the same feature engineering, scaling factors, log/any transformation steps which you used for training ML model and predicting this new data from streamlit and displaying the output.
7) Using pickle module to dump and load models such as encoder(onehot/ label/ str.cat.codes /etc), scaling models(standard scaler), ML models.

## Learning Outcomes:
* Experienced in Python and its data analysis libraries, including Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and Streamlit.
* Acquiring expertise in data preprocessing techniques, encompassing handling missing values, outlier detection, and data normalization to optimize data for machine learning modeling.
* Understanding and visualizing the data distribution using EDA techniques such as boxplots, & histograms.
* Learned advanced machine learning techniques including regression and classification for predictive modeling, alongside optimizing models through evaluation metrics, cross-validation, and grid search.
* Experienced in feature engineering techniques to create new informative representations of the data.
* Developing a web application using the Streamlit module to showcase the machine learning models and make predictions on new data.
* Understanding the challenges and best practices in the manufacturing domain and how machine learning can help solve them.

## Conclusion
The Industrial Copper Modeling project aims to predict the selling price and status in the industrial copper market using machine learning techniques
