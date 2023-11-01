import matplotlib.pyplot as mt
import math
import numpy as np
import tkinter as tk


def y(theta, velocity, g, x):
    return x * math.tan(theta) - (
        (g * x * x) / (2 * velocity * velocity * math.cos(theta) * math.cos(theta))
    )


def max_range(theta, velocity, g):
    return (velocity * velocity * math.sin(2 * theta)) / g


def calculate_trajectory():
    try:
     theta = float(angle_box.get())
     velocity = float(velocity_box.get())
     g = 9.8
     horizontal_range = max_range(theta, velocity, g)
     print("max horizontal distance is:", horizontal_range)
     x_all = np.arange(0, (horizontal_range), 0.0005)
     y_all = [y(theta, velocity, g, x) for x in x_all]
     mt.plot(x_all, y_all)
     max_height_x = horizontal_range / 2
     max_height_y = y(theta, velocity, g, max_height_x)
     mt.plot(max_height_x, max_height_y, "ro")
     mt.plot([max_height_x, max_height_x], [0, max_height_y], "r--")
     mt.show()
    except:
     print('Please enter numeric values')


root = tk.Tk()
root.title("Projectile Tracer")
root.geometry("500x500")

label1 = tk.Label(root, text="Enter angles in degrees:")
label1.place(x=0, y=0)
angle_box = tk.Entry(root)
angle_box.place(x=160, y=0)

label2 = tk.Label(root, text="Enter velocity of projection:")
label2.place(x=0, y=25)
velocity_box = tk.Entry(root)
velocity_box.place(x=160, y=25)

calculate_button = tk.Button(
    root, text="Calculate Trajectory", command=calculate_trajectory
)
calculate_button.place(x=0, y=75)

root.mainloop()
