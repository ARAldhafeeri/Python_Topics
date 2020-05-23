import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot(squares)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis= 'both', labelsize=14)
plt.style.use('ggplot')
plt.show()

# plt.style.available
"""

['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast',
'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep',
 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel',
 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
 'seaborn-whitegrid', 'tableau-colorblind10']

"""
