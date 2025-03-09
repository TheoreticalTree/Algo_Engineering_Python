import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a DataFrame
df = pd.read_csv('output_topsort.csv')

# Ensure that the 'algorithm' column is treated as a categorical variable
algorithms = df['Algorithm'].unique()

# Set up a list of marker styles for each algorithm
markers = ['o', 's', '^', 'D', 'v']  # Circle, square, triangle, diamond, and inverted triangle

# Plot data
plt.figure(figsize=(10, 6))

for i, algorithm in enumerate(algorithms):
    # Filter data for the current algorithm
    subset = df[df['Algorithm'] == algorithm]
    
    # Plot with the algorithm-specific marker
    plt.scatter(subset['N'], subset['runtime'], label=algorithm,
                marker=markers[i % len(markers)], s=100)  # s=100 for marker size

# Labeling the axes
plt.xlabel('N')
plt.ylabel('runtime in ms')

# Add a title
plt.title('Runtime vs n for Different Algorithms')

# Show the legend
plt.legend(title='Algorithm')

# Show the plot
plt.grid(True)
plt.savefig('plot_topsort.png')
plt.show()
