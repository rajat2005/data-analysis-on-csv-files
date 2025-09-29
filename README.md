# Data Analysis on CSV Files

This Python script performs basic data analysis on sales data from a CSV file using the Pandas library and generates visualizations with Matplotlib.

## Features

- Loads sales data from a `sales_data.csv` file.
- Calculates and displays total sales by product.
- Generates a bar chart for sales by product.
- Calculates and displays monthly sales trends (requires a 'Date' column).
- Generates a line chart for monthly sales trends.
- Creates a dummy `sales_data.csv` if one doesn't exist for demonstration purposes.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install pandas matplotlib
    ```
2.  **Save the code** as `data_analysis.py`.
3.  **Prepare your data:** Ensure you have a `sales_data.csv` file in the same directory with at least 'Product', 'Sales', and optionally 'Date' columns. A dummy file will be created if it doesn't exist.
4.  **Run the script** from your terminal:
    ```bash
    python data_analysis.py
    ```

## Files

-   `data_analysis.py`: The main Python script for data analysis.
-   `sales_data.csv`: (Optional, dummy created if not present) The input CSV file containing sales data.
-   `sales_by_product.png`: (Automatically generated) Bar chart showing total sales by product.
-   `monthly_sales_trend.png`: (Automatically generated) Line chart showing monthly sales trend.

