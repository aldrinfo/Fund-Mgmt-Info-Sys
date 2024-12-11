import pandas as pd
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the data
df = pd.read_csv('C:/Users/aldri/OneDrive/Documents/Python Projects/MIS Fundamentals/Project 2/my_flask_app/data/TableauSalesData.csv')

# Convert the 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y')

# Extract the year from the 'Order Date' column
df['Year'] = df['Order Date'].dt.year

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get all filter values
        category = request.form.get('category')
        sub_category = request.form.get('sub_category')
        region = request.form.get('region')
        segment = request.form.get('segment')
        query_type = request.form.get('query_type')

        # Apply filters to dataframe
        filtered_df = df.copy()
        if category:
            filtered_df = filtered_df[filtered_df['Category'] == category]
        if sub_category:
            filtered_df = filtered_df[filtered_df['Sub-Category'] == sub_category]
        if region:
            filtered_df = filtered_df[filtered_df['Region'] == region]
        if segment:
            filtered_df = filtered_df[filtered_df['Segment'] == segment]

        # Process different queries
        if query_type == 'total_sales_profit':
            results = {
                'Total Sales': f"${filtered_df['Sales'].sum():,.2f}",
                'Total Profit': f"${filtered_df['Profit'].sum():,.2f}"
            }
            
        elif query_type == 'avg_discount_product':
            results = filtered_df.groupby('Product Name')['Discount'].mean()\
                     .sort_values(ascending=False)\
                     .round(3)\
                     .reset_index()
            results['Discount'] = results['Discount'].map('{:.1%}'.format)
            
        elif query_type == 'sales_by_year':
            results = filtered_df.groupby('Year')['Sales'].sum()\
                     .reset_index()
            results['Sales'] = results['Sales'].map('${:,.2f}'.format)
            
        elif query_type == 'profit_by_region':
            results = filtered_df.groupby('Region')['Profit'].sum()\
                     .sort_values(ascending=False)\
                     .reset_index()
            results['Profit'] = results['Profit'].map('${:,.2f}'.format)
            
        elif query_type == 'negative_profit':
            results = filtered_df[filtered_df['Profit'] < 0][
                ['Product Name', 'Sales', 'Profit']
            ].sort_values('Profit')
            results['Sales'] = results['Sales'].map('${:,.2f}'.format)
            results['Profit'] = results['Profit'].map('${:,.2f}'.format)

    # Get unique values for filters
    categories = sorted(df['Category'].unique())
    sub_categories = sorted(df['Sub-Category'].unique())
    regions = sorted(df['Region'].unique())
    segments = sorted(df['Segment'].unique())

    return render_template('index.html',
                         categories=categories,
                         sub_categories=sub_categories,
                         regions=regions,
                         segments=segments,
                         results=results if 'results' in locals() else None,
                         query_type=request.form.get('query_type') if request.method == 'POST' else None)

if __name__ == '__main__':
    app.run(debug=True)
