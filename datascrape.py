import numpy as np
import pandas as pd
import re

import plotly.graph_objects as go

# This function will convert the url to a download link
def convert_gsheets_url(u):
    try:
        worksheet_id = u.split('#gid=')[1]
    except:
        # Couldn't get worksheet id. Ignore it
        worksheet_id = None
    u = re.findall('https://docs.google.com/spreadsheets/d/.*?/',u)[0]
    u += 'export'
    u += '?format=csv'
    if worksheet_id:
        u += '&gid={}'.format(worksheet_id)
    return u

sample_url = 'https://docs.google.com/spreadsheets/d/1C7xqQrWEz_CSXt9Ih-TahgqVgxrfZITLRa97NajZpYw/edit?usp=sharing'
try:
    url = convert_gsheets_url(URL)
    df = pd.read_csv(url)
    print('Read successfully')
except:
    print(f"Could not read any data from the URL you provided.\nReading from {sample_url} instead.")
    url = convert_gsheets_url(sample_url)
    df = pd.read_csv(url)
df.head(10)

# HODP colors
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# HODP template
theme_hodp = go.layout.Template(
    layout=go.Layout(
        title = {'font':{'size':24, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
        font = {'size':18, 'family':'Helvetica', 'color':'#717171'},
        xaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'showline': True,
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'automargin': True
                },
        yaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'showline': True,
                'automargin': True
                },
        legend = {'bgcolor':'rgba(0,0,0,0)', 
                'title':{'font':{'size':18, 'family':"Helvetica", 'color':monochrome_colors[0]}}, 
                'font':{'size':14, 'family':"Helvetica"}, 
                'yanchor':'bottom'
                },
        colorscale = {'diverging':monochrome_colors},
        coloraxis = {'autocolorscale':True, 
                'cauto':True, 
                'colorbar':{'tickfont':{'size':14,'family':'Helvetica'}, 'title':{'font':{'size':18, 'family':'Helvetica'}}},
                }
    )
)

# Pie Chart in a Final Club
fig = go.Figure()

yes = df['Are you in a final club?'].value_counts()['Yes'] 
no = df['Are you in a final club?'].value_counts()['No'] 

labels = ["Yes", "No"]
values = [yes/(yes+no) * 100, no/(yes+no) * 100]
colors = ['#C63F3F', '#F4B436', '#83BFCC']

# initialize the figure
fig = go.Figure()

# add a trace
fig.add_trace(go.Pie(
   values=values, 
   labels=labels,
   textinfo='label',
   marker_colors=colors,
   hoverinfo='label+percent'
))

# update the layout
fig.update_layout(
   title="Are You in a Final Club?", 
   xaxis={'title':{'text':'X Axis Label'}}, 
   yaxis={'title':{'text':'Y Axis Label'}}, 
   legend={'title':{'text':'Legend Title'}},
   template=theme_hodp
)

# display the figure
fig.show()

### Pie Chart 2

import plotly.graph_objects as go

fig = go.Figure()

yes = df['Have you been punched by a final club before?'].value_counts()['Yes'] 
no = df['Have you been punched by a final club before?'].value_counts()['No'] 

labels = ["Yes", "No"]
values = [yes/(yes+no) * 100, no/(yes+no) * 100]
colors = ['#C63F3F', '#F4B436', '#83BFCC']

# initialize the figure
fig = go.Figure()

# add a trace
fig.add_trace(go.Pie(
   values=values, 
   labels=labels,
   textinfo='label',
   marker_colors=colors,
   hoverinfo='label+percent'
))

# update the layout
fig.update_layout(
   title="Have You Been Punched by a Final Club Before?", 
   xaxis={'title':{'text':'X Axis Label'}}, 
   yaxis={'title':{'text':'Y Axis Label'}}, 
   legend={'title':{'text':'Legend Title'}},
   template=theme_hodp
)

# display the figure
fig.show()

### Pie Chart 3

import plotly.graph_objects as go

fig = go.Figure()

yes = df['Have you attended a final club party or event in the last:'].value_counts()['Month?'] +  df['Have you attended a final club party or event in the last:'].value_counts()['Year?'] + df['Have you attended a final club party or event in the last:'].value_counts()['Week?']
 

labels = ["Yes", "No"]
values = [yes/34 * 100, (34-yes)/34* 100]
colors = ['#C63F3F', '#F4B436', '#83BFCC']

# initialize the figure
fig = go.Figure()

# add a trace
fig.add_trace(go.Pie(
   values=values, 
   labels=labels,
   textinfo='label',
   marker_colors=colors,
   hoverinfo='label+percent'
))

# update the layout
fig.update_layout(
   title="Have You Attended a Final Club Party or Event in the Last Year?", 
   xaxis={'title':{'text':'X Axis Label'}}, 
   yaxis={'title':{'text':'Y Axis Label'}}, 
   legend={'title':{'text':'Legend Title'}},
   template=theme_hodp
)

# display the figure
fig.show()

### Most well known figure bar chart

#initialize figure
fig = go.Figure()

# creating the dataset
data = {'Porcellian':8, 'Phoenix':3, 'Spee':4,
        'Owl':2, 'Fox':1, 'Delphic':1, 'Sigma Chi': 1, 'Fly': 2}
clubs = list(data.keys())
values = list(data.values())
  
fig = go.Figure()

fig.add_trace(go.Bar(
    x=clubs,
    y=values,
    marker_color=primary_colors[0]
    
))

fig.update_layout(
    title="Most Well Known Clubs",
    template=theme_hodp
)

fig.show()

### Worst reputation bar graph

#initialize figure
fig = go.Figure()

# creating the dataset
data = {'Porcellian':3, 'Phoenix':5, 'Spee':3,
        'Owl':1, 'Fox':2, 'Delphic':1, 'Bee': 1, 'Fly': 1,
        'Fleur-de-lis':1}
clubs = list(data.keys())
values = list(data.values())
  

fig.add_trace(go.Bar(
    x=clubs,
    y=values,
    marker_color=primary_colors[0]
    
))

fig.update_layout(
    title="Clubs with the Worst Reputation",
    template=theme_hodp
)

fig.show()

### Best reputation bar graph

#initialize figure
fig = go.Figure()

# creating the dataset
data = {'Porcellian':4,
        'Owl':1, 'Fox':4, 'Delphic':1, 'Bee': 2, 'Fly': 1,
        'La Vie':1}
clubs = list(data.keys())
values = list(data.values())
  

fig.add_trace(go.Bar(
    x=clubs,
    y=values,
    marker_color=primary_colors[0]
    
))

fig.update_layout(
    title="Clubs with the Best Reputation",
    template=theme_hodp
)

fig.show()

###Punches across race pie chart

#initialize figure
fig = go.Figure()

data = {'White':9, 'Black':1, 'Asian':3, 'Hispanic':2}

labels = ["Yes", "No"]
values = [yes/34 * 100, (34-yes)/34* 100]
colors = ['#C63F3F', '#F4B436', '#83BFCC']

# initialize the figure
fig = go.Figure()

# add a trace
fig.add_trace(go.Pie(
   values=list(data.values()), 
   labels=list(data.keys()),
   textinfo='label',
   marker_colors=colors,
   hoverinfo='label+percent'
))

# update the layout
fig.update_layout(
   title="Race of Final Club Punches", 
   xaxis={'title':{'text':'X Axis Label'}}, 
   yaxis={'title':{'text':'Y Axis Label'}}, 
   legend={'title':{'text':'Race'}},
   template=theme_hodp
)

# display the figure
fig.show()

###Punches across academic area pie chart

#initialize figure
fig = go.Figure()

data = {'Social Sciences':7, 'Sciences':5, 'Arts and Humanities':1}

labels = ["Yes", "No"]
values = [yes/34 * 100, (34-yes)/34* 100]
colors = ['#C63F3F', '#F4B436', '#83BFCC']

# initialize the figure
fig = go.Figure()

# add a trace
fig.add_trace(go.Pie(
   values=list(data.values()), 
   labels=list(data.keys()),
   textinfo='label',
   marker_colors=colors,
   hoverinfo='label+percent'
))

# update the layout
fig.update_layout(
   title="Academic Areas of Final Club Punches", 
   xaxis={'title':{'text':'X Axis Label'}}, 
   yaxis={'title':{'text':'Y Axis Label'}}, 
   legend={'title':{'text':'Race'}},
   template=theme_hodp
)

# display the figure
fig.show()
