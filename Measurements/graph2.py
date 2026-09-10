#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt
import math

# Density values (g/mL)
density = [0.993, 0.989, 0.991, 0.991, 0.990]

# Sample labels
samples = ["Sample 1", "Sample 2", "Sample 3", "Sample 4", "Sample 5"]

# Calculate the average
average = sum(density) / len(density)

# Calculate the sample standard deviation
squared_differences = []

for value in density:
    difference = value - average
    squared_differences.append(difference ** 2)

standard_deviation = math.sqrt(
    sum(squared_differences) / (len(density) - 1)
)

# Reference density
reference_density = 1.000

# Create the bar graph
plt.figure(figsize=(9, 6))

plt.bar(
    samples,
    density,
    yerr=standard_deviation,
    capsize=5,
    color="#FA86c4",
    edgecolor="black"
)

# Average line
plt.axhline(
    average,
    linestyle="--",
    linewidth=2,
    label=f"Average = {average:.3f} g/mL"
)

# Reference density line
plt.axhline(
    reference_density,
    linestyle="-",
    linewidth=2,
    label="Reference Density = 1.000 g/mL"
)

# Axis titles
plt.xlabel("Trials")
plt.ylabel("Density")
plt.ylabel("Density (g/mL)")

# Graph title
plt.title("Volumetric Pipette")

# Set the y-axis range
plt.ylim(0.90, 1.03)

# Add legend
plt.legend()

# Add grid
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Display the graph
plt.tight_layout()
plt.show()

# Print results
print("Average density:", round(average, 3), "g/mL")
print("Standard deviation:", round(standard_deviation, 4), "g/mL")
