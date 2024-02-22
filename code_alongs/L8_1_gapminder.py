import plotly_express as px

gapminder = px.data.gapminder()

fig = px.scatter(
gapminder, 
x="gdpPercap", 
y="lifeExp", 
size="pop", 
color="country",
size_max=70,
log_x=True, 
animation_frame="year", 
animation_group="country",
title="Gapminder",
range_y=[25,90], 
range_x=[100,100000])

fig.show()