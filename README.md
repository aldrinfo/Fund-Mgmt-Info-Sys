# Interactive Web Application for Superstore Data Analysis

## Overview
This project is an interactive web application built using Flask, Pandas, and HTML. It allows users to filter data from a Superstore dataset based on various criteria and execute predefined queries. The application provides insights such as total sales, profit, and discount information through user-friendly web interfaces.

The project integrates core web development, data manipulation, and visualization concepts, offering hands-on experience with real-world tools and technologies.

## Features
- **Dynamic Filtering**: Users can filter data by Category, Sub-Category, Region, and Segment through dropdown menus populated dynamically from the dataset.
- **Predefined Queries**:
  1. Total Sales and Profit: Calculates the sum of sales and profit for the filtered data.
  2. Average Discount by Product: Computes the average discount for each product in the selected subset, sorted in descending order.
  3. Total Sales by Year: Groups data by year and calculates total sales.
  4. Profit by Region: Groups data by region and calculates total profit.
  5. Products with Negative Profit: Displays products with negative profit in the filtered subset.
- **Interactive Results**: Filtered results and query outputs are displayed on the same page, formatted for readability.

## Learning Objectives
By completing this project, you will:
- Gain experience in web application development using Flask.
- Practice data manipulation and analysis using Pandas.
- Learn to connect front-end forms with back-end query processing.
- Develop debugging, code structuring, and user interface creation skills.
- Enhance your coding abilities with AI tools for problem-solving and optimization.

## Project Structure
```
my_flask_app/
├── app.py                   # Main Flask application
├── templates/
│   └── index.html           # HTML form and results page
├── static/
│   └── style.css            # CSS styles for the application
└── data/
    └── superstore_sales.csv # Dataset for analysis
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd my_flask_app
   ```
2. Install dependencies:
   ```bash
   pip install flask pandas
   ```
3. Place the `superstore_sales.csv` dataset in the `data/` directory.

## Running the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. **Select Filters**:
   - Use dropdown menus to filter data by Category, Sub-Category, Region, and Segment.
2. **Choose a Query**:
   - Select one of the predefined queries from the dropdown menu.
3. **View Results**:
   - The filtered results will be displayed on the same page after submission.

## Technologies Used
- **Flask**: Backend web framework.
- **Pandas**: Data manipulation and analysis.
- **HTML & CSS**: Front-end user interface design.

## Example Queries
1. **Total Sales and Profit**:
   - Input: `Furniture`, `Chairs`, `West`, `Consumer`.
   - Output: Total sales = $5,000, Total profit = $1,200.

2. **Average Discount by Product**:
   - Input: `Technology`, `Phones`, `Central`, `Corporate`.
   - Output: Sorted average discounts for products.

3. **Products with Negative Profit**:
   - Input: `Office Supplies`, `Paper`, `East`, `Home Office`.
   - Output: List of products with negative profit.

## Contribution
Feel free to contribute to this project by:
- Reporting bugs or issues.
- Suggesting new features or enhancements.
- Submitting pull requests.

## Reflection
This project encouraged the use of AI tools to assist with coding and debugging. GPT was used to:
- Generate initial Flask setup and routing code.
- Debug errors in query logic and improve efficiency.
- Suggest enhancements for user interface design.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
