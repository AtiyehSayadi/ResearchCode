import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


#gp_max

#data=[27, 10, 7, 11, 9, 14, 17, 12, 16, 23, 12, 19, 14, 21, 15, 15, 13, 13, 25, 25, 9, 36, 10, 14, 28, 14, 14, 5, 18, 18, 22, 50, 43, 14, 22, 42, 8, 34, 22, 44, 12, 8, 3, 28, 12, 93, 24, 9, 18, 18, 4, 78, 102, 14, 85, 3, 59, 18, 20, 21, 5, 26, 5, 10, 20, 9, 15, 10, 88, 16, 16, 12, 4, 12, 15, 17, 29, 15, 3, 45, 22, 44, 27, 19, 14, 45, 14, 54, 9, 13, 6, 41, 11, 12, 6, 18, 24, 16, 12, 8]
#refined
#data=[25, 10, 7, 8, 8, 10, 22, 16, 12, 21, 11, 15, 16, 22, 11, 14, 12, 11, 24, 22, 10, 36, 8, 14, 22, 11, 10, 5, 16, 13, 19, 28, 35, 14, 18, 22, 7, 55, 17, 41, 13, 9, 3, 21, 9, 58, 24, 8, 16, 14, 4, 53, 64, 12, 47, 3, 52, 18, 20, 10, 6, 16, 5, 10, 11, 8, 15, 10, 58, 13, 21, 10, 3, 11, 14, 13, 32, 11, 3, 29, 18, 37, 20, 14, 15, 33, 14, 44, 9, 10, 5, 23, 11, 13, 7, 10, 14, 17, 11, 8]
#number of equal=0
#near to equal=2
#

#gp_random
#data=[55, 25, 27, 18, 32, 28, 25, 41, 28, 38, 60, 31, 131, 94, 20, 30, 37, 67, 60, 54, 21, 63, 23, 46, 21, 35, 23, 8, 31, 16, 58, 66, 59, 33, 73, 75, 12, 175, 54, 122, 35, 14, 3, 73, 43, 93, 37, 21, 50, 27, 6, 124, 200, 194, 81, 4, 98, 84, 46, 18, 11, 64, 8, 22, 45, 29, 52, 30, 200, 47, 56, 39, 9, 30, 32, 35, 200, 35, 2, 42, 41, 155, 64, 61, 25, 40, 89, 127, 20, 16, 14, 65, 33, 27, 11, 35, 36, 48, 20, 26]
#refined
data=[66, 33, 18, 18, 22, 20, 25, 85, 20, 26, 31, 33, 41, 44, 20, 28, 24, 24, 48, 32, 14, 56, 25, 29, 37, 24, 26, 10, 32, 15, 47, 37, 124, 29, 53, 54, 19, 54, 53, 198, 19, 11, 5, 35, 29, 101, 27, 11, 28, 26, 6, 56, 186, 43, 101, 3, 121, 40, 36, 31, 8, 57, 9, 25, 41, 27, 38, 30, 190, 39, 139, 37, 10, 29, 42, 20, 49, 14, 3, 39, 28, 41, 59, 31, 25, 61, 78, 82, 14, 21, 16, 50, 38, 21, 11, 35, 26, 31, 23, 29]
#number of equal= 0
#near to equal=4


#to number
#data=[23, 16, 16, 19, 19, 18, 21, 17, 20, 20, 22, 20, 24, 22, 23, 16, 19, 21, 22, 21, 16, 27, 25, 21, 17, 18, 18, 14, 22, 18, 26, 20, 24, 22, 20, 21, 15, 26, 23, 30, 17, 10, 8, 23, 21, 31, 19, 18, 21, 18, 12, 30, 24, 16, 27, 10, 26, 25, 23, 18, 12, 23, 13, 18, 21, 17, 21, 19, 25, 23, 23, 20, 11, 17, 18, 24, 27, 17, 11, 25, 23, 24, 19, 20, 14, 24, 22, 24, 14, 19, 15, 26, 20, 15, 18, 17, 17, 18, 20, 17]
#number of equal=0
#near to equal=12


#inconsistency
# data=[16, 24, 16, 12, 12, 17, 17, 15, 16, 17, 19, 19, 19, 14, 22, 17, 12, 15, 18, 20, 20, 22, 26, 22, 17, 20, 16, 7, 17, 13, 27, 16, 21, 21, 24, 18, 10, 22, 23, 27, 21, 8, 15, 17, 16, 23, 15, 14, 18, 15, 14, 23, 17, 12, 24, 14, 21, 15, 22, 13, 17, 24, 7, 17, 24, 14, 22, 14, 17, 14, 20, 16, 6, 23, 14, 21, 23, 11, 11, 18, 14, 23, 21, 17, 11, 18, 25, 18, 8, 12, 8, 24, 21, 21, 8, 11, 14, 17, 17, 12]
#number of equal=0
#near to equal=70
# Count the occurrences of each value
# value_counts = Counter(data)

# # Prepare data for plotting
# values = list(value_counts.keys())
# counts = list(value_counts.values())
# plt.figure(figsize=(7, 4)) 

# # Create a bar plot
# plt.bar(values, counts, color='blue', alpha=0.7,  width=0.1)

# # Add labels and title
# plt.xlabel('\nThe Number of Generations', fontdict={'fontsize': 17, 'fontweight': 'bold', 'fontname': 'DejaVu Serif'})
# plt.ylabel('The Number of Matrices', fontdict={'fontsize': 17, 'fontweight': 'bold', 'fontname': 'DejaVu Serif'})
# plt.yticks(fontsize=13, fontname= 'DejaVu Serif',fontweight= 'bold')
# plt.xticks(fontsize=7,fontname= 'DejaVu Serif', fontweight= 'bold')

# # Customize the title with bold font, larger size, and a specific font
# plt.title('Distribution of Matrices to Achieve Consistency\n by the Number of Generations\n', 
#           fontdict={'fontsize': 22, 'fontweight': 'bold', 'fontname': 'DejaVu Serif'})
# plt.xlim(min(values) - 0.5, max(values) + 0.5)

# # Show the plot
# plt.xticks(values)  # Ensure all x-ticks are shown
# plt.show()

# 
# 
# 
# 
# 

bin_edges = list(range(1, 201, 5))  # 1, 6, 11, ..., 196

# Get histogram counts
counts, _ = np.histogram(data, bins=bin_edges)

# Create range labels
labels = [f"{bin_edges[i]}–{bin_edges[i+1]-1}" for i in range(len(bin_edges)-1)]

# Filter out bins with zero counts
filtered_labels = [labels[i] for i, c in enumerate(counts) if c > 0]
filtered_counts = [c for c in counts if c > 0]

# Plot only the non-zero bins
plt.figure(figsize=(12, 5))
plt.bar(filtered_labels, filtered_counts, color='skyblue', alpha=0.8)

# Formatting
plt.xlabel('\nRange of Number of Generations', fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.ylabel('Number of Matrices', fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.title('Distribution of Matrices by Generation Ranges\n', fontdict={'fontsize': 20, 'fontweight': 'bold'})
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=12)
plt.tight_layout()

plt.show()
# 
# 
# 
# 
# algorithms = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Refined Version of Algorithm 3']
# percentages = [70, 12, 4, 2]  # Replace with your real values

# # Plot
# plt.figure(figsize=(8, 5))
# bars = plt.bar(algorithms, percentages, color=['steelblue', 'orange', 'green', 'purple'], alpha=0.8)

# # Add value labels on top of each bar
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

# # Labels and formatting
# plt.ylabel('% of Matrices with ≥50% "≈"', fontsize=14, fontweight='bold')
# plt.title('Comparison of Algorithms by Indifference Dominance', fontsize=16, fontweight='bold')
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.ylim(0, 100)
# plt.tight_layout()
# plt.grid(axis='y', linestyle='--', alpha=0.4)

# plt.show()