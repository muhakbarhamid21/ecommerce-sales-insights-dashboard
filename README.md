# E-Commerce Sales Insights Dashboard

This project is part of the **Belajar Analisis Data dengan Python** course from the **Data Science** learning path at **Dicoding**. The main goal of this project is to apply data analysis techniques using Python to gain insights into eCommerce sales data. Through this project, various analyses such as sales trends, top product categories, RFM analysis, geoanalysis, and clustering are demonstrated using a public eCommerce dataset.

## Project Background

This project is part of the final assessment for the **Belajar Analisis Data dengan Python** course, which is part of the **Data Science** learning path at **Dicoding**. Throughout the course, several key topics in data analysis were covered, including:

- Fundamentals of Data Analysis
- Application of Descriptive Statistics
- Data Processing Considerations
- Data Wrangling
- Exploratory Data Analysis (EDA)
- Data Visualization
- Dashboard Development

For the final project, students are required to apply these skills by performing a complete data analysis process, from defining business questions to delivering insights through an interactive dashboard.

### Objectives of the Project

In this project, the goal is to:

1. **Analyze the dataset**: Perform an end-to-end data analysis using one of the provided datasets, which include:

   - Bike Sharing Dataset
   - **E-Commerce Public Dataset (selected)**
   - Air Quality Dataset

2. **Answer business questions**: Define at least two business questions and answer them through analysis. These questions should align with the topics covered in the **Defining Questions for Data Exploration** module.

3. **Create visualizations**: Provide at least two visualizations that help explain the results of the analysis. The visualizations should be relevant to the business questions being addressed.

4. **Develop a dashboard**: Create an interactive dashboard using **Streamlit** to present the results of the analysis. The dashboard must run smoothly and be accessible locally.

### Business Questions

The analysis for this project aims to uncover valuable insights by addressing the following key business questions:

1. **Which product categories are the top performers, and which ones are struggling?**  
   Understanding which categories are leading in sales and which are underperforming is crucial for strategic decision-making.

2. **What are the trends in monthly sales performance?**  
   By tracking sales over time, we can reveal seasonal trends and overall business performance throughout the year.

3. **Who are our most valuable customers based on RFM (Recency, Frequency, Monetary) Analysis?**

   - When was the last time our customers made a purchase?
   - How often are customers making repeat purchases in recent months?
   - Who are the top 5 big spenders, and how much are they contributing to revenue?

4. **Which states are driving the most sales, and where are we falling short?**  
   A geographic breakdown of sales helps identify which regions are the strongest contributors to the business and which regions may need further attention.

5. **What is the relationship between product price, shipping cost, and customer satisfaction (measured by review scores)?**  
   Through clustering analysis, we explore how pricing and shipping costs impact customer reviews, helping optimize pricing strategies and delivery costs.

### About this Project

For this specific project, the **E-Commerce Public Dataset** was selected. This dataset contains detailed information about eCommerce orders, including order status, payment information, customer details, product categories, and delivery timelines.

The following analyses were performed:

- **Sales Trend Analysis**: Examining the daily and monthly sales trends to uncover patterns in customer orders.
- **Top Product Categories**: Identifying the best and worst performing product categories in terms of quantity ordered.
- **RFM Analysis**: Segmenting customers based on their Recency, Frequency, and Monetary value.
- **Geoanalysis**: Analyzing total sales by state to understand regional sales performance.
- **Clustering Analysis**: Exploring the relationship between product price, freight cost, and review score to gain insights into customer satisfaction.

### Criteria for Completion

To successfully complete this project, the following criteria were met:

1. **Dataset Usage**: The project uses the **E-Commerce Public Dataset** to conduct the analysis.
2. **Complete Data Analysis Process**: All steps of the data analysis process were followed, from defining business questions to drawing conclusions.
3. **Well-documented Notebook**: The analysis was performed in a clear and organized manner, following the provided notebook template.
4. **Interactive Dashboard**: A simple, interactive dashboard was built using **Streamlit** to present the results, allowing users to explore the data through visualizations and insights.

Upon completion, the project will be reviewed by the Dicoding team to ensure that all requirements have been fulfilled.

## Features

- **Sales Trend Analysis**: Daily and monthly sales charts.
- **Top Product Categories**: Visualization of the top 5 best and worst product categories.
- **RFM Analysis**: Recency, Frequency, and Monetary analysis to identify key customers.
- **Geoanalysis**: Total sales by customer state.
- **Clustering Analysis**: Relationship between product price, freight cost, and review score.

## Dataset Source

The dataset used in this analysis is publicly available from the following sources:

- [Kaggle: Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- [Google Drive Link](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view)

## Requirements

To run the dashboard, you need the following Python libraries installed:

- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Streamlit**
- **Babel**

## Installation Guide

### 1. Clone or Download the Repository

First, you need to clone the repository or download the code files:

```bash
git clone https://github.com/muhakbarhamid21/ecommerce-sales-insights-dashboard
```

Alternatively, download the ZIP file from the repository and extract it to your desired location.

### 2. Create a Virtual Environment (Optional but Recommended)

To avoid conflicts with other Python projects, it is recommended to create a virtual environment for this project:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Once the virtual environment is created, you need to activate it:

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
.\venv\Scripts\activate
```

### 4. Install the Required Dependencies

Install the necessary Python libraries by running:

```bash
pip install -r requirements.txt
```

This will automatically install all required packages (streamlit, pandas, plotly, matplotlib, seaborn).

### 5. Running the Streamlit Dashboard

Now, run the Streamlit application by executing the following command:

```bash
streamlit run dashboard/app.py
```

### 6. Access the Dashboard

Once the app is running, a new tab will automatically open in your web browser. If it does not open automatically, you can manually navigate to the following address in your browser:

```bash
http://localhost:8501
```

## Contributing

Contributions to this project are welcome! Feel free to fork the repository, submit pull requests, or open issues to improve the dashboard or analysis. I am open to suggestions and collaboration to make this project even more insightful and user-friendly.

## Explore and Expand

This project serves as a foundation for deeper exploration into e-commerce data analytics. I encourage you to experiment with additional datasets, refine the visualizations, or expand the dashboard with new features such as predictive analytics or customer segmentation.

Thank you for checking out this project! I hope you find valuable insights and inspiration as you interact with the **E-Commerce Sales Insights Dashboard**.
