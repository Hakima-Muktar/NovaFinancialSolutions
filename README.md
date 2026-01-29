# Predicting Price Moves with News Sentiment
Analyze the relationship between financial news sentiment and stock price movements to provide actionable insights for Nova Financial Solutions.
## Table of Contents
- project Overview 
- Business Objective 
- Dataset Overview
- Folder Structure
- Setup & Installation
- Tasks Completed
- Requirements
- Key Insights

# Project Overview
This project covers end-to-end analysis of financial news and stock prices:

- Exploratory Data Analysis (EDA) of news headlines, publishers, and publishing times
- Sentiment analysis of news headlines
- Technical indicators computation using TA-Lib and PyNance
- Correlation analysis between sentiment scores and stock price movements
- Development workflow using Git branches and CI/CD
  
# Business Objectives 
Nova Financial Solutions aims to strengthen predictive analytics by combining qualitative news sentiment with quantitative stock metrics.
The project focuses on:
- Measuring sentiment in financial news
- Linking sentiment to stock returns
- Highlighting actionable signals for investment strategies
# Dataset Overview
Financial News and Stock Price Integration Dataset (FNSPID):

![tabe of stock](images/pppp.png>)

 Stock Price Dataset:
- Open, High, Low, Close (OHLC)
- Volume
- Daily returns
# Folder Structure
![folder Structure](<images/structure.png>)
## Clone the repository:
git clone https://github.com/Hakima-Muktar/NovaFinancialSolutions.git
- cd NovaFinancialSolution

## Create a Python virtual environment and activate it:
python -m venv venv
## Activate (Windows)
venv\Scripts\activate
# Tasks Completed
## Task 1: Git & Environment Setup
- Repository initialized with branches and CI workflow
- Python virtual environment created
- Exploratory Data Analysis (EDA) of news headlines, publishers, and publishing times
## Task 2: Technical Indicators & Market Analysis
- Stock price data cleaned and prepared
- Technical indicators computed (SMA, EMA, RSI, MACD)
- Visualizations for trends and volume
## Task 3: Sentiment vs Stock Movement Correlation
- Sentiment scores generated from news headlines
- Daily stock returns calculated
- Pearson correlation analysis between sentiment and returns
- Visualizations for patterns and regression
## Requirements
- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn
- TA-Lib, PyNance
- NLTK, TextBlob
- Jupyter Notebook
- Git & GitHub Actions
## Key Insights
- Negative news sentiment often precedes short-term price drops
- Certain publishers have strong positive or negative bias
- Sentiment combined with technical indicators improves predictive power
- Publishing spikes align with major financial events
