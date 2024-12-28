
# Tesla Stock Forecasting

Tesla Stock Forecasting is a Streamlit-based web application that uses the Prophet library for time series forecasting. 
The app allows users to explore Tesla's historical stock data, analyze trends, and predict future stock performance.

## Features

- **Data Exploration**: Visualize Tesla stock prices and derived metrics like price range and price change.
- **Custom Forecasting**: Select any stock column (e.g., Open, High, Low, Close, Volume) for forecasting.
- **Dynamic Forecast Period**: Choose the forecast duration (e.g., weekly, monthly, yearly) with customizable periods.
- **Cumulative Growth Analysis**: Analyze weekly, monthly, and yearly cumulative growth based on forecasts.
- **Dark and Light Modes**: Switch between themes for a better user experience.
- **Interactive Visualizations**: Includes dynamic charts for forecast trends and confidence intervals.

## Installation

1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/your-repo/tesla-stock-forecasting.git
   cd tesla-stock-forecasting
   ```

2. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload the Tesla stock data CSV (`TESLA.csv`) to the application.
2. Use the sidebar to configure your forecast settings:
   - Choose the column to forecast (e.g., Open, Close, Volume).
   - Select the forecast period and the number of days to predict.
   - Pick a specific date for detailed growth analysis.
3. View the forecast results, including confidence intervals, growth metrics, and cumulative trends.

## Technical Details

- **Libraries Used**:
  - `Prophet`: For time series forecasting.
  - `Plotly`: For interactive data visualizations.
  - `Pandas`: For data manipulation and preprocessing.
  - `Streamlit`: For creating the web application.

- **Data Preprocessing**:
  - Derived metrics: Price range (High - Low) and price change (Close - Open).
  - Converted dates to the required format for Prophet.

- **Forecasting**:
  - Weekly, monthly, and yearly seasonality enabled in Prophet.
  - Cumulative growth calculations for trend, weekly, and yearly components.

## Notes

- The application assumes the presence of a properly formatted Tesla stock dataset (`TESLA.csv`).
- Prophet requires a compatible environment setup. Ensure to use a virtual environment if issues arise during installation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For any queries, contact [your-email@example.com].
