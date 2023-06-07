import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


plt.style.use('ggplot')  # nice themes: bmh, ggplot,
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.plot(input_values, squares, linewidth=3)

# Defining the title and the axis label
ax.set_title("Random numbers")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of values", fontsize=14)


# Defining the size of the labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Defining the range of each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
