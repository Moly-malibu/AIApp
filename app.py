#base
import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
from pandas.core.reshape.merge import merge
from pandas._config.config import reset_option
from pandas.core import groupby

from requests.api import options 

import numpy
import numpy as np
from re import sub

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys

import requests
from requests import get
from bs4 import BeautifulSoup

#import yfinance 
import yfinance as yf 
from yahoo_fin.stock_info import get_analysts_info
from yahoo_fin.stock_info import *
from yahoofinancials import YahooFinancials
from yahoo_fin import stock_info as si
from yahoo_fin import options as ops


#Prediction
import math
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from bs4 import BeautifulSoup
import scipy as sp
import mpld3

import keras
import tensorflow as tf
tf.compat.v1.get_default_graph()
tf.keras.models.Model()
from tensorflow import keras
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D
from tensorflow.python.keras import Model
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras import layers
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, LSTM

#visualization
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from matplotlib import style
import plotly.graph_objs as go
import plotly.express as px
style.use('ggplot')

st.markdown("<h1 style='text-align: center; color: #002967;'>Revolutionize Your Investments:</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #002967;'>AI-Driven Financial Insights</h1>", unsafe_allow_html=True)

def main():
    # Register pages
    pages = {
        "Home": Home,
        "Stock": Stock,
        "Index": Index,
        'Statement': Statement,
        'Portfolio': Portfolio,
        # "Prediction": Prediction,
        "IndustryAVG": IndustryAVG,
    }
    st.sidebar.title("Companies Analysis")
    page = st.sidebar.selectbox("Select Menu", tuple(pages.keys()))
    pages[page]()

def Home():
    def main():
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("https://media.istockphoto.com/id/1149653875/photo/creative-minimal-paper-idea-concept-white-world-with-white-background-3d-render-3d.jpg?b=1&s=612x612&w=0&k=20&c=PCVDwb6-bzRUxHkU8I5bIvkFjYFQpMuePfhcqrSK91I=");
        background-size: cover;
        }
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.write(
        """

        Your AI-Powered Financial Analyst.
        
        - ***Revolutionize Your Investing with AI***

        Harness the power of artificial intelligence to make informed investment decisions. Our app provides a comprehensive suite of tools to analyze thousands of companies and forecast future market trends.

        - ***Key Features***:

        ***Extensive Company Coverage***: Access financial data for over 8,100 companies, covering a wide range of industries and market segments.
        
        ***Advanced Chart Analysis***: Visualize stock price trends, volatility, and momentum. Compare multiple stocks side-by-side to identify potential opportunities.
        
        ***Cutting-Edge Forecasting***:  Utilize state-of-the-art machine learning algorithms, including Long Short-Term Memory (LSTM), Decision Tree Regression, and Linear Regression.
        Predict future stock prices with greater accuracy.
        
        ***Robust Portfolio Analysis***: Optimize your portfolio with advanced statistical techniques like correlation analysis, covariance matrices, and Monte Carlo simulations.
        Calculate key metrics such as expected return, volatility, and risk-adjusted returns.
        
        ***In-Depth Financial Analysis***: Delve into detailed financial statements, including income statements, balance sheets, and cash flow statements.
        Analyze financial ratios to assess a company's financial health and performance. Evaluate option pricing and risk management strategies.
        
        ***Comprehensive Company Profiles***: Gain insights into a company's historical performance, current trends, and future prospects. Discover hidden correlations and patterns in financial data using advanced statistical techniques.
        
        
        ***Why Choose Our App?***

        - ***AI-Powered Precision***: Our AI algorithms deliver accurate and reliable insights.
        - ***User-Friendly Interface***: Easily navigate complex financial data with our intuitive design.
        - ***Real-Time Updates***: Stay informed with the latest market news and financial data.
        - ***Data-Driven Decisions***: Make informed investment choices based on quantitative analysis.
        
        Elevate Your Investment Strategy Today

        - ***Chart Analysis of single and multiple companies' stocks***.  

        - ***Financial Information:***

                - Company Information.
                - Company Share Asigned.
                - Stocks Recommendations.
                - Actions and Split.
                - Statistics.
                - Status of Evaluation.

        - ***Profiling each company:***

                - Interactions in High, Low, Close, Volume and Dividens.
                - Correlations: Pearson's r, Spearman's p, Kendalls's T, Phik (@K)
                - Matrix.
                - Heatmap.
                - Dentrogram.

        ---
        """)
        # today = st.date_input('Today is', datetime.datetime.now())

        footer_temp1 = """

            <!-- CSS  -->
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
            <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
            <footer class="background-color: black">
                <div class="container" id="About App">
                <div class="row">
                    <div class="col l6 s12">
                    </div>
            <div class="col l3 s12">
                    <h5 class="white-text">Connect With Me</h5>
                    <ul>
                        <a href="aiengineerdsml@gmail.com/" target="#002967" class="white-text">
                        ❤<i class="❤"></i>
                    </a>
                    <a href="https://www.linkedin.com/in/monica-bustamante-b2ba3781/3" target="#002966" class="white-text">
                        <i class="fab fa-linkedin fa-4x"></i>
                    <a href="aiengineerdsml@gmaill.com" target="#002967" class="white-text">
                    ❤<i class="❤"></i>
                    </a>
                    <a href="https://github.com/Moly-malibu/financesApp" target="#002967" class="white-text">
                        <i class="fab fa-github-square fa-4x"></i>
                    <a href="aiengineerdsml@gmail.com/" target="#002967" class="white-text">
                    ❤<i class="❤"></i>
                    </a>
                    </ul>
                    </div>
                </div>
                </div>
                <div class="footer-copyright">
                <div class="container">
                <a class="white-text text-lighten-3" href="aiengineerdsml@gmail.com/">Made by Liliana Bustamante</a><br/>
                <a class="white-text text" href=""> @Copyrigh</a>
                </div>
                </div>
            </footer>
            """
        components.html(footer_temp1,height=500)

    if __name__ == "__main__":
        main()

title_temp = """
	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	 <footer class="background-color: white">
	    <div class="container" id="About App">
	      <div class="row">
	        <div class="col l6 s12">
                <h4 style='text-align: center; class="black-text-dark">AI Internet of Things (IoT)-</h4>
              <h6 class="Sklearn, Tensorflow,  Keras, Pandas Profile, Numpy, Math, Data Visualization. </h6>
	        </div>     
	  </footer>
	"""
components.html(title_temp,height=100)
def Statement():
    page_bg_img = '''
    <style>
    .stApp{
    background-image: url("https://images.pexels.com/photos/950241/pexels-photo-950241.jpeg?cs=srgb&dl=pexels-gdtography-950241.jpg&fm=jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #002966;'>Overview</h1>", unsafe_allow_html=True)    

    symbols = 'https://raw.githubusercontent.com/Moly-malibu/AIApp/main/bxo_lmmS1.csv'
    df = pd.read_csv(symbols)

    ticker = st.sidebar.selectbox('Stocks by Company', (df))
    tickerData = YahooFinancials(ticker)
    company = yf.Ticker(ticker)
    
    # st.write(company.info) #Json
    try:
        website = company.info["website"]
        if website is not None:
                st.write('***Web site:***', website)
        else:
                st.write('***Web site:*** Information not available')
    except KeyError:
            st.write('***Web site:*** Information not available')
    #exception:
    try:
        industry = company.info["industry"]
        if industry is not None:
            st.write('***Industry:***',industry)
        else:
            st.write('***Industry:*** Information not available')
    except KeyError:
        st.write('***Industry:*** Information not available')
    
    company_general = st.sidebar.checkbox("Quick_Ratio")
    if company_general:
        st.subheader("""**Quick Ratio**""")
        quick_ratio = (company.info["quickRatio"])
        if not quick_ratio:
            st.write("No data available")
        else:
            st.write('***Quick Ratio:*** (CurrentAssets - Inventory)/Current Liabilities)')
            st.write(f'Quick Ratio: ${quick_ratio:,.2f}')
            
    company_hist = st.sidebar.checkbox("recommendations")
    if company_hist:
            st.markdown("<h1 style='text-align: center; color: #002966;'>recommendations</h1>", unsafe_allow_html=True)
            finan = company.recommendations_summary
            if finan.empty == True:
                st.write("No data available")
            else:
                st.write(finan)
    company_hist = st.sidebar.checkbox("Earnings History")
    if company_hist:
            st.markdown("<h1 style='text-align: center; color: #002966;'>Earnings History</h1>", unsafe_allow_html=True)
            apt = company.earnings_history
            if apt.empty == True:
                st.write("No data available")
            else:
                st.write(apt)
    company_hist = st.sidebar.checkbox("Dividends and Split")
    if company_hist:
            st.markdown("<h1 style='text-align: center; color: #002966;'>Dividends and Split</h1>", unsafe_allow_html=True)
            ds = company.actions
            if ds.empty == True:
                st.write("No data available")
            else:
                st.write(ds)
    
    # Options for financial statements
    statements = ["Income Statement", "Balance Sheet", "Cash Flow Statement", "Statement of Owner's Equity"]

    # Selectbox for choosing a financial statement
    selected_statement = st.selectbox("Choose a Financial Statement:", statements)
    # Display content based on selection
    st.markdown("<h1 style='text-align: center; color: #002966;'>Financial Statements</h1>", unsafe_allow_html=True)
    if selected_statement == "Income Statement":
        st.subheader("Income Statement")
        st.write("""
        The Income Statement shows the company's revenues and expenses during a specific period. 
        It provides insights into profitability and operational efficiency.
        Key components include:
        - Operating Revenue
        - Non-Operating Revenue
        - Total Expenses
        - Net Income
        """)
        st.markdown(
        """ 
        ***Income Statement***

        ***Purpose***: The income statement, also known as the profit and loss statement, details a company's revenues, expenses, and profits over a specific period.
        
        ***Importance***: It is often regarded as the most crucial statement by many users because it shows how profitable a company is during that time frame. It helps stakeholders understand operational efficiency and profitability metrics such as gross margin and net income
        """)
        st.write("""**Income Statement for each company**""", company.income_stmt) 
        

    elif selected_statement == "Balance Sheet":
        st.subheader("Balance Sheet")
        st.write("""
        The Balance Sheet presents a snapshot of a company's assets, liabilities, and equity at a specific point in time.
        It helps assess the company's financial position.
        Key components include:
        - Assets (Current and Non-Current)
        - Liabilities (Current and Long-Term)
        - Shareholder's Equity
        """)
        st.markdown(
        """ 
        ***Balance Sheet***

        ***Purpose***: The balance sheet presents a snapshot of a company's assets, liabilities, and shareholders' equity at a specific point in time.
        
        ***Importance***: While it may not directly reflect operational performance like the income statement or cash flow statement, it is crucial for assessing the overall financial position of a company. It shows how assets are financed (through debt or equity) and provides insights into long-term solvency and capital structure. 
        
        """)
        st.write("""**Balance for each company**""", company.balance_sheet)
        
    elif selected_statement == "Cash Flow Statement":
        st.subheader("Cash Flow Statement")
        st.write("""
        The Cash Flow Statement outlines the inflows and outflows of cash within the company over a period.
        It helps evaluate liquidity and cash management.
        Key components include:
        - Cash from Operating Activities
        - Cash from Investing Activities
        - Cash from Financing Activities
        """)
        st.markdown(
        """ 
        ***Cash Flow Statement***

        ***Purpose***: This statement tracks the flow of cash in and out of a business, categorized into operating, investing, and financing activities.
        
        ***Importance***: Many financial experts argue that the cash flow statement is the most critical financial statement. It provides insights into a company's liquidity and ability to sustain operations through cash management. It highlights whether a company generates enough cash to meet its obligations, making it vital for investors and creditors   
        
        """)
        st.write("""**Cash Flow Statement for each company**""",company.get_cashflow(freq='yearly'))  # For annual data

    elif selected_statement == "Statement of Owner's Equity":
        st.subheader("Statement of Owner's Equity")
        st.write("""
        The Statement of Owner's Equity details changes in equity from transactions with owners during a specific period.
        Key components include:
        - Beginning Equity
        - Additions (e.g., Investments)
        - Deductions (e.g., Withdrawals)
        - Ending Equity
        """)
        equity_data = company.get_financials()
        st.write("""**Statement of Owner's Equity**""", equity_data)  # For annual data
    #############################################################################################################################
    st.markdown("<h1 style='text-align: center; color: #002966;'>Financial Ratios</h1>", unsafe_allow_html=True)
    st.markdown(
    """ 
    These financial ratios provide valuable insights into a company's profitability, efficiency, liquidity, and valuation. By analyzing these ratios in conjunction with each other and comparing them against industry benchmarks or historical performance, investors can make more informed decisions regarding their investments in publicly traded companies.
    """)
    
    st.markdown(
    """
    
    Determining which financial statement is "most important" depends on the user's objectives: 
    
    ***Investors*** often focus on the cash flow statement to assess liquidity. 

    ***Management*** may prioritize the income statement to evaluate operational performance. 

    ***Creditors*** typically examine the balance sheet to understand risk and repayment capacity.

    In practice, these statements should be viewed together to gain a comprehensive understanding of a company's financial health

    Having direct access to financial statements empowers you to conduct in-depth analyses, enabling informed investment decisions. By scrutinizing these statements, you can gain valuable insights into a company's financial health, profitability, and growth potential. This knowledge empowers you to assess risk, identify opportunities, and make strategic investment choices that align with your financial goals.
    
    """)
    st.subheader("""Relevant Financial Ratios:""")
    st.markdown(
    """ 
    ***Price to Earnings (P/E) Ratio***: This ratio compares a company's current share price to its earnings per share (EPS). A high P/E may indicate that the stock is overvalued or that investors expect high growth rates in the future. 
    
    ***Price to Book (P/B) Ratio***: This measures a company's market value relative to its book value. A lower P/B ratio may suggest that the stock is undervalued.
    
    ***Price to Sales (P/S) Ratio***: This ratio compares a company's stock price to its revenues per share, providing insight into how much investors are willing to pay for each dollar of sales.

    """)
    
    # Get relevant financial data
    try:
            market_cap = company.info["marketCap"]
            if market_cap is not None:
                st.write(f'Market Capitalization:  ${market_cap:,.2f}')
            else:
                st.write('***Market Capitalization:*** Information not available')
    except KeyError:
            st.write('***Market Capitalization:*** Information not available')    
            
    # eps = company.info['trailingEps']        # Earnings Per Share (EPS)
    try:
            eps = company.info['trailingEps']
            if eps is not None:
                st.write(f'Trailing earnings per share: ${eps:,.2f}')
            else:
                st.write('***Trailing earnings per share:*** Information not available')
    except KeyError:
            st.write('***Trailing earnings per share:*** Information not available')   
            
    # book_value = company.info['bookValue']   # Book Value per Share
    try:
           book_value = company.info['bookValue']
           if book_value is not None:
                st.write(f'Book Value: ${book_value:,.2f}')
           else:
                st.write('***=Book Value:*** Information not available')
    except KeyError:
            st.write('***Book Value:*** Information not available')  
    # Exception
    try:
        dividend_yield = company.info['dividendYield']
        if dividend_yield is not None:
            st.write(f'Dividend Yield: ${dividend_yield:,.2f}')
        else:
            st.write('***Dividend Yield:*** Information not available')
    except KeyError:
            st.write('***Dividend Yield:*** Information not available')
    try:
            payout_ratio = company.info["payoutRatio"]
            if payout_ratio is not None:
                st.write(f'***Payout Ratio:*** ${payout_ratio:,.2f}')
            else:
                st.write('***Payout Ratio:*** Information not available')
    except KeyError:
            st.write('***Payout Ratio:*** Information not available')
    # Exception
    try:
            trailingAnnualDividendYield = company.info["trailingAnnualDividendYield"]
            if trailingAnnualDividendYield is not None:
                st.write(f'***Trailing Annual Dividend Yield:*** ${trailingAnnualDividendYield:,.2f}')
            else:
                st.write('***Trailing Annual Dividend Yield:*** Information not available')
    except KeyError:
            st.write('***Trailing Annual Dividend Yield:*** Information not available') 
        # Exception   
    try:
            dividendRate = company.info["dividendRate"]
            if dividendRate is not None:
                st.write(f'***Dividend Rate:*** ${dividendRate:,.2f}')
            else:
                st.write('***Dividend Rate:*** Information not available')
    except KeyError:
            st.write('***Dividend Rate:*** Information not available')

    # st.write("""**Dividend Yield**""", company.info["dividendYield"])
    # Exception
    try:
            profitMargins = company.info["profitMargins"]
            if profitMargins is not None:
                st.write(f'***Profit Margins:*** ${profitMargins:,.2f}')
            else:
                st.write('***Profit Margins:*** Information not available')
    except KeyError:
            st.write('***Profit Margins:*** Information not available')    

        # Exception
    try:
            pegRatio = company.info["pegRatio"]
            if pegRatio is not None:
                st.write(f'***Peg Ratio:*** ${pegRatio:,.2f}')
            else:
                st.write('***Peg Ratio:*** Information not available')
    except KeyError:
            st.write('***Peg Ratio:*** Information not available')

    # dividend_yield = company.info['dividendYield']  # Dividend Yield
    current_price = company.history(period='1d')['Close'].iloc[-1]
    # Price-to-Earnings Ratio (P/E)
    pe_ratio = current_price / eps if eps else None
    # Price-to-Book Ratio (P/B)
    pb_ratio = current_price / book_value if book_value else None
    # Dividend Yield is already fetched as a percentage
    dividend_yield_percentage = dividend_yield * 100 if dividend_yield else None

    # Displaying the results #f"${market_cap:,.2f}"
    st.write(f"Current Price: ${current_price: .2f}")
    # st.write(f"Market Cap: ${market_cap: ,.2f}") 
    st.write(f"Earnings Per Share (EPS): ${eps: .2f}")
    # st.write(f"Book Value: ${book_value: .2f}")
    # st.write(f"P/E Ratio: {pe_ratio: .2f}" if pe_ratio else "P/E Ratio: Not available")
    # st.write(f"P/B Ratio: {pb_ratio: .2f}" if pb_ratio else "P/B Ratio: Not available")
    # st.write(f"Dividend Yield: {dividend_yield_percentage: .2f}%" if dividend_yield_percentage else "Dividend Yield: Not available")
    
    #################################################################################################################
    # Options for financial Ratios
    statements = ["Price to Earnings (P/E) Ratio", "Price to Book (P/B) Ratio", "Price to Sales (P/S) Ratio", "Return on Equity (ROE)", "Return on Assets: ROA", "Analyst price Target", "Debt to Equity Ratio", "Current Ratio", "Quick Ratio (Acid-Test Ratio)"]
    # Selectbox for choosing a financial statement
    st.subheader("""Valuation Ratios by Company""")
    selected_statement = st.selectbox("Choose a Financial Ratios:", statements)
    # Display content based on selection
    if selected_statement == "Price to Earnings (P/E) Ratio":
        st.subheader("Price to Earnings (P/E) Ratio")
        st.write('The price/earnings to growth (PEG) ratio is a metric used by investors when valuing stocks. The PEG ratio can give a more complete picture than the P/E ratio because it factors in future earnings growth. PEG ratios above 1 are generally considered overvalued, while those below 1 are seen as undervalued.')
        st.write(""" 
        ***Definition***: Compares a company's market capitalization to its total sales over the past 12 months.
        
        ***Importance***: Useful for evaluating companies with little or no earnings. A lower P/S ratio may indicate better value.
        """)
        # st.write(f"P/E Ratio: {pe_ratio: .2f}" if pe_ratio else "P/E Ratio: Not available")
        # Attempt to fetch necessary data
        try:
            # Get P/E ratio
            pe_ratio = company.info.get('trailingPE', None)  # Trailing P/E ratio
            trailing_eps = company.info.get('trailingEps')   #Trailing Earnings Per Share
            current_price = company.info.get('currentPrice')  # Current stock price
            # Get expected annual growth rate (5-year expected growth rate)
            growth_rate = company.info.get('earningsGrowth', None)  # This is usually a percentage
            # Calculate P/E ratio if trailing PE is not available but EPS is
            if pe_ratio is None and trailing_eps is not None and current_price is not None:
                pe_ratio = current_price / trailing_eps  # Calculate P/E ratio
            # Check if we have valid data
            if pe_ratio is None:
                st.write("P/E Ratio: Not available")
            if growth_rate is not None:
                growth_rate_decimal = growth_rate / 100  # Convert percentage to decimal
            else:
                st.write("Expected Growth Rate: Not available")
            st.write(f"Price to Earnings : {pe_ratio:.2f}")
            st.write(f"Expected Growth Rate: {growth_rate_decimal:.2%}")
            # Calculate PEG Ratio
            if pe_ratio is not None and growth_rate_decimal is not None and growth_rate_decimal > 0:
                peg_ratio = pe_ratio / growth_rate_decimal
                st.write(f"Price Earnings to Growth: {peg_ratio: ,.2f}")
            else:
                st.write("price/earnings to growth: Not available or invalid due to zero/negative growth.")
        except IndexError as e:
            st.write("IndexError: The requested data is not available for this ticker.")
        except Exception as e:
            st.write(f"An error occurred: {e}")
            st.write(f"An error occurred fetching data: {e}")
    elif selected_statement == "Price to Sales (P/S) Ratio":
        st.subheader("Price to Sales (P/S) Ratio")
        st.write("TThe price to sales (P/S) ratio is a financial metric that compares a company's stock price to its sales or revenue:  What it measures. The P/S ratio indicates how much investors are willing to pay for each dollar of a company's sales. It's a useful way to assess a company's market valuation and determine if its stock is fairly priced. How it's calculated The P/S ratio is calculated by dividing a company's market capitalization by its total sales or revenue over the past 12 months.")
        # Attempt to fetch necessary data
        try:
            # Get current price
            current_price = company.info.get('currentPrice')  # Current stock price
            # Get total revenue (annual)
            total_revenue = company.info.get('totalRevenue')  # Total revenue

            # Check if we have valid data for P/S ratio calculation
            if current_price is None or total_revenue is None:
                st.write("Current Price or Total Revenue: Not available")
            # Calculate market capitalization
            market_cap = company.info.get('marketCap')  # Market capitalization

            # If market cap is not available, calculate it from current price and shares outstanding
            if market_cap is None:
                shares_outstanding = company.info.get('sharesOutstanding')
                if shares_outstanding is not None:
                    market_cap = current_price * shares_outstanding
            # Calculate P/S ratio
            if market_cap is not None and total_revenue > 0:
                ps_ratio = market_cap / total_revenue
                st.write(f"Price-to-Sales (P/S) Ratio for {ticker}: {ps_ratio:.2f}")
            else:
                st.write("Market Capitalization or Total Revenue is invalid for P/S calculation.")
        except Exception as e:
            st.write(f"An error occurred: {e}")
    elif selected_statement == "Price to Book (P/B) Ratio":
        st.subheader("Price to Book (P/B) Ratio")
        st.write(
        """
        Price to Book (P/B) Ratio: This measures a company's market value relative to its book value. A lower P/B ratio may suggest that the stock is undervalued.
        """)
        st.write(f"Book Value: ${book_value: .2f}")
    elif selected_statement == "Return on Equity (ROE)":
        st.subheader("Return on Equity (ROE")
        st.write(
        """
        ***Return on Equity (ROE)***
        
        ***Definition***: Measures net income as a percentage of shareholders' equity.
        
        ***Importance***: Indicates how effectively management is using equity financing to generate profits. Higher ROE values are generally favorable.
        """)
        roe = company.info.get('returnOnEquity')
        st.write(f"ROE: ${roe: ,.2f}")
    elif selected_statement == "Analyst price Target":
        st.subheader("Analyst price Target")
        my_dict = (company.analyst_price_targets)
        # Get the value associated with the key 'low'
        value = my_dict.get('low')
        valueh = (my_dict.get('high'))
        valuem =(my_dict.get('mean'))
        valuemm = (my_dict.get('median'))  
        # Display the result with a descriptive name
        st.write(f"Low Price is: {value}")
        st.write(f"High Price is: {valueh}")       
        st.write(f"Mean Price is: {valuem}")
        st.write(f"Median Price is: {valuemm}")
    elif selected_statement == "Debt to Equity Ratio":
        st.subheader("Debt to Equity Ratio")   
        st.markdown(
        """
        ***Definition***: Compares total liabilities to shareholders' equity.
        
        ***Importance***: Assesses a company's financial leverage and risk. A lower ratio generally indicates less risk, while a higher ratio suggests more risk due to increased debt levels.
        
        Debt-to-Equity Ratio = Total Debt / Total Shareholders' Equity
        
        ***Interpretation of the D/E Ratio***
        
        A higher D/E ratio indicates that a company is more leveraged, meaning it relies more on debt financing compared to equity. This can signal higher financial risk, especially if the company faces difficulties in meeting its debt obligations.
        
        A lower D/E ratio suggests that a company is less reliant on debt and may have a more stable financial structure. However, it could also indicate that the company is not taking full advantage of debt financing to fuel growth.
        """)
        # Fetching balance sheet data
        balance_sheet = company.balance_sheet
        
        # Extracting total debt and total equity
        total_debt = balance_sheet.loc['Total Liabilities Net Minority Interest'].values[0]
        total_equity = balance_sheet.loc['Ordinary Shares Number'].values[0] * company.info["lastDividendValue"]  # Approximation for equity
        
        # Calculating Debt to Equity Ratio
        if total_equity != 0:
            debt_to_equity_ratio = total_debt / total_equity
            st.write(f"Debt to Equity Ratio ${debt_to_equity_ratio: ,.2f}")
    elif selected_statement == "Debt to Equity Ratio":
        st.subheader("Debt to Equity Ratio")   
        st.markdown(
        """
        ***Definition***: Compares total liabilities to shareholders' equity.
        
        ***Importance***: Assesses a company's financial leverage and risk. A lower ratio generally indicates less risk, while a higher ratio suggests more risk due to increased debt levels.
        
        Debt-to-Equity Ratio = Total Debt / Total Shareholders' Equity
        
        ***Interpretation of the D/E Ratio***
        
        A higher D/E ratio indicates that a company is more leveraged, meaning it relies more on debt financing compared to equity. This can signal higher financial risk, especially if the company faces difficulties in meeting its debt obligations.
        
        A lower D/E ratio suggests that a company is less reliant on debt and may have a more stable financial structure. However, it could also indicate that the company is not taking full advantage of debt financing to fuel growth.
        """)
        # Fetching balance sheet data
        balance_sheet = company.balance_sheet
        
        # Extracting total debt and total equity
        total_debt = balance_sheet.loc['Total Liabilities Net Minority Interest'].values[0]
        total_equity = balance_sheet.loc['Ordinary Shares Number'].values[0] * company.info["lastDividendValue"]  # Approximation for equity
        
        # Calculating Debt to Equity Ratio
        if total_equity != 0:
            debt_to_equity_ratio = total_debt / total_equity
            st.write(f"Debt to Equity Ratio ${debt_to_equity_ratio: ,.2f}")
    elif selected_statement == "Current Ratio":
        st.subheader("Current Ratio")       
        st.markdown(
        """
        ***Current Ratio***
        
        ***Definition***: Measures a company's ability to pay short-term obligations by comparing current assets to current liabilities.
        
        ***Importance***: A current ratio above 1 indicates that the company can cover its short-term liabilities, which is essential for liquidity.
        
        """)
        # Fetching balance sheet data
        balance_sheet = company.balance_sheet
        # Extracting current assets and current liabilities
        
        current_assets = balance_sheet.loc['Current Assets'].values[0]
        current_liabilities = balance_sheet.loc['Current Liabilities'].values[0]
            # Calculating Current Ratio
        if current_assets != 0: 
            current_ratio = current_assets / current_liabilities
            st.write(f"current_ratio ${current_ratio: ,.2f}")
    elif selected_statement == "Quick Ratio (Acid-Test Ratio)":
        st.subheader("Quick Ratio (Acid-Test Ratio)")
        st.markdown(
        """
        ***Quick Ratio (Acid-Test Ratio)***
        
        ***Definition***: Similar to the current ratio but excludes inventory from current assets.
        
        ***Importance***: Provides a stricter measure of liquidity, indicating how well a company can meet short-term obligations without relying on inventory sales.
        """)
        # Fetching balance sheet data
        balance_sheet = company.balance_sheet
        # Extracting current assets, inventories, and current liabilities
        current_assets = balance_sheet.loc['Current Assets'].values[0]
        inventories = balance_sheet.loc['Inventory'].values[0]
        current_liabilities = balance_sheet.loc['Current Liabilities'].values[0]
        # Calculating Quick Ratio
        if current_assets != 0 or inventory != 0: 
            quick_ratio = (current_assets - inventory) / current_liabilities
            st.write(f"Quick_ratio ${quick_ratio: ,.2f}")
    elif selected_statement == "Return on Assets: ROA":
        st.subheader("Return on Assets: ROA")
        st.markdown(
        """
        ROA stands for Return on Assets. It's a financial ratio that measures how profitable a company is relative to its total assets. In simpler terms, it shows how well a company uses its assets to generate profits.   
        
        ROA = (Net Income / Total Assets) * 100%
        
        What does ROA tell you?

        Efficiency: A higher ROA indicates that a company is using its assets efficiently to generate profits.   
        Profitability: It helps you compare the profitability of different companies within the same industry.   
        Investment Potential: Investors often use ROA to evaluate the potential return on their investment in a company.   
        How to interpret ROA:

        Higher ROA is generally better: A higher ROA suggests that the company is using its assets effectively to generate profits.   
        Industry Comparison: It's important to compare a company's ROA with other companies in the same industry, as different industries have different benchmarks.   
        Trend Analysis: Tracking a company's ROA over time can help you identify trends and potential issues.   
        Remember: While ROA is a valuable tool, it's not the only metric to consider when evaluating a company's financial performance. Other factors like debt levels, revenue growth, and industry trends should also be taken into account
                
        """)
        income_statement = company.financials
        balance_sheet = company.balance_sheet

        # Extract relevant data
        net_income = income_statement.loc['Net Income'][-1]
        total_assets = balance_sheet.loc['Total Assets'][-1]
        
        # Calculating Quick Ratio
        if net_income != 0 or total_assets != 0: 
            # Calculate ROE
            roa = (net_income / total_assets) * 100
            st.write(f"ROA ${roa: ,.2f}")
            
    # #GRAPHIC 
    # Set the title of the app
    st.title('Stock Ticker Statistics')

    ## Input for stock ticker symbol
    ticker_symbol = st.text_input('Enter Stock Ticker Symbol', 'AAPL')

    # Fetch data from yfinance
    if ticker_symbol:
        data = yf.download(ticker_symbol, start="2020-01-01", end="2024-01-01")
        
        # Check if data is available
        if not data.empty:
            # Create a line chart for the closing price
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))

            # Update layout of the figure
            fig.update_layout(title=f'{ticker_symbol} Closing Prices',
                            xaxis_title='Date',
                            yaxis_title='Price (USD)',
                            template='plotly_dark')

            # Display the figure in Streamlit
            st.plotly_chart(fig)
        else:
            st.error("No data found for the given ticker symbol.")  
                
    # # Define the stock ticker symbol
    # ticker = 'AAPL'  # Example: Apple Inc.

    # # Fetch historical data for the specified ticker
    # data = yf.download(ticker, start='2020-01-01', end='2024-01-01')

    # # Display the first few rows of the dataset
    # print(data.head())
    
    # # Calculate daily returns
    # data['Daily Return'] = data['Adj Close'].pct_change()

    # # Calculate moving averages
    # data['30 Day MA'] = data['Adj Close'].rolling(window=30).mean()
    # data['100 Day MA'] = data['Adj Close'].rolling(window=100).mean()

    # # Plotting Closing Prices and Moving Averages
    # plt.figure(figsize=(14, 7))
    # plt.plot(data['Adj Close'], label='Adjusted Close Price', color='blue')
    # plt.plot(data['30 Day MA'], label='30 Day Moving Average', color='orange')
    # plt.plot(data['100 Day MA'], label='100 Day Moving Average', color='green')
    # plt.title(f'{ticker} Stock Price and Moving Averages')
    # plt.xlabel('Date')
    # plt.ylabel('Price (USD)')
    # plt.legend()
    # plt.show()

    # # Plotting Daily Returns
    # plt.figure(figsize=(14, 7))
    # plt.hist(data['Daily Return'].dropna(), bins=50, alpha=0.75)
    # plt.title(f'Daily Returns Histogram for {ticker}')
    # plt.xlabel('Daily Return')
    # plt.ylabel('Frequency')
    # plt.show()
    
    # import plotly.graph_objs as go

    # # Create a Plotly figure
    # fig = go.Figure()

    # # Add traces for Adjusted Close Price and Moving Averages
    # fig.add_trace(go.Scatter(x=data.index, y=data['Adj Close'], mode='lines', name='Adjusted Close'
    

            
            
#########################################
   

        ...    
# # Analysis stocks companies by close and volume
def IndustryAVG(): 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("https://images.pexels.com/photos/743986/pexels-photo-743986.jpeg?cs=srgb&dl=pexels-jess-bailey-designs-743986.jpg&fm=jpg&_gl=1*ckiwkv*_ga*MTI1MDQwMzMyOS4xNjU5ODc1MzA2*_ga_8JE65Q40S6*MTY2NjQxMzM3OS4xMC4xLjE2NjY0MTM3OTMuMC4wLjA.");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    symbols = 'https://raw.githubusercontent.com/Moly-malibu/AIApp/main/industAVG.csv'
    df = pd.read_csv(symbols)
    st.markdown("<h1 style='text-align: center; color: #002967;'>Stock Market</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #002967;'>Behavior by Industry</h1>", unsafe_allow_html=True)
    start = st.sidebar.date_input("Enter Date Begin Analysis: ") 
    tickerSymbol = st.sidebar.selectbox('Stocks Close and Volume price by Industry', (df))
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='id', start=start, end=None)
    st.markdown('Make Informed Stock Decisions, Simplified')
    company = tickerSymbol1 = st.sidebar.multiselect("Select Industry Stock be compared", (df))

    # Set up the Streamlit app title
    st.title('Stock Price Analysis Dashboard')

    # Sidebar for user input
    st.sidebar.header('User Input')
    ticker_input = st.sidebar.text_input('Enter Stock Ticker', value='^RUT')

    # Fetch and display data based on user input
    if ticker_input:
        data = yf.download(ticker_input, start='2020-01-01', end='2024-01-01')
        data['Daily Return'] = data['Adj Close'].pct_change()
        data['30 Day MA'] = data['Adj Close'].rolling(window=30).mean()
        data['100 Day MA'] = data['Adj Close'].rolling(window=100).mean()

        # Plotting the stock price and moving averages
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Adj Close'], mode='lines', name='Adjusted Close'))
        fig.add_trace(go.Scatter(x=data.index, y=data['30 Day MA'], mode='lines', name='30 Day MA'))
        fig.add_trace(go.Scatter(x=data.index, y=data['100 Day MA'], mode='lines', name='100 Day MA'))

        # Update layout of the figure
        fig.update_layout(title=f'{ticker_input} Stock Price and Moving Averages',
                        xaxis_title='Date',
                        yaxis_title='Price (USD)',
                        template='plotly_dark')

        # Display the figure in Streamlit
        st.plotly_chart(fig)

        # Show daily returns histogram
        st.subheader('Daily Returns Histogram')
        st.bar_chart(data['Daily Return'].dropna())
    
    

    if company:
        st.subheader("**Compared Status**")
        button_clicked = st.sidebar.button("GO")
        
        # Downloading data
        analysis = yf.download(tickerSymbol1, start=start, end=None)
        st.write('Analysis', analysis)
        
        # Check if data is available
        if not analysis.empty:
            fig, ax = plt.subplots()
            analysis['Adj Close'].plot(ax=ax)
            plt.xlabel("Date")
            plt.ylabel("Adjusted")
            plt.title("Stock by Industry")
            
            # Convert figure to HTML for interactivity
            fig_html = mpld3.fig_to_html(fig)
            st.components.v1.html(fig_html, height=600)
        else:
            st.write("No data available for this ticker.")

    if company:
        st.subheader("**Compared Status**")
        # button_clicked = st.sidebar.button("GO")
        
        # Downloading data
        analysis = yf.download(tickerSymbol1, start=start, end=None)
        st.write('Analysis', analysis)
        
        # Check if data is available
        if not analysis.empty:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=analysis.index, y=analysis['Adj Close'], mode='lines', name='Adjusted Close'))
            
            fig.update_layout(title='Stock by Industry',
                            xaxis_title='Date',
                            yaxis_title='Adjusted',
                            hovermode='x unified')
            
            # Display the interactive plot
            st.plotly_chart(fig)
        else:
            st.write("No data available for this ticker.")
        
        st.write(
        """
        Stock Market Indices

        - ***DJI (Dow Jones Industrial Average)***: A price-weighted index that tracks 30 large, publicly-owned companies in the U.S. It serves as a barometer for the overall health of the U.S. economy and is one of the oldest indices, established in 1896.
        
        - ***IXIC (NASDAQ Composite)***:  This index includes almost all stocks listed on the NASDAQ stock exchange, heavily weighted towards technology companies. It is a capitalization-weighted index, meaning companies with larger market capitalizations have a greater impact on its value.
        
        - ***GSPC (S&P 500)***: Comprising 500 of the largest U.S. companies, this index is also market-capitalization weighted. It is widely regarded as one of the best representations of the U.S. stock market and economy.
       
        - ***TYX (CBOE 10-Year Treasury Yield Index***: This index reflects the yield on 10-year U.S. Treasury bonds, which is often used as a benchmark for other interest rates and as an indicator of investor sentiment regarding future economic conditions.
       
        - ***NYA (NYSE Composite Index)***: This index includes all common stocks listed on the New York Stock Exchange (NYSE). It is a broad measure of the performance of the NYSE and includes both domestic and international companies.
        
        - ***N225 (Nikkei 225)***: A stock market index for the Tokyo Stock Exchange that includes 225 large companies. It is price-weighted, similar to the DJIA, and is one of Japan's most prominent indices.
        
        - ***RUT (Russell 2000)***: This index measures the performance of the smallest 2,000 stocks in the Russell 3000 Index, representing small-cap companies in the U.S. market.
        Commodity Futures
        
        - ***CL=F (Crude Oil WTI Futures)***: This represents futures contracts for West Texas Intermediate (WTI) crude oil, a benchmark for oil pricing in North America.
        
        - ***GC=F (Gold Futures)***: This symbol represents futures contracts for gold, which are used by investors to hedge against inflation or currency fluctuations.
        
        - ***SI=F (Silver Futures)***:  Similar to gold futures, this represents futures contracts for silver, another precious metal often used as an investment.
        Currency Pairs
        
        - ***EURUSD=X***: This symbol represents the exchange rate between the Euro and the U.S. Dollar, one of the most traded currency pairs in the world.
        
        - ***GBPUSD=X***: This represents the exchange rate between the British Pound and the U.S. Dollar, another major currency pair in global markets.
        Other Indices
        
        - ***TNX (CBOE 10-Year Treasury Note Yield)***: This index reflects the yield on 10-year Treasury notes, providing insights into investor expectations regarding future interest rates and inflation.
        
        - ***CMC200 (Crypto Market Cap Index)***:  An index that tracks the market capitalization of cryptocurrencies, providing a snapshot of overall market performance in this sector.
        
        - ***BTC-USD (Bitcoin)***: Represents Bitcoin's price in U.S. Dollars, reflecting its value in the cryptocurrency market.
        
        
        
        These indices and commodities provide valuable insights into various sectors of financial markets, including equities, commodities, currencies, and fixed income securities. They are widely used by investors for analysis and decision-making regarding investments and economic trends.

        EXAMPlE:

        When comparing the Dow Jones Industrial Average (DJI), the CBOE 10-Year Treasury Yield Index (TYX), and the Nikkei 225 (N225), several insights can be drawn regarding market performance, economic conditions, and investor sentiment. Here’s a breakdown of what this comparison can show:
        
        
        - ***1. Market Performance***:

        ***DJI***: Represents the performance of 30 large, established companies in the U.S. A rising DJI indicates strong performance in the industrial sector and overall economic health.
        
        ***TYX***: Reflects the yield on 10-year U.S. Treasury bonds. A higher yield often suggests that investors expect stronger economic growth and potentially higher inflation, leading to increased interest rates.
        
        ***N225***: Shows the performance of major Japanese companies. Comparing it with DJI can highlight differences in market sentiment between the U.S. and Japan.
        
        - ***2. Economic Indicators*** The relationship between DJI and TYX can indicate investor confidence. If the DJI is rising while TYX is also increasing, it may suggest that investors are optimistic about economic growth but are also concerned about inflation leading to higher interest rates.
        Conversely, if DJI is falling while TYX rises, it may indicate a flight to safety among investors, where they prefer bonds over stocks due to economic uncertainty.
        
       - ***3. Global Market Trends***

        Comparing DJI and N225 can provide insights into how global markets react to similar economic events. ***For example***, if both indices are moving in tandem, it may suggest a global trend affecting investor sentiment.
        If one index rises while the other falls, it may indicate regional differences in economic conditions or investor confidence.
        
        - ***4. Investment Strategies***

        Investors might use this comparison to make decisions about asset allocation. For instance, if DJI is performing well but TYX is rising sharply, it may prompt investors to shift some assets from stocks to bonds to hedge against potential interest rate hikes.
        Observing N225 alongside DJI could influence decisions for international investments, particularly for those looking at exposure in Asian markets.
        
        - ***5. Risk Assessment***
        The volatility of these indices can help assess market risk. A stable DJI with fluctuating TYX could suggest a cautious approach to investing in U.S. equities, while a volatile N225 might signal greater risk in Japanese markets.
        
        
        - ***Conclusion***
        
        
        By comparing the DJI with TYX and N225, investors can gain a comprehensive view of market dynamics, economic expectations, and global trends. This analysis helps in making informed investment decisions based on varying factors influencing stock and bond markets across different regions.


        ---
        """)

def Index():        
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("https://img.freepik.com/free-photo/3d-geometric-abstract-cuboid-wallpaper-background_1048-9891.jpg?size=626&ext=jpg&ga=GA1.2.635976572.1603931911");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    symbols = 'https://raw.githubusercontent.com/Moly-malibu/AIApp/main/bxo_lmmS1.csv'
    # Load symbols from CSV
    df = pd.read_csv(symbols)

    st.markdown("<h1 style='text-align: center; color: #002967;'>Stock Price </h1>", unsafe_allow_html=True)
    
    # Date input for analysis start date
    start = st.sidebar.date_input("Enter Date Begin Analysis:")

    # Select box for ticker symbols
    tickerSymbol = st.sidebar.selectbox('Stocks Close and Volume price by Company', df['Symbol'].tolist())  # Ensure 'Symbol' is a column in df
    
    # Fetching ticker data
    tickerData = yf.Ticker(tickerSymbol)

    # Fetch historical data starting from 'start'
    tickerDf = tickerData.history(start=start)

    # Display analysis header
    st.write("# Analysis of Data")

    # Check if DataFrame is not empty
    if not tickerDf.empty:
        # Displaying closing prices
        st.write("## Closing Prices")
        st.line_chart(tickerDf['Close'])
    else:
        st.write("No data available for this ticker symbol.")

    company = yf.Ticker(tickerSymbol)
    st.write('Company name and Web:', company.info["website"])
    # st.line_chart(tickerDf.Close)
    st.write(""" 
    ## Volume Price
    """)
    st.line_chart(tickerDf.Volume)
    st.write(tickerDf)
    st.markdown("<h1 style='text-align: center; color: #002967;'>Stock Price Compared</h1>", unsafe_allow_html=True)
    st.write("""
    **Business** and **Techology** are two fills that have changed the world, both occupy the main ratings in finance, being one of the most highly valued in the stock market leading their owners to be billionaires, in this simple application we can analyze the stock movement and prediction of future price of stock used algoriths and Machile Learning.
    Show are the Stock **Closing Price** and ** Volume** of Stocks by year!
    """)
    st.markdown('Help to take algoritmc decision about stocks')
    company = tickerSymbol1 = st.sidebar.multiselect("Select Companies Stock be compared", (df))

        # Sidebar for selecting companies
    company = st.sidebar.multiselect("Select Companies Stock to be compared", (df))

    if company:
        st.subheader("**Compared Status**")
        button_clicked = st.sidebar.button("GO")
        
        # Downloading data
        tickerDf = yf.download(company, start=start, end=None)
        
        # Check if data is available
        if not tickerDf.empty:
            # Create a Plotly figure
            fig = go.Figure()
            
            # Add traces for each selected company
            for ticker in company:
                fig.add_trace(go.Scatter(x=tickerDf.index, 
                                        y=tickerDf['Adj Close'][ticker], 
                                        mode='lines', 
                                        name=ticker))

            # Update layout with titles and labels
            fig.update_layout(title='Company Stock Comparison',
                            xaxis_title='Date',
                            yaxis_title='Adjusted Close Price',
                            legend_title='Companies',
                            hovermode='x unified')
            
            # Display the interactive plot
            st.plotly_chart(fig)

            # Volume chart (optional)
            volume_fig = go.Figure()
            for ticker in company:
                volume_fig.add_trace(go.Bar(x=tickerDf.index, 
                                            y=tickerDf['Volume'][ticker], 
                                            name=ticker))
            
            volume_fig.update_layout(title='Trading Volume Comparison',
                                    xaxis_title='Date',
                                    yaxis_title='Volume',
                                    barmode='stack')
            
            st.plotly_chart(volume_fig)
            
        else:
            st.write("No data available for the selected stocks.")

# Portfolio
def Portfolio():
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("https://www.istockphoto.com/vector/white-luxury-abstract-background-with-vector-illustration-gm1497133340-519598971");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    symbols = 'https://raw.githubusercontent.com/Moly-malibu/AIApp/main/bxo_lmmS1.csv'
    df = pd.read_csv(symbols)
    st.markdown("<h1 style='text-align: center; color: #002967;'>Portfolio</h1>", unsafe_allow_html=True)
    st.write(""" Make your ***own Portfolio*** with 5 companies and analyze what will be your profit.""")
    st.write("""***Instructions:***""") 
    st.write(
        """
        - Select 5 companies where you want to invest or Analysis.  ('others' it needs more companies)  

        - Select Date.
        ---
        """)
    
    stockStarData = st.sidebar.date_input("Select Date when you started to investing:")
    company = tickerSymbol1 = st.multiselect("Select Companies to create the Portfolio", (df['Symbol']))
    button_clicked = st.sidebar.button("GO")
    if company:
        def getmyportfolio(stock=tickerSymbol1, start=stockStarData, end=None):
            numAssets = len(tickerSymbol1)
            st.write('***you have*** ' +str(numAssets) + ' ***Assets in your Portafolio.***')
            data = yf.download(tickerSymbol1, start=start, end=end)['Adj Close']
            return data
        my_stocks = getmyportfolio(tickerSymbol1)
        st.write(my_stocks)
        daily_return = my_stocks.pct_change(1)
        daily_return.corr()
        daily_return.cov()
        daily_return.var()
        daily_return.std()
        st.write('***Stock Return***',daily_return)
        st.write('***Stock Correlation***',daily_return.corr())

        # Calculate daily returns
        daily_returns = my_stocks.pct_change()

        # Calculate correlation matrix
        correlation_matrix = daily_returns.corr()

        # Display the correlation matrix as a heatmap
        import seaborn as sns
        st.subheader("Stock Correlation Heatmap")
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title("Correlation Matrix of Selected Stocks")
        
        # Show the plot in Streamlit
        st.pyplot(plt)
    else:
        st.write("Please enter valid stock tickers.")


        st.write('***Stock Covariance Matrix for Return***',daily_return.cov())
        st.write('***Stock Variance***',daily_return.var())
        st.write('***Stock Volatility***', daily_return.std())
    
    #Visualization
        # Load symbols from CSV (ensure 'symbols' is defined)
    df = pd.read_csv(symbols)

    st.markdown("<h1 style='text-align: center; color: #002967;'>Stock Price </h1>", unsafe_allow_html=True)

    # Date input for analysis start date
    start = st.sidebar.date_input("Enter Date Begin Analysis:")

    # Select box for ticker symbols
    tickerSymbol = st.sidebar.selectbox('Stocks Close and Volume price by Company', df['Symbol'].tolist())  # Ensure 'Symbol' is a column in df

    # Fetching ticker data
    tickerData = yf.Ticker(tickerSymbol)

    # Fetch historical data starting from 'start'
    tickerDf = tickerData.history(start=start)

    # Display analysis header
    st.write("# Analysis of Data")

    # Check if DataFrame is not empty
    if not tickerDf.empty:
        # Create a candlestick chart using Plotly
        fig = go.Figure(data=[go.Candlestick(x=tickerDf.index,
                                            open=tickerDf['Open'],
                                            high=tickerDf['High'],
                                            low=tickerDf['Low'],
                                            close=tickerDf['Close'])])

        # Update layout of the chart
        fig.update_layout(title=f'Candlestick Chart for {tickerSymbol}',
                        xaxis_title='Date',
                        yaxis_title='Price',
                        xaxis_rangeslider_visible=False)

        # Display the candlestick chart in Streamlit
        st.plotly_chart(fig)
    else:
        st.write("No data available for this ticker symbol.")

    #get Growth Investment
        dailyMeanSimpleReturns = daily_return.mean()
        randomWeights = np.array([0.4, 0.1, 0.3, 0.1, 0.1])
        portfoliosimpleReturn = np.sum(dailyMeanSimpleReturns*randomWeights)
        dailyCumulSimpleReturn = (daily_return+1).cumprod()
    st.write("""***Daily Expected Portfolio Return and Expected Annualized Portfolio Return***""")
    st.markdown(
    """ 
    When you have both the Daily Expected Portfolio Return and the Expected Annualized Portfolio Return, you can draw several conclusions about your investment portfolio. Here’s a breakdown of what these metrics imply and how they can guide your investment decisions:
    Understanding Daily Expected Portfolio Return.

    - ***Short-Term Performance***: The Daily Expected Portfolio Return gives you an estimate of how much return you can expect from your portfolio on a daily basis. This is useful for short-term trading strategies or for understanding daily fluctuations in your investment's value.
    
    - ***Volatility Assessment***: A higher daily expected return may indicate a more volatile portfolio, where returns can fluctuate significantly day-to-day. This can help you gauge the risk level associated with your investments.
    Understanding Expected Annualized Portfolio Return
   
    - ***Long-Term Growth Projection***: The Expected Annualized Portfolio Return translates the daily returns into an annual figure, providing a more comprehensive view of potential growth over a year. This is crucial for long-term investment planning and assessing whether your portfolio aligns with your financial goals.
    Comparison with Benchmarks: You can compare the expected annualized return against benchmarks (like market indices) to evaluate whether your portfolio is likely to outperform or underperform relative to the market.
    
    
    ***Conclusions:***

    - ***Risk vs. Reward***: If the daily expected return is significantly higher than the annualized return, it may indicate that while short-term gains could be substantial, the overall annual performance may not reflect that due to volatility or market conditions. This highlights the importance of understanding both short-term and long-term perspectives.
    
    - ***Investment Strategy Alignment***: If your expected annualized return meets or exceeds your investment goals (e.g., retirement savings, purchasing a home), it suggests that your current asset allocation and investment strategy are aligned with your financial objectives.
    
    - ***Portfolio Adjustments***: If the expected returns are lower than desired, consider rebalancing your portfolio by adjusting asset allocations, diversifying into higher-return assets, or exploring different investment strategies to enhance overall returns.
    
    - ***Performance Monitoring***: Regularly monitor both daily and annualized returns to assess whether your investments are performing as expected. This can help in making timely adjustments to mitigate losses or capitalize on gains.
    
    - ***Expectations Management***: Both metrics serve as reminders that investment returns are not guaranteed and are subject to market risks. They help set realistic expectations for future performance based on historical data and market conditions.
    
    - ***Example Calculation To illustrate***, if you have a Daily Expected Portfolio Return of 0.05% (or 5% annually) and an Expected Annualized Portfolio Return of 8%, this suggests:
    Your investments are projected to grow at a reasonable rate annually. The daily return indicates potential for short-term gains, but you should consider whether this aligns with your risk tolerance and investment horizon.
    
    
    - ***Conclusion***:

    By analyzing both daily expected returns and annualized returns, you gain a comprehensive view of your portfolio's performance potential. This dual perspective aids in making informed decisions about risk management, portfolio adjustments, and aligning investments with long-term financial goals.


    """)

    #Visualization
    # Calculate daily mean simple returns
    dailyMeanSimpleReturns = daily_return.mean()
    st.write('***Daily Mean Simple Return:*** ', dailyMeanSimpleReturns)

    # Define random weights for the portfolio
    randomWeights = np.array([0.4, 0.1, 0.3, 0.1, 0.1])
    portfoliosimpleReturn = np.sum(dailyMeanSimpleReturns * randomWeights)
    st.write('***Daily Expected Portfolio Return:*** ', portfoliosimpleReturn)
   
    # Calculate expected annualized portfolio return
    expectedAnnualizedReturn = portfoliosimpleReturn * 253  # Assuming 253 trading days in a year
    st.write('***Expected Annualized Portfolio Return:*** ', expectedAnnualizedReturn)

    # Calculate cumulative simple returns
    dailyCumulSimpleReturn = (daily_return + 1).cumprod()
    st.write('***Growth of Investment:*** ', dailyCumulSimpleReturn)

    # Visualization with Matplotlib
    # st.subheader("Matplotlib Visualization")

    st.title("Cumulative Returns Visualization")

    # Select the columns to plot
    selected_columns = st.multiselect('Select Stocks', dailyCumulSimpleReturn.columns)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    for col in selected_columns:
        ax.plot(dailyCumulSimpleReturn.index, dailyCumulSimpleReturn[col].cumprod(), label=col)

    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative Return')
    ax.set_title('Cumulative Returns of Selected Stocks')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
    plt.figure(figsize=(12.2, 6))
    for c in dailyCumulSimpleReturn.columns.values:
        plt.plot(dailyCumulSimpleReturn.index, dailyCumulSimpleReturn[c], lw=2, label=c)

    plt.grid(True)
    plt.legend(loc='upper left', fontsize=10)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Growth of $1 Investment', fontsize=12)
    plt.title('Daily Cumulative Returns', fontsize=14)

    # Show the plot in Streamlit
    st.pyplot()

    # Visualization with Plotly
    st.subheader("Dayly Cumulative Return")
    fig = go.Figure()

    for c in dailyCumulSimpleReturn.columns.values:
        fig.add_trace(go.Scatter(x=dailyCumulSimpleReturn.index,
                                y=dailyCumulSimpleReturn[c],
                                mode='lines+markers',
                                name=c))

    fig.update_layout(title='Daily Cumulative Returns',
                    xaxis_title='Date',
                    yaxis_title='Growth of $1 Investment',
                    legend_title='Stocks',
                    template='plotly_white')  # Clean template

    # Display the interactive plot in Streamlit
    st.plotly_chart(fig)  # Use st.plotly_chart() for Plotly figures only

#Differente models to predict the price.
# def Prediction():
#     page_bg_img = '''
#     <style>
#     .stApp {
#     background-image: url("https://images.pexels.com/photos/4194857/pexels-photo-4194857.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=1000");
#     background-size: cover;
#     }
#     </style>
#     '''
#     # Assuming page_bg_img is defined somewhere in your code
#     st.markdown(page_bg_img, unsafe_allow_html=True)

    # symbols = 'https://raw.githubusercontent.com/Moly-malibu/AIApp/main/bxo_lmmS1.csv'
    # df = pd.read_csv(symbols)

    # # Get the current date and time correctly
    # now = pd.to_datetime('now')

    # tickerSymbol = st.sidebar.selectbox('Company List', (df['Symbol']))
    # tickerData = yf.Ticker(tickerSymbol)
    # tickerDf = tickerData.history(period='id', start='2019-01-01', end=now)
    # data = tickerDf.filter(['Close'])
    # dataset = data.values
    # company = yf.Ticker(tickerSymbol)
    # st.write('Web:', company.info["website"])
    # # company_hist = st.sidebar.checkbox('Long Short Term Memory')
    
    # if company_hist:
    #     st.markdown("<h1 style='text-align: center; color: #002966;'>Long Short Term Memory</h1>", unsafe_allow_html=True)
        
    #     # Scaler data
    #     train_len = math.ceil(len(dataset) * .8)
    #     scaler = MinMaxScaler(feature_range=(0, 1))
    #     scaled_data = scaler.fit_transform(dataset)
        
    #     train_data = scaled_data[0:train_len, :]
        
    #     # Train data preparation
    #     x_train = []
    #     y_train = []
        
    #     for i in range(60, len(train_data)):
    #         x_train.append(train_data[i-60:i, 0])
    #         y_train.append(train_data[i, 0])
    #         if i <= 60:
    #             print(x_train)
    #             print(y_train)
        
    #     x_train, y_train = np.array(x_train), np.array(y_train)
    #     x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))  # Reshape for LSTM model
        
    #     # Model definition
    #     model =tf.keras.Sequential()
    #     model.add(LSTM(54, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    #     model.add(LSTM(50, return_sequences=False))
    #     model.add(Dense(25))
    #     model.add(Dense(1))
    #     model.tf.keras.layers.Dense(10)

    #     # Compile the model
    #     model.compile(optimizer='adam', loss='mean_squared_error')
    #     model.compile(loss='mean_squared_error', optimizer='adam')
    #     model.fit(x_train, y_train, batch_size=1, epochs=1)

    #     # Test data preparation
    #     test_data = scaled_data[train_len - 60:, :]
    #     x_test = []
    #     y_test = dataset[train_len:, :]
        
    #     for i in range(60, len(test_data)):
    #         x_test.append(test_data[i-60:i, 0])
        
    #     x_test = np.array(x_test)
    #     x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        
    #     predictions = model.predict(x_test)
    #     predictions = scaler.inverse_transform(predictions)

    #     # Graphic preparation
    #     train = data[:train_len]
    #     valid = data[train_len:]
    #     valid['Predictions'] = predictions

    # st.markdown(page_bg_img, unsafe_allow_html=True)

    # symbols = 'https://raw.githubusercontent.com/Moly-malibu/AIApp/main/bxo_lmmS1.csv'
    # df = pd.read_csv(symbols)

    # # #Firs model to predict price and accuracy
    # now = pd.to_datetime('now')
    # tickerSymbol = st.sidebar.selectbox('Company List', (df['Symbol']))

    # tickerData = yf.Ticker(tickerSymbol)
    # tickerDf = tickerData.history(period='id', start='2019-01-01', end=now)
    # data = tickerDf.filter(['Close'])
    # dataset = data.values
    # company = yf.Ticker(tickerSymbol)

    # st.write('Web:', company.info["website"])
    
    # # company_hist = st.sidebar.checkbox('Long Short Term Memory')

    # if company_hist:
    #     st.markdown("<h1 style='text-align: center; color: #002966;'>Long Short Term Memory</h1>", unsafe_allow_html=True)

    #     #Scaler data
    #     train_len = math.ceil(len(dataset)*.8)
    #     scaler = MinMaxScaler(feature_range=(0,1))
    #     scaled_data = scaler.fit_transform(dataset)
    #     train_data = scaled_data[0:train_len, :]

    #     #train data
    #     x_train = []
    #     y_train = []
    #     for i in range(60, len(train_data)):
    #         x_train.append(train_data[i-60:i,0])
    #         y_train.append(train_data[i,0])
    #         if i<=60:
    #             print(x_train)
    #             print(y_train)
    #     x_train, y_train = np.array(x_train), np.array(y_train)
    #     x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1],1))        #Model
    #     model = Sequential()
    #     model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1],1)))
    #     model.add(LSTM(50, return_sequences=False))
    #     model.add(Dense(25))
    #     model.add(Dense(1))
    #     model.compile(optimizer='adam', loss='mean_squared_error')
    #     model.fit(x_train, y_train, batch_size=1, epochs=1)

    #     #Test data
    #     test_data = scaled_data[train_len - 60: , :]
    #     x_test = []
    #     y_test = dataset[train_len:, :]
    #     for i in range(60, len(test_data)):
    #         x_test.append(test_data[i-60:i,0])
    #     x_test = np.array(x_test)
    #     x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))
    #     predictions = model.predict(x_test)
    #     predictions = scaler.inverse_transform(predictions)

    #     #Graphic
    #     train = data[:train_len]
    #     valid = data[train_len:]
    #     valid['Predictions'] = predictions

    #     plt.figure(figsize=(16,8))
    #     plt.title('Model')
    #     plt.xlabel('Date', fontsize=18)
    #     plt.ylabel('Close Price USD($)', fontsize=18)
    #     plt.plot(train['Close'])
    #     plt.plot(valid[['Close', 'Predictions']])
    #     plt.legend(['train', 'Val', 'Predictions'], loc='upper left')
    #     st.set_option('deprecation.showPyplotGlobalUse', False)
    #     st.pyplot()


    #     st.markdown("<h1 style='text-align: center; color: #002966;'>Forecasting the Price Stocks</h1>", unsafe_allow_html=True)
    #     st.write(""" 
    #     Using keras Long Short Term Memory (LSTM) model that permit to store past information to predict the future price of stocks.
    #     """)
    #     st.write(predictions)
    #     st.markdown("<h1 style='text-align: center; color: #002966;'>Root Mean Square Deviation</h1>", unsafe_allow_html=True)
    #     st.write(""" 
    #     The RMSE shows us how concentrated the data is around the line of best fit.
    #     """)
    #     rmse = np.sqrt(np.mean(predictions - y_test)**2)
    #     st.write(rmse)


#     #Second Model
    # from sklearn.model_selection import train_test_split, GridSearchCV
    # from sklearn.ensemble import RandomForestRegressor
    # import matplotlib.pyplot as plt

    # company_hist = st.sidebar.checkbox('Decision Tree Regression')

    # forcast_days = 25
    # tickerDf['Prediction'] = tickerDf[['Close']].shift(-forcast_days)

    # # Feature Engineering: Create additional features like moving averages
    # tickerDf['MA_5'] = tickerDf['Close'].rolling(window=5).mean()
    # tickerDf['MA_10'] = tickerDf['Close'].rolling(window=10).mean()
    # tickerDf.dropna(inplace=True)  # Drop NaN values after creating moving averages

    # X = np.array(tickerDf.drop(['Prediction'], axis=1)[:-forcast_days].fillna(0))
    # y = np.array(tickerDf['Prediction'])[:-forcast_days]

    # # Train-Test Split    
    # x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # # Model Selection: Using Random Forest Regressor instead of Decision Tree Regressor
    # model = RandomForestRegressor(n_estimators=100)
    # model.fit(x_train, y_train)

    # # Prepare future data for prediction
    # x_future = tickerDf.drop(['Prediction'], axis=1)[-forcast_days:]
    # x_future = np.array(x_future)

    # # Predict future prices
    # tree_prediction = model.predict(x_future)

    # # Visualize Predictions
    # valid = tickerDf[X.shape[0]:]
    # valid['Predictions'] = np.nan  # Initialize Predictions column with NaN values
    # valid.iloc[-forcast_days:, valid.columns.get_loc('Predictions')] = tree_prediction  # Fill in predictions

    # # Streamlit Visualization
    # st.markdown("<h1 style='text-align: center; color: #002966;'>Random Forest Regression Model</h1>", unsafe_allow_html=True)
    # st.line_chart(valid[['Close', 'Predictions']])


    # if company_hist: 
    #     forcast_days = 25
    #     tickerDf['Prediction'] = tickerDf[['Close']].shift(-forcast_days)
    #     X=np.array(tickerDf.drop(['Prediction'], 1)[:-forcast_days].fillna(0))
    #     y=np.array(tickerDf['Prediction'])[:-forcast_days] 

    #     # #Train Data    
    #     x_train, x_test, y_train, y_test= train_test_split(X,y, test_size=0.25)
    #     tree = DecisionTreeRegressor().fit(x_train, y_train)
    #     # x_future = tickerDf.drop(['Prediction'], 1)[:-forcast_days]
    #     x_future = x_future.tail(forcast_days)
    #     x_future = np.array(x_future)
    #     tree_prediction = tree.predict(x_future)
    #     st.markdown("<h1 style='text-align: center; color: #002966;'>Decision Tree Regression Model</h1>", unsafe_allow_html=True)

    #     # #Graph 
    #     predictions = tree_prediction
    #     valid = tickerDf[X.shape[0]:]
    #     valid['Predictions'] = predictions

    #     plt.figure(figsize=(16,8))
    #     plt.title('Model')
    #     plt.xlabel('Days')
    #     plt.ylabel('Close Price USD($)')
    #     plt.plot(tickerDf['Close'])
    #     plt.plot(valid[['Close', 'Predictions']])
    #     plt.legend(['orig', 'Val', 'Pred'])
    #     st.set_option('deprecation.showPyplotGlobalUse', False)
    #     st.pyplot()
    #     st.write('Prediction:', predictions) 
    #     st.write('Accuracy:', tree.score(x_train, y_train))

    #     tree_confidence = tree.score(x_test, y_test)
        
    #     st.write('Confidence:', tree_confidence)

    # Third Model
    # company_hist = st.sidebar.checkbox('Linear Regression')
    
    # if company_hist:     
    #     st.markdown("<h1 style='text-align: center; color: #002966;'>Linea Regression Model</h1>", unsafe_allow_html=True)
        
    #     forcast_days = 25
    #     tickerDf['Prediction'] = tickerDf[['Close']].shift(-forcast_days)
    #     X = np.array(tickerDf.drop(['Prediction'], axis=1)[:-forcast_days].fillna(0))
    #     y = np.array(tickerDf['Prediction'])[:-forcast_days]

    #     # Prepare future data for prediction
    #     x_future = tickerDf.drop(['Prediction'], axis=1).tail(forcast_days)
    #     x_future = np.array(x_future)

    #     # #Train Data    
    #     x_train, x_test, y_train, y_test= train_test_split(X,y, test_size=0.25)
    #     lr = LinearRegression().fit(x_train, y_train)
    #     lr_prediction = lr.predict((x_future))
    #     lr_confidence = lr.score(x_test, y_test)

    #     #Prediction
    #     predictions = lr_prediction
    #     valid = tickerDf[X.shape[0]:]
    #     valid['Predictions'] = predictions

    #     plt.figure(figsize=(16,8))
    #     plt.title('Model')
    #     plt.xlabel('Days')
    #     plt.ylabel('Close Price USD($)')
    #     plt.plot(tickerDf['Close'])
    #     plt.plot(valid[['Close', 'Predictions']])
    #     plt.legend(['orig', 'Val', 'Pred'])
    #     st.set_option('deprecation.showPyplotGlobalUse', False)

    #     st.pyplot()
    #     st.write('Predictioin by LR:', predictions)
    #     st.write('Accuracy:', lr.score(x_train, y_train))
    #     st.write('linear Regression confidence:', lr_confidence)

    # st.markdown("<h1 style='text-align: center; color: #002966;'>Compared Forecasting</h1>", unsafe_allow_html=True)
    # new_predict = tickerDf['Close']
    # st.write(tickerDf)
        



def Stock():
    page_bg_img = """
    <style>
    .stApp {
    background-image: url("https://media.istockphoto.com/id/1126699549/vector/empty-white-room-the-inner-space-of-the-light-box-vector-design-illustration-mock-up-for-you.jpg?s=612x612&w=0&k=20&c=KjR99MWfsh8MciAn63VhbgedDH7JG-P_xsrcLPqO5pE=");
    background-size: cover;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    symbols = 'https://raw.githubusercontent.com/Moly-malibu/AIApp/main/bxo_lmmS1.csv'
    df = pd.read_csv(symbols)
    # st.markdown("<h1 style='text-align: center; color: #002966;'>Financial Information</h1>", unsafe_allow_html=True)
    st.write("""
    Financial information from the companies and Stocks by years!
    """)
    start = st.sidebar.date_input("Date to Analysis")
    st.sidebar.subheader("Index")
    tickerSymbol2 = st.sidebar.selectbox('Stocks by Company', (df))
    tickerData = yf.Ticker(tickerSymbol2)
    tickerDf = tickerData.history(period='id', start=start, end=None)

    company = yf.Ticker(tickerSymbol2)
    company = yf.Ticker(tickerSymbol2)
    st.write('Web:', company.info["website"])
    # st.write(company.info)
    company_general = st.sidebar.checkbox("Company Information")

    if company_general:
        st.markdown("<h1 style='text-align: center; color: #002966;'>General Information</h1>", unsafe_allow_html=True)
        st.write('***Sector:***', company.info["sector"])
        st.write('***Industry:***', company.info["industry"])
        st.write('***Phone:***', company.info["phone"])
        st.write('***Address:***', company.info["address1"])
        st.write('***City:***', company.info["city"])
        st.write('***Country:***', company.info["country"])
        st.write('***Web:***', company.info["website"])
        st.write('***Business Summary:***', '\n', company.info["longBusinessSummary"])
        st.write('***Job Generator*** ${company.info["fullTimeEmployees"]')
    company_hist = st.sidebar.checkbox("Company Shares Asigned")

    if company_hist:
            st.markdown("<h1 style='text-align: center; color: #002966;'>Company Shares  Asigned </h1>", unsafe_allow_html=True)
            display_histo = company.major_holders
            display_mh = company.history(period='max')
            if display_histo.empty == True:
                st.write("No data available")
            else:
                st.write(display_histo)
    company_recomend = st.sidebar.checkbox("Stocks Recommendations")

    if company_recomend:
            st.markdown("<h1 style='text-align: center; color: #002966;'>Stocks Recommendatios</h1>", unsafe_allow_html=True)    
            display_recomend = company.recommendations
            if display_recomend.empty == True:
                st.write("No data available")
            else:
                st.write(display_recomend)
    company_job = st.sidebar.checkbox("Action and Split")

    if company_job:
        st.markdown("<h1 style='text-align: center; color: #002966;'>History Actions and Split</h1>", unsafe_allow_html=True)
        data = {}
        list = [(tickerSymbol2)]
        for ticker in list:
            ticker_object = yf.Ticker(ticker)
            temp = pd.DataFrame.from_dict(ticker_object.info, orient='index')
            temp.reset_index(inplace=True)
            temp.columns = ['Attribute', 'Recent']
            data[ticker] = temp
        merge = pd.concat(data)
        merge = merge.reset_index()
        del merge['level_1']
        merge.columns=['Ticker', 'Attribute', 'Recent'] 
        split=company.history(period='max', interval='1wk')
        st.sidebar.checkbox("Stock level")
        st.write('Company History', split)
    company_stadistic = st.sidebar.checkbox("Statistics")

    if company_stadistic:
        st.markdown("<h1 style='text-align: center; color: #002966;'>Statistics</h1>", unsafe_allow_html=True)
        data = yf.download((tickerSymbol2), start=start, end=None, group_by='tickers')
        st.table(data.describe())

    # Set up the Streamlit app title
    st.title('Stock Price Analysis Dashboard')

    # Sidebar for user input
    st.sidebar.header('User Input')
    ticker_input = st.sidebar.text_input('Enter Stock Ticker', value='AAPL')

    # Fetch and display data based on user input
    if ticker_input:
        data = yf.download(ticker_input, start='2020-01-01', end='2024-01-01')
        data['Daily Return'] = data['Adj Close'].pct_change()
        data['30 Day MA'] = data['Adj Close'].rolling(window=30).mean()
        data['100 Day MA'] = data['Adj Close'].rolling(window=100).mean()

        # Plotting the stock price and moving averages
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Adj Close'], mode='lines', name='Adjusted Close'))
        fig.add_trace(go.Scatter(x=data.index, y=data['30 Day MA'], mode='lines', name='30 Day MA'))
        fig.add_trace(go.Scatter(x=data.index, y=data['100 Day MA'], mode='lines', name='100 Day MA'))

        # Update layout of the figure
        fig.update_layout(title=f'{ticker_input} Stock Price and Moving Averages',
                        xaxis_title='Date',
                        yaxis_title='Price (USD)',
                        template='plotly_dark')

        # Display the figure in Streamlit
        st.plotly_chart(fig)

        # Show daily returns histogram
        st.subheader('Daily Returns Histogram')
        st.bar_chart(data['Daily Return'].dropna())
    

if __name__ == "__main__":
   main()
