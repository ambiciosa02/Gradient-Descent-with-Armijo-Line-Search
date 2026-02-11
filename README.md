# Gradient-Descent-with-Armijo-Line-Search

Smart Step Gradient Descent
This project demonstrates a "smarter" version of a standard optimization algorithm. Instead of taking steps of a fixed size toward a goal, this script calculates the best step size on the fly to reach the bottom of a curve as efficiently as possible.

🧐 What does this do?
Imagine you are standing on a hill in a thick fog, trying to find the lowest point in the valley.

Standard Gradient Descent: You decide to take steps that are exactly 1 foot long every time. If you are far away, it takes forever. If you are very close to the bottom, a 1-foot step might make you overstep the center and start climbing up the other side.

This Project (Armijo Search): Before you take a step, you "test" the ground. If a big step would take you too far or back uphill, you shorten your stride until you’re sure the next move will actually lower your position.

🌟 Key Features
Self-Adjusting Steps: The algorithm automatically slows down as it approaches the target to ensure it never "overshoots" the minimum.

Visual Trajectory: The script generates a graph showing exactly how the optimizer traveled down the curve, marking each "test" point in red.

Efficiency Logging: The console tells you exactly how many times the algorithm had to shrink its step size to stay on track.


<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/2691f8b6-19a3-48d2-9b17-b04047bc46ce" />



🛠️ Requirements
You will need Python and two common libraries:

NumPy: For handling the data points.

Matplotlib: For drawing the final graph.
