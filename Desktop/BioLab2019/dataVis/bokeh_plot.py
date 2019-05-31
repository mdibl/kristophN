# Load in required libraries #

import pandas as pd
import numpy as np

# Read in Data #

data = pd.read_csv('YSH1.fa.pos.txt', sep='\t', skiprows=1, header = None, names = ['Base', 'Position', 'e1', 'e2', 'e3', 'pA Site', 'e4'])

# Bokeh Multiline Plot #

from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend, LegendItem
from bokeh.models import Range1d
from bokeh.embed import components


p = figure() # Set size of plot



colors=['#000003', '#3B0F6F', '#8C2980', '#DD4968', '#FD9F6C']
ax = p.multi_line(xs=[data['Position'], data['Position'], data['Position'], data['Position'], data['Position']],
             ys=[data['e1'], data['e2'], data['e3'], data['pA Site'], data['e4']],
                  color=colors) # Plot function

# Add in legend parameters #

legend = Legend(items=[
    LegendItem(label="e1", renderers=[ax], index=0),
    LegendItem(label="e2", renderers=[ax], index=1),
    LegendItem(label="e3", renderers=[ax], index=2),
    LegendItem(label="pA Site", renderers=[ax], index=3),
    LegendItem(label="e4", renderers=[ax], index=4),
])

p.add_layout(legend)

# Label x and y-axis and give title

p.title.text = 'Interactive Plot Iteration 2.0'
p.xaxis.axis_label = 'Position'
p.yaxis.axis_label = 'Value'

show(p) # Display

script, div = components(p)
print(script)
print(div)
