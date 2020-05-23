import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(2,4, s=200)
x_values = [1,2,3,4,5]
y_values = [1,2,3,4,5]
ax.scatter(x_values, y_values, s= 100)
ax.set_title("hellow world", fontsize=14)
ax.set_xlabel('x axis', fontsize=14)
ax.set_ylabel('y axis', fontsize=14)


# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
