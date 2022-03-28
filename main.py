import matplotlib.pyplot as plt
x_axis_coords=[1, 2, 3, 4, 5, 6, 7] #day in the week
y_axis_coords=[2, 2, 1, 1, 0, 0, 0] #how many lessons per day
y_axis_coords2=[1, 0, 2, 0, 0, 0, 0] #sports
plt.style.use("seaborn-pastel")
plt.plot(x_axis_coords, y_axis_coords, label="Math lessons")
plt.plot(x_axis_coords, y_axis_coords2, label="Sport lessons")
plt.xlabel("Day of the week")
plt.ylabel("Lessons per day")
plt.title("Lessons in a week")
plt.legend(loc="upper right")

plt.show()



