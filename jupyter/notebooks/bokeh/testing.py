# Import the necessary functions from the bokeh.plotting module:
from bokeh.plotting import figure, show
from bokeh.io import save, output_file

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Create a file
output_file("testing-lines.png")

# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
save(p, "testing-lines.png", title="Test")
show(p)