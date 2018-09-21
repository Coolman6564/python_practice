import json

from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

#Load the data into a list
filename = 'population_data.json'

with open(filename) as file_object:
    pop_data = json.load(file_object)

# Build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            # print(code + ": " + str(population))
        # else:
          #  print('ERROR - ' + country_name)

        #print(country_name + ": " + str(population))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_populations.svg')