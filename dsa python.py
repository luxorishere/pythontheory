import matplotlib.pyplot as plt

# Complex dataset
categories = ['A', 'B', 'C', 'D']
values1 = [10, 15, 7, 12]
values2 = [8, 12, 6, 10]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot two sets of bars
bar_width = 0.35
fig, ax = plt.subplots()

bar1 = ax.bar(categories, values1, bar_width, label='Set 1')
# Create a figure and axis

# Calculate the x positions for the second set of bars
x_positions = [x + bar_width for x in range(len(categories))]

# Plot the second set of bars
bar2 = ax.bar(x_positions, values2, bar_width, label='Set 2')
# Add labels, title, and legend
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Comparison of Two Sets of Data')
plt.xticks([x + bar_width/2 for x in categories], categories)
plt.legend()

# Display the graph
plt.show()