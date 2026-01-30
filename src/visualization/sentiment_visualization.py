import matplotlib.pyplot as plt
import seaborn as sns


def plot_sentiment_returns_scatter(
    df,
    sentiment_col='sentiment',
    returns_col='daily_return',
    title='Sentiment vs Daily Returns'
):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=sentiment_col,
        y=returns_col,
        data=df
    )
    plt.title(title)
    plt.xlabel("Sentiment Score")
    plt.ylabel("Daily Returns")
    plt.show()
def plot_sentiment_returns_time_series(df, title=None):
    plt.figure(figsize=(12, 6))
    
    plt.plot(df['date'], df['sentiment'], label='Sentiment', color='blue')
    plt.plot(df['date'], df['returns'], label='Returns', color='green')

    if title:
        plt.title(title)

    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)

def plot_sentiment_returns_time_series(df):
    fig, ax1 = plt.subplots()

    ax1.plot(df['date'], df['sentiment'], color='blue')
    ax1.set_ylabel('Sentiment')

    ax2 = ax1.twinx()
    ax2.plot(df['date'], df['daily_return'], color='red')
    ax2.set_ylabel('Daily Return')

    plt.title("Sentiment & Returns Over Time")
    plt.show()


def plot_lagged_correlations(df, max_lag=5):
    correlations = []
    lags = range(-max_lag, max_lag + 1)

    for lag in lags:
        correlations.append(
            df['sentiment'].corr(df['daily_return'].shift(lag))
        )

    sns.barplot(x=list(lags), y=correlations)
    plt.title("Lagged Correlations")
    plt.show()


def plot_sentiment_distribution(
    df,
    sentiment_col='sentiment',
    title='Sentiment Distribution'
):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[sentiment_col], kde=True)
    plt.title(title)
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()