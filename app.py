import streamlit as st
from prophet import Prophet
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Tesla Stock Forecasting", page_icon=":chart_with_upwards_trend:", layout="centered")

df = pd.read_csv('TESLA.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)

df['Price_Range'] = df['High'] - df['Low']
df['Price_Change'] = df['Close'] - df['Open']

st.markdown(
    """
    <style>
    body {
        background-color: #181818;
        color: white;
        font-family: 'Roboto', sans-serif;
    }
    .css-1d391kg {
        color: #ff3333;
    }
    .css-1v0mbdj {
        color: #ffffff;
    }
    .stButton>button {
        background-color: #ff3333;
        color: white;
        font-weight: bold;
        border-radius: 4px;
        transition: background-color 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #cc2929;
    }
    .stTextInput input {
        background-color: #303030;
        color: white;
    }
    .stSlider>div>div>input {
        background-color: #303030;
        color: white;
    }
    .stMetric>div>div>div {
        background-color: #333333;
        color: white;
    }
    .stSelectbox select {
        background-color: #303030;
        color: white;
    }
    .stDataFrame table {
        font-size: 14px;
    }
    .stDataFrame tbody tr:hover {
        background-color: #444444;
    }
    </style>
    """, unsafe_allow_html=True
)

st.sidebar.image('tesla.png')

mode = st.sidebar.radio('Select Theme', ['Dark', 'Light'])

if mode == 'Light':
    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff;
            color: black;
        }
        .stButton>button {
            background-color: #1e1e1e;
            color: white;
        }
        .stTextInput input {
            background-color: #f1f1f1;
            color: black;
        }
        .stSlider>div>div>input {
            background-color: #f1f1f1;
            color: black;
        }
        .stMetric>div>div>div {
            background-color: #e0e0e0;
            color: black;
        }
        .stSelectbox select {
            background-color: #f1f1f1;
            color: black;
        }
        </style>
        """, unsafe_allow_html=True
    )

st.title('Tesla Stock Forecasting')
st.markdown('---')

column_to_forecast = st.sidebar.selectbox('Select Column for Forecasting:',
                                          ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Price_Range', 'Price_Change'])

growth_period = st.sidebar.radio('Select Growth Period:', ['Weekly', 'Monthly', 'Yearly'])

forecast_timeframe = st.sidebar.selectbox('Select Forecasting Period:', ['Weekly', 'Monthly', 'Yearly'])

fixed_periods = st.sidebar.number_input('Select Forecast Period (in days):', min_value=1, value=1000, step=1)

selected_date = st.sidebar.date_input("Select Date", pd.to_datetime("2025-12-01"))

df1 = df[['Date', column_to_forecast]].copy()
df1.columns = ['ds', 'y']
df1['ds'] = pd.to_datetime(df1['ds'], format='%m/%d/%y')

m = Prophet(weekly_seasonality=True, yearly_seasonality=True, daily_seasonality=False)

m.fit(df1)

future = m.make_future_dataframe(periods=fixed_periods, freq='D')

forecast = m.predict(future)

st.subheader(f'Forecast for {column_to_forecast} with {forecast_timeframe} period')

forecast_tail = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
forecast_tail['ds'] = forecast_tail['ds'].dt.strftime('%Y-%m-%d')

st.markdown("### Latest Forecast Results")

fig = go.Figure()

fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast', line=dict(color='red')))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', name='Lower Bound', line=dict(color='blue', dash='dash')))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', name='Upper Bound', line=dict(color='blue', dash='dash')))

fig.update_layout(title=f'{column_to_forecast} Forecast with Confidence Intervals',
                  xaxis_title='Date', yaxis_title=f'{column_to_forecast}', template='plotly_dark')

st.plotly_chart(fig)

st.subheader(f'{column_to_forecast} Growth Analysis')

forecast['trend_cumsum'] = forecast['trend'].cumsum()
forecast['weekly_cumsum'] = forecast['weekly'].cumsum()
forecast['yearly_cumsum'] = forecast['yearly'].cumsum()
forecast['monthly_cumsum'] = forecast['weekly_cumsum'] * 4

selected_date = pd.to_datetime(selected_date)
forecast['ds'] = pd.to_datetime(forecast['ds'], format='%Y-%m-%d')

if selected_date < forecast['ds'].min() or selected_date > forecast['ds'].max():
    st.warning(f"Selected date {selected_date.date()} is outside the forecast range.")
else:
    selected_forecast = forecast[forecast['ds'].dt.date == selected_date.date()]
    st.info(f"Selected Forecast Data for {selected_date.date()}:")
    st.dataframe(selected_forecast)

    if not selected_forecast.empty:
        if growth_period == 'Weekly':
            growth_value = selected_forecast['weekly_cumsum'].values[0]
            st.metric(label="Weekly Cumulative Growth", value=f"{growth_value:.2f}", delta=f"{growth_value:.2f}")

        elif growth_period == 'Monthly':
            growth_value = selected_forecast['monthly_cumsum'].values[0]
            st.metric(label="Monthly Cumulative Growth", value=f"{growth_value:.2f}", delta=f"{growth_value:.2f}")

        elif growth_period == 'Yearly':
            growth_value = selected_forecast['yearly_cumsum'].values[0]
            st.metric(label="Yearly Cumulative Growth", value=f"{growth_value:.2f}", delta=f"{growth_value:.2f}")
    else:
        st.error(f"No forecast data available for the selected date: {selected_date}")
