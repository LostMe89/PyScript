import pandas as pd
import matplotlib.pyplot as plt

def generate_performance_report(csv_file, output_folder):
    """
    Reads a CSV file and generates graphs for performance metrics.

    Parameters:
        csv_file (str): Path to the CSV file containing performance data.
        output_folder (str): Folder where the graphs will be saved.
    """
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(csv_file)

        # Check if the necessary columns are present
        required_columns = ['GPU temperature', 'Memory usage', 'Power percent', 'RAM usage', 'Framerate']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Column '{column}' not found in CSV file.")

        # Plot each metric
        metrics = {
            'GPU temperature': 'GPU Temperature (°C)',
            'Memory usage': 'Memory Usage (MB)',
            'Power percent': 'Power Usage (%)',
            'RAM usage': 'RAM Usage (MB)',
            'Framerate': 'Framerate (FPS)'
        }

        for metric, label in metrics.items():
            plt.figure(figsize=(10, 6))
            plt.plot(data.index, data[metric], label=label, color='blue')
            plt.title(f"{label} Over Time", fontsize=14)
            plt.xlabel("Sample Index", fontsize=12)
            plt.ylabel(label, fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.legend()
            plt.tight_layout()

            # Save the plot
            output_path = f"{output_folder}/{metric.replace(' ', '_').lower()}.png"
            plt.savefig(output_path)
            plt.close()

            print(f"Graph saved: {output_path}")

        print("All graphs have been successfully generated.")

    except Exception as e:
        print(f"An error occurred: {e}")


generate_performance_report("PerformanceWorldOfTanksMainMenu.csv", "./outputMM") # change .csv file to other form foler to create new grapsh, also change name of foler where output will be created
