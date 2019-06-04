Kristoph Naggert | Oberlin College | Mount Desert Island Biological Laboratory

Summer 2019 Project (BioLab2019):
    
    dataVis/ - Contains a number of visualization program written in Python3 using Bokeh
    
          dataVis.py - Program written using Python3 and Seaborn to produce a multiline plot of the data.
          heatmap_bokeh.py - Program written using Python3 and Bokeh to produce a heatmap for the data.
          multiline_bokeh.py - Program written using Python3 and Bokeh to produce multiline plot of the data.
          stackedplot_bokeh.py - Program written using Python3 and Bokeh to produce individual line plots displayed on the same screen.
          YSH1.fa.pos.txt - Sample datafile for testing visualization programs.
          
    flask_proj/ - The directory containing the (Begggining) web application that will host the visualize programs\
    
          application.py - Current version of data visualization application, currently only supports a single data visualization at a time.
                  a.) Working on creating an application that will support all 3 visualizations, as well as user inputed data
          
          data/ - Directory that contains the data for the application, currently contains only preprocessed datafiles
                YSH1.fa.pos.txt - Sample datafile for testing application.
          
          templates/ - Directory containing HTML templates for the application.
                chart.html - Basic HTML template for a single multiline plot.
