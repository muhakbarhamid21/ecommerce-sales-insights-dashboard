import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Function to load data from CSV and convert specific columns to datetime format
def load_data():
    """
    Load and preprocess the data from a CSV file.
    
    Returns:
        DataFrame: Processed DataFrame with datetime columns.
    """
    df = pd.read_csv('./data/all_data.csv')
    date_columns = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
                    'order_delivered_customer_date', 'order_estimated_delivery_date']
    for column in date_columns:
        df[column] = pd.to_datetime(df[column])
    return df


# Function to create a daily orders dataframe based on purchase timestamp
def create_daily_orders(df):
    """
    Create a DataFrame that aggregates the number of unique orders and total payment
    values on a daily basis.
    
    Args:
        df (DataFrame): The input DataFrame.
    
    Returns:
        DataFrame: Aggregated daily order data.
    """
    daily_orders = df.resample(rule='D', on='order_purchase_timestamp').agg({
        'order_id': 'nunique',
        'payment_value': 'sum'
    }).reset_index()
    return daily_orders


# Function to create a monthly orders dataframe based on purchase timestamp
def create_monthly_orders(df):
    """
    Create a DataFrame that aggregates the number of unique orders and total payment
    values on a monthly basis.
    
    Args:
        df (DataFrame): The input DataFrame.
    
    Returns:
        DataFrame: Aggregated monthly order data.
    """
    monthly_orders = df.resample(rule='M', on='order_purchase_timestamp').agg({
        'order_id': 'nunique',
        'payment_value': 'sum'
    }).reset_index()
    return monthly_orders


# Function to create sidebar filters in Streamlit for date range and order status
def create_sidebar(df):
    """
    Create sidebar filters for date range and order status selection in the Streamlit app.
    
    Args:
        df (DataFrame): The input DataFrame containing order data.
    
    Returns:
        Tuple: The start date, end date, and selected order status from user input.
    """
    with st.sidebar:
        min_date = df['order_purchase_timestamp'].min().date()
        max_date = df['order_purchase_timestamp'].max().date()

        # Date input for selecting a date range
        start_date, end_date = st.date_input(
            label='Date Range', min_value=min_date, max_value=max_date,
            value=[min_date, max_date]
        )

        # Radio button for selecting order status
        order_status = ['ALL'] + list(df['order_status'].unique())
        selected_status = st.radio('Select Order Status: ', order_status)

    return start_date, end_date, selected_status


# Function to filter data based on the selected date range and order status
def filter_data(df, start_date, end_date, selected_status):
    """
    Filter the data based on the selected date range and order status.
    
    Args:
        df (DataFrame): The input DataFrame to be filtered.
        start_date (datetime.date): The start date for filtering.
        end_date (datetime.date): The end date for filtering.
        selected_status (str): The selected order status to filter.
    
    Returns:
        DataFrame: The filtered DataFrame based on user input.
    """
    filtered_df = df[(df["order_purchase_timestamp"].dt.date >= start_date) &
                     (df["order_purchase_timestamp"].dt.date <= end_date)]

    if selected_status != 'ALL':
        filtered_df = filtered_df[filtered_df['order_status'] == selected_status]

    return filtered_df


# Function to create a dataframe for best and worst performing product categories
def create_best_worst_categories(df):
    """
    Create a DataFrame that aggregates the total quantity ordered for each product category.
    
    Args:
        df (DataFrame): The input DataFrame.
    
    Returns:
        DataFrame: Aggregated product category data sorted by quantity ordered.
    """
    category_summary = df.groupby('product_category_name_english')['qty_order'].sum().reset_index()
    return category_summary


# Function for RFM Analysis
def create_rfm_analysis(df):
    """
    Perform Recency, Frequency, and Monetary (RFM) analysis on the customer data.
    
    Args:
        df (DataFrame): The input DataFrame.
    
    Returns:
        DataFrame: RFM analysis results with customer IDs and their corresponding RFM values.
    """
    now = df['order_purchase_timestamp'].max()
    rfm_df = df.groupby('customer_id').agg({
        'order_purchase_timestamp': lambda x: (now - x.max()).days,
        'order_id': 'count',
        'payment_value': 'sum'
    }).reset_index()

    rfm_df.columns = ['customer_id', 'recency', 'frequency', 'monetary']
    rfm_df['numeric_id'] = pd.factorize(rfm_df['customer_id'])[0] + 1
    return rfm_df


# Function for geographical analysis of sales
def create_geoanalysis(df):
    """
    Perform geographical analysis by aggregating total sales based on customer state.
    
    Args:
        df (DataFrame): The input DataFrame.
    
    Returns:
        DataFrame: Sales data aggregated by customer state.
    """
    sales_by_state = df.groupby('customer_state')['payment_value'].sum().sort_values(ascending=True)
    return sales_by_state


# Function to display a monthly sales chart
def display_monthly_sales(df):
    """
    Generate and display a monthly sales chart in the Streamlit app.
    
    Args:
        df (DataFrame): The input DataFrame containing the order data.
    """
    monthly_orders = create_monthly_orders(df)
    st.subheader('Monthly Sales Chart')

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly_orders['order_purchase_timestamp'], monthly_orders['order_id'])
    plt.title('Monthly Sales Count')
    plt.xlabel('Date')
    plt.ylabel('Sales Count (R$)')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x, 'BRL', locale='pt_BR')))

    st.pyplot(fig)


# Function to display a daily sales chart
def display_daily_sales(df):
    """
    Generate and display a daily sales chart in the Streamlit app.
    
    Args:
        df (DataFrame): The input DataFrame containing the order data.
    """
    daily_orders = create_daily_orders(df)
    st.subheader('Daily Sales Chart')

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(daily_orders['order_purchase_timestamp'], daily_orders['order_id'])
    plt.title('Daily Sales Count')
    plt.xlabel('Date')
    plt.ylabel('Sales Count')

    st.pyplot(fig)


# Function to display top 5 best and worst product categories
def display_best_worst_categories(df):
    """
    Generate and display bar charts showing the top 5 best and worst product categories based on quantity ordered.
    
    Args:
        df (DataFrame): The input DataFrame containing product category data.
    """
    category_summary = create_best_worst_categories(df)

    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(16, 12))
    colors = ["#72BCD4"] * 5

    sns.barplot(x='qty_order', y='product_category_name_english',
                data=category_summary.sort_values(by='qty_order', ascending=False).head(5),
                palette=colors, ax=ax[0])
    ax[0].set_title('Top 5 Best-Selling Categories', fontsize=15)

    sns.barplot(x='qty_order', y='product_category_name_english',
                data=category_summary.sort_values(by='qty_order', ascending=True).head(5),
                palette=colors, ax=ax[1])
    ax[1].set_title('Top 5 Worst-Selling Categories', fontsize=15)

    st.subheader('Top 5 Best and Worst-Selling Categories by Quantity Ordered')
    st.pyplot(fig)


# Function to display RFM analysis charts
def display_rfm_analysis(df):
    """
    Generate and display RFM analysis charts showing the top 5 customers for each RFM metric.
    
    Args:
        df (DataFrame): The input DataFrame containing RFM analysis data.
    """
    rfm_df = create_rfm_analysis(df)

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))
    colors = ['#72BCD4'] * 5

    sns.barplot(y="recency", x='numeric_id', data=rfm_df.sort_values(by='recency', ascending=True).head(5), palette=colors, ax=ax[0])
    ax[0].set_title('Recency (days)', fontsize=18)

    sns.barplot(y='frequency', x='numeric_id', data=rfm_df.sort_values(by='frequency', ascending=False).head(5), palette=colors, ax=ax[1])
    ax[1].set_title('Purchase Frequency', fontsize=18)

    sns.barplot(y='monetary', x='numeric_id', data=rfm_df.sort_values(by='monetary', ascending=False).head(5), palette=colors, ax=ax[2])
    ax[2].set_title('Total Monetary Value', fontsize=18)
    ax[2].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x, 'BRL', locale='pt_BR')))

    st.subheader('Best Customers Based on RFM Analysis')
    st.pyplot(fig)


# Function to display geographical sales analysis
def display_geoanalysis(df):
    """
    Generate and display a bar chart showing total sales by customer state.
    
    Args:
        df (DataFrame): The input DataFrame containing geographical sales data.
    """
    sales_by_state = create_geoanalysis(df)
    st.subheader('Sales by State')

    fig, ax = plt.subplots(figsize=(12, 6))
    sales_by_state.plot(kind='barh', ax=ax)
    plt.title('Sales by State')
    plt.ylabel('State')
    plt.xlabel('Total Sales')
    plt.tight_layout()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x, 'BRL', locale='pt_BR')))

    st.pyplot(fig)


# Function to display clustering analysis based on price, freight, and review score
def display_clustering(df):
    """
    Generate and display a scatter plot showing the relationship between product price, freight cost, and review score.
    
    Args:
        df (DataFrame): The input DataFrame containing product and review data.
    """
    st.subheader('Relationship between Price, Freight Cost, and Review Score')

    fig, ax = plt.subplots(figsize=(14, 8))
    scatter = ax.scatter(df['price'], df['freight_value'], c=df['review_score'], cmap='viridis', alpha=0.5)
    plt.colorbar(scatter, label='Review Score')

    plt.xlabel('Product Price')
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x, 'BRL', locale='pt_BR')))
    plt.ylabel('Freight Cost')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format_currency(x, 'BRL', locale='pt_BR')))

    plt.title('Price vs Freight Cost vs Review Score')
    st.pyplot(fig)


# Function to display order statistics
def display_order_stats(df):
    """
    Display total orders and total revenue as metrics in Streamlit.
    
    Args:
        df (DataFrame): The input DataFrame containing order data.
    """
    col1, col2 = st.columns(2)

    total_orders = df['order_id'].nunique()
    total_revenue = df['payment_value'].sum()

    with col1:
        st.metric('Total Orders', total_orders)

    with col2:
        formatted_revenue = format_currency(total_revenue, 'BRL', locale='pt_BR')
        st.metric('Total Revenue', formatted_revenue)


# Function to display order status visualization
def display_order_status_viz(df):
    """
    Generate and display a bar chart showing the number of orders by status.
    
    Args:
        df (DataFrame): The input DataFrame containing order status data.
    """
    st.subheader('Orders by Status')
    order_count = df['order_status'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    order_count.plot(kind='bar', ax=ax)
    plt.title('Orders by Status')
    plt.xlabel('Order Status')
    plt.ylabel('Order Count')
    st.pyplot(fig)


# Function to display raw order data
def display_order_data(df):
    """
    Display the raw order data in a Streamlit table.
    
    Args:
        df (DataFrame): The input DataFrame containing order data.
    """
    st.subheader('Order Data')
    st.dataframe(df)


# Main function to orchestrate the Streamlit app
def main():
    """
    Main function that loads data, applies filters, and displays various visualizations
    for order analysis in the Streamlit app.
    """
    st.title('Order Data Analysis')

    # Load data
    all_data = load_data()

    # Sidebar filters
    start_date, end_date, selected_status = create_sidebar(all_data)

    # Filter data based on user input
    filtered_data = filter_data(all_data, start_date, end_date, selected_status)

    # Visualization and analysis
    st.subheader(f'Data Visualization for Status: {selected_status}')
    display_order_stats(filtered_data)
    display_monthly_sales(filtered_data)
    display_daily_sales(filtered_data)
    display_best_worst_categories(filtered_data)
    display_rfm_analysis(filtered_data)
    display_order_status_viz(filtered_data)
    display_geoanalysis(filtered_data)
    display_clustering(filtered_data)
    display_order_data(filtered_data)


# Run the main function when script is executed
if __name__ == "__main__":
    main()
