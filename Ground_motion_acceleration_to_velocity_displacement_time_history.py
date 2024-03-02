import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('kocaeli.csv')
acc = data.acc_g  # acceleration: g
a = acc * 981  # acceleration: cm/s^2


# Calculate the consecutive time step between the time data
dt = data.t[1] - data.t[0]

# Velocity Time History
v = np.cumsum(a) * dt  # Unit of velocity: cm/sec

# Displacement Time History
d = np.cumsum(v) * dt  # Unit of displacement: cm

# Plotting the figure and parameter specifies width and height of the figure in inches
plt.figure(figsize=(8, 8))

# Plot acceleration
# Subplot grid with 3 rows, 1column and selecting first index of subplot for plotting the acceleration time history 
plt.subplot(3,1,1) 
# Plotting the acceleration against time with blue colour adjusting the thickness of line to be of 1 point
plt.plot(data.t, acc, 'b',linewidth=1 )
# Setting the label for the x and y-axis and its font size 
plt.xlabel('Time/s', fontsize=15)
plt.ylabel('Acceleration(g)', fontsize=15)
# Setting the limit for the x and y-axis 
plt.xlim(0,28)
plt.ylim(-0.5,0.4)
# Calculating the index of maximum absolute value of acceleration
# Absolute value of all the element considering the both positive and negative values are determined then index of the maximum absolute acceleration value is stored which is later used to annotate the plot with maximum acceleration value 
max_acc_index = np.argmax(np.abs(acc))
# Scatter plot point to the aceleration subplot at the time corresponding to the maximum value is plotted marked by the red circle as a marker 
plt.scatter(data.t[max_acc_index], acc[max_acc_index], color='red', marker='o')
# Display the text showing maximum value with correct sign
# Determine the sign of the maximum acceleration value
sign = '+' if acc[max_acc_index] >= 0 else '-'
plt.text(data.t[180], -1.1*np.max(np.abs(acc)), f'PGA: {sign}{np.abs(acc[max_acc_index]):.2f}\nTime: {data.t[max_acc_index]:.2f}',
         bbox=dict(facecolor='white', alpha=1),fontsize =12)

# Plot velocity time history
plt.subplot(3,1,2)
plt.plot(data.t, v,'b',linewidth=1.5)
plt.xlabel('Time/s',fontsize=15)
plt.ylabel('Velocity/(cm/s)',fontsize=15)
plt.xlim(0,28)
plt.ylim(-50,65)
max_v_index = np.argmax(v)
plt.scatter(data.t[max_v_index], v[max_v_index], color='red', marker='o')
plt.text(data.t[150], -0.7*np.max(v), f'PGV: {np.max(v):.2f}\nTime: {data.t[max_v_index]:.2f}',
         bbox=dict(facecolor='white', alpha=1),fontsize =12)

# Plot displacement time history
plt.subplot(3,1,3)
plt.plot(data.t, d,'b',linewidth=1.5)
plt.xlabel('Time/s',fontsize=15)
plt.ylabel('Displacement/(cm)',fontsize=15)
plt.xlim(0,28)
plt.ylim(-20,30)
max_d_index = np.argmax(d)
plt.scatter(data.t[max_d_index], d[max_d_index], color='red', marker='o')
plt.text(data.t[150], -0.6*np.max(d), f'PGD: {np.max(d):.2f}\nTime: {data.t[max_d_index]:.2f}',
         bbox=dict(facecolor='white', alpha=1),fontsize =12)

plt.tight_layout()
plt.show()