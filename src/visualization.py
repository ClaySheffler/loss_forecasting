import matplotlib.pyplot as plt

def plot_forecast(actual, forecast, title="Forecast vs Actual"):
    plt.figure(figsize=(10, 5))
    plt.plot(actual, label='Actual')
    plt.plot(forecast, label='Forecast', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.show()