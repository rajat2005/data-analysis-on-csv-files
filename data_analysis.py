
import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales_data(csv_file="sales_data.csv"):
    try:
        df = pd.read_csv(csv_file)
        print(f"Successfully loaded {csv_file}")
        print("DataFrame head:")
        print(df.head())

        # Example analysis: Total sales by product
        if 'Product' in df.columns and 'Sales' in df.columns:
            sales_by_product = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
            print("\nTotal Sales by Product:")
            print(sales_by_product)

            # Generate a bar chart
            plt.figure(figsize=(10, 6))
            sales_by_product.plot(kind='bar')
            plt.title('Total Sales by Product')
            plt.xlabel('Product')
            plt.ylabel('Total Sales')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plot_filename = 'sales_by_product.png'
            plt.savefig(plot_filename)
            print(f"Generated plot: {plot_filename}")
        else:
            print("DataFrame must contain 'Product' and 'Sales' columns for this analysis.")

        # Example analysis: Monthly sales trend (assuming a 'Date' column)
        if 'Date' in df.columns and 'Sales' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            df['Month'] = df['Date'].dt.to_period('M')
            monthly_sales = df.groupby('Month')['Sales'].sum()
            print("\nMonthly Sales Trend:")
            print(monthly_sales)

            plt.figure(figsize=(12, 6))
            monthly_sales.plot(kind='line', marker='o')
            plt.title('Monthly Sales Trend')
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.grid(True)
            plt.tight_layout()
            plot_filename_monthly = 'monthly_sales_trend.png'
            plt.savefig(plot_filename_monthly)
            print(f"Generated plot: {plot_filename_monthly}")
        else:
            print("DataFrame must contain 'Date' and 'Sales' columns for monthly trend analysis.")

    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
        print("Please create a 'sales_data.csv' file with 'Product', 'Sales', and 'Date' columns.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create a dummy sales_data.csv for demonstration if it doesn't exist
    if not os.path.exists("sales_data.csv"):
        data = {
            'Date': pd.to_datetime(['2023-01-10', '2023-01-15', '2023-02-01', '2023-02-20', '2023-03-05', '2023-03-10']),
            'Product': ['A', 'B', 'A', 'C', 'B', 'A'],
            'Sales': [100, 150, 120, 200, 180, 130]
        }
        dummy_df = pd.DataFrame(data)
        dummy_df.to_csv("sales_data.csv", index=False)
        print("Created a dummy sales_data.csv for demonstration.")

    analyze_sales_data("sales_data.csv")


