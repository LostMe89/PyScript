import pandas as pd
import matplotlib.pyplot as plt

def analyze_performance_metrics(csv_file, output_folder):
    """
    Reads a CSV file and calculates the min, max, and average values for performance metrics,
    and generates bar charts for the summary statistics. Excludes metrics where all values are zero.

    Parameters:
        csv_file (str): Path to the CSV file containing performance data.
        output_folder (str): Folder where the charts will be saved.

    Returns:
        dict: A dictionary with min, max, and average values for each metric.
    """
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(csv_file)

        # Check if the necessary columns are present
        required_columns = ['GPU temperature', 'Memory usage', 'Power percent', 'RAM usage', 'Framerate']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Column '{column}' not found in CSV file.")

        # Calculate min, max, and average for each column, excluding metrics where all values are zero
        stats = {}
        for column in required_columns:
            if data[column].sum() != 0:  # Exclude columns where all values are zero  
                if column == 'Framerate':
                    # Find the first non-zero value for min in Framerate
                    non_zero_values = data[column][data[column] > 0]
                    min_value = non_zero_values.min() if not non_zero_values.empty else 0
                else:
                    min_value = data[column].min()

                stats[column] = {
                    'min': min_value,
                    'max': data[column].max(),
                    'avg': data[column].mean()
                }

        # Generate bar charts for summary statistics
        for column, values in stats.items():
            metrics = ['min', 'max', 'avg']
            chart_values = [values[metric] for metric in metrics]

            plt.figure(figsize=(8, 5))
            bars = plt.bar(metrics, chart_values, color=['blue', 'green', 'orange'])
            plt.title(f"{column} Summary", fontsize=14)
            plt.xlabel("Metrics", fontsize=12)
            plt.ylabel("Values", fontsize=12)
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            # Add text on top of each bar to show the values
            for i, bar in enumerate(bars):
                plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,  # Position above the bar
                         f"{chart_values[i]:.2f}", ha='center', va='bottom', fontsize=12)

            # Save the plot
            output_path = f"{output_folder}/{column.replace(' ', '_').lower()}_summary.png"
            plt.savefig(output_path)
            plt.close()

            print(f"Chart saved: {output_path}")

        return stats

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
stats = analyze_performance_metrics("PerformanceWorldOfTanksMainMenu.csv", "./outputMM")   # change .csv file to other form foler to create new grapsh, also change name of foler where output will be created
if stats:
    for metric, values in stats.items():
        print(f"{metric} -> Min: {values['min']}, Max: {values['max']}, Avg: {values['avg']:.2f}")