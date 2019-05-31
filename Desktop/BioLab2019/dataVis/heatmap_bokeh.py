from math import pi
import pandas as pd

from bokeh.io import show
from bokeh.models import LinearColorMapper, BasicTicker, PrintfTickFormatter, ColorBar
from bokeh.plotting import figure
from bokeh.palettes import Magma256

columns=['e1', 'e2', 'e3', 'pA Site', 'e4']
data = pd.read_csv('/Users/knaggert/Desktop/BioLab2019/dumb/data/YSH1.fa.pos.txt', sep='\t', skiprows=1, header = None,
                 names = ['Base', 'Position', 'e1', 'e2', 'e3', 'pA Site', 'e4'])


array_1 = []


for k in range(len(data)):
    if (k+6 >= len(data)):
        array_1.append("N/A")
    else:
        s=""
        list1=[]
        for l in range(k, k+6):
            list1.append(data.Base[l])
        s=s.join(list1)
        array_1.append(s)
        
print(array_1[0])
print(len(array_1))

sequences = []
for n in range(len(data)*len(columns)):
    sequences.append(n)

temporary = 0
for q in range(len(array_1)):
    for d in range(len(columns)):
        sequences[temporary] = array_1[q]
        temporary = temporary+1

Sequences = pd.DataFrame(sequences, columns=['Sequence'])

'''
array = []
for l in range(len(data)*len(columns)):
    array.append(l)

temp = 0
for i in range(len(data)):
    for j in range(len(columns)):
        array[temp] = data.Base[i]
        temp=temp+1
        
Bases = pd.DataFrame(array, columns=['Base'])
'''

data['Position']=data['Position'].astype(str)
data = data.set_index('Position')

data = data.drop(columns=['Base'])

data.columns.name = 'Values'
Position = list(data.index)
Values = list(data.columns)

df = pd.DataFrame(data.stack(), columns=['score']).reset_index()

df_complete = pd.concat([df, Sequences], axis = 1)
print(df_complete)

Magma256.reverse()
mapper = LinearColorMapper(palette=Magma256, high=df_complete.score.max(), low=df_complete.score.min())

TOOLS = "hover, save, pan, box_zoom, undo, redo, reset, wheel_zoom"

p = figure(title="Heatmap of Sites", x_range=Position, y_range=Values,
           x_axis_location="above", plot_width=900, plot_height=400,
           tools=TOOLS, toolbar_location='below',
           tooltips=[('Position','@Position'),('Score', '@score'), ('Sequence', '@Sequence')])



p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "8pt"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = pi / 3

p.rect(x="Position", y="Values", width=1, height=1,
       source=df_complete,
       fill_color={'field':'score', 'transform' : mapper},
       line_color=None)


color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="8pt",
                     ticker=BasicTicker(),
                     label_standoff=6, border_line_color=None, location=(0, 0))

p.add_layout(color_bar, 'right')

show(p)      # show the plot
