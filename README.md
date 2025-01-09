
# Tesla Stock Forecasting 💹

Tesla Stock Forecasting is an interactive web application built with Streamlit, enabling users to analyze and forecast Tesla's stock performance. The app uses the Prophet library for time series forecasting and offers dynamic visualizations through Plotly.  

## Features  

### **Interactive Data Exploration**  
- Visualize Tesla's historical stock data, including derived metrics like **Price Range** (High - Low) and **Price Change** (Close - Open).  
- Access interactive charts to better understand trends and historical patterns.  

### **Custom Forecasting**  
- Choose any stock column (e.g., Open, High, Low, Close, Volume) for detailed forecasting.  
- Forecast for customizable timeframes: weekly, monthly, yearly.  

### **Dynamic Growth Analysis**  
- Analyze cumulative growth for weekly, monthly, or yearly trends.  
- Specify a custom date to view detailed growth metrics.  

### **User-Centric Design**  
- Toggle between **Dark Mode** and **Light Mode** for a personalized experience.  
- Sidebar-based controls for seamless configuration.  

### **Advanced Visualizations**  
- Plot forecasted values, confidence intervals, and growth metrics using **Plotly**.  
- Interactive charts with hover capabilities to enhance data comprehension.  

## Installation  

### Prerequisites  
Ensure Python 3.8+ is installed on your system.  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/Akshat-Sharma-110011/Tesla-Stock-Forecasting  
   cd tesla-stock-forecasting  
   ```  

2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the application**:  
   ```bash  
   streamlit run app.py  
   ```  

## Usage  

1. **Upload Tesla Stock Data**  
   - Prepare a Tesla stock dataset (e.g., `TESLA.csv`) with the necessary columns: Date, Open, High, Low, Close, Volume, etc.  

2. **Configure Forecast Settings**  
   - Select the column for forecasting: Open, High, Low, Close, Volume, or derived metrics (Price Range, Price Change).  
   - Choose a forecast period (e.g., Weekly, Monthly, Yearly).  
   - Define the forecast duration (e.g., 1000 days).  
   - Specify a date for cumulative growth analysis.  

3. **View Results**  
   - Explore interactive charts showing forecasted values, confidence intervals, and growth metrics.  
   - Analyze detailed growth for your selected period (weekly, monthly, or yearly).  

## Technical Details  

### **Libraries and Tools**  
- **Prophet**: Time series forecasting with customizable seasonality.  
- **Pandas**: Data manipulation and preprocessing.  
- **Plotly**: Interactive visualizations for charts and trends.  
- **Streamlit**: Web application framework for data visualization.  

### **Data Preparation**  
- Derives metrics:  
  - **Price Range**: High - Low.  
  - **Price Change**: Close - Open.  
- Ensures proper formatting of date fields for compatibility with Prophet.  

### **Forecasting Approach**  
- Utilizes Prophet for forecasting with weekly and yearly seasonality enabled.  
- Calculates cumulative growth trends for weekly, monthly, and yearly components.  

### **UI Enhancements**  
- Custom styling for both dark and light themes using Streamlit's HTML injection.  
- Interactive sidebar controls for theme selection, forecasting period, and analysis parameters.  

## Notes  

- Ensure the Tesla stock dataset (`TESLA.csv`) is correctly formatted before using the application.  
- Use a virtual environment to avoid dependency conflicts while installing required packages.  

## Contribution  

We welcome contributions to improve the application. Follow these steps:  
1. Fork the repository.  
2. Create a feature branch.  
3. Submit a pull request with your changes.  

## License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 

## Website

Link: [(https://tesla-stock-forecasting.onrender.com/)]

---

For questions or support, contact [akshatsharma.work.1310@gmail.com].  
