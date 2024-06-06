# %%
import ibm_db
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.DataFrame({1,2,3})

# %%
df[0].shape
df.plot()
# %%
df.plot(kind='pie', labels=False)

# %%
from wordcloud import WordCloud

alice = WordCloud()

# %%
import seaborn as sns
ax = sns.regplot

# %%
import plotly.graph_objects as go
import plotly

trace0 = go.Scatter(
     x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = go.Data([trace0, trace1])

plotly.offline.iplot(data, filename = 'basic-line') 

go.Layout()

# %%
data_x = [1000,518,331,277]
data_y = ['Rent','Food','Bills','Miscellaneous']
colors = ['#d32c58', '#f9b1ee', '#b7f9b1', '#b1f5f9']
trace = go.Pie(labels=data_x, values=data_y,
    hoverinfo='label+percent', textinfo='value',
     textfont=dict(size=25),
     marker=dict(colors=colors,
         line=dict(color='#000000', width=3))) 
# %%
data_x = [1000,518,331,277]
data_y = ['Rent','Food','Bills','Miscellaneous']
colors = ['#d32c58', '#f9b1ee', '#b7f9b1', '#b1f5f9']
trace = go.Pie(labels=data_y, values=data_x,
     hoverinfo='label+percent', textinfo='value',
     textfont=dict(size=25),
     marker=dict(colors=colors,
          line=dict(color='#000000', width=3))) 
# %%
data_x = [1000,518,331,277]
data_y = ['Rent','Food','Bills','Miscellaneous']
colors = ['#d32c58', '#f9b1ee', '#b7f9b1', '#b1f5f9']
trace = go.Pie(x=data_x, y=data_y,
     hoverinfo='label+percent', textinfo='value',
     textfont=dict(size=25),
     marker=dict(colors=colors,
          line=dict(color='#000000', width=3))) 
# %%
data_x = [1000,518,331,277]
data_y = ['Rent','Food','Bills','Miscellaneous']
colors = ['#d32c58', '#f9b1ee', '#b7f9b1', '#b1f5f9']
trace = go.Pie(x=data_x, y=data_y,
     hoverinfo='label+percent', textinfo='value',
     textfont=dict(size=25),
     mode=dict(colors=colors,
         line=dict(color='#000000', width=3))) 

# %%
# import plotly.express as px
# fig = px.scatter()

from plotly import __version__
__version__
# %%
