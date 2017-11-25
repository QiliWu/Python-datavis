import collections
from bokeh.sampledata import us_counties, unemployment
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool

county_coordinate_xs = [us_counties.data[code]['lons'] for code in us_counties.data if us_counties.data[code]['state']=='ca']
county_coordinate_ys = [us_counties.data[code]['lats'] for code in us_counties.data if us_counties.data[code]['state']=='ca']
colors = ['#e6f2ff', '#cce5ff', '#99cbff', '#b2d8ff', '#73abe5', '#5985b2']
county_colors = []
for county_id in us_counties.data:
    if us_counties.data[county_id]['state'] != 'ca':
        continue
    try: 
        rate = unemployment.data[county_id]
        idx = min(int(rate/2), 5)
        county_colors.append(colors[idx])
    except KeyError:
        county_colors.append('black')
        
output_file('california.html', title='california.py example')
TOOLS = 'pan, wheel_zoom, box_zoom, reset, hover, save'
p = figure(title='California Unemployment 2009', width=1000, height=1000, tools=TOOLS)
p.patches(county_coordinate_xs, county_coordinate_ys, fill_color=county_colors, fill_alpha=0.7, line_color='white', line_width=0.5)
mouse_hover = p.select(dict(type=HoverTool))
mouse_hover.point_policy = 'follow_mouse'
mouse_hover.toolips = collections.OrderedDict([('index', '$index'),('(x,y)','($x, $y)'), ('fill color', '$color[hex,swatch]:fill_color')])
show(p)