import matplotlib.pyplot as plt

x_values = range(0,1000)
y_values = [x**2 for x in x_values]

ax,fig = plt.subplots()
plt.style.use('seaborn')
plt.scatter(x_values, y_values, s=10)
plt.axis([0,1100, 0,110000])
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
