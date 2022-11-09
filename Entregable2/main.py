import math
import pandas as pd
from ast import literal_eval as make_tuple

from Graph import Graph


def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


graphy = Graph()

df = pd.read_csv('data.csv', sep=';')

source = (-75.5666955, 6.1860806)
target = (-75.5807143, 6.2966117)

for i in range(len(df)):
    row = df.iloc[i]
    length_str = row['length'].split('.')

    if len(length_str) > 2:
        length_str = ''.join(length_str)
    else:
        length_str = row['length']

    origin = make_tuple(row['origin'])
    destination = make_tuple(row['destination'])

    graphy.add_vertex(str(origin), distance(origin, target)*76.4)
    graphy.add_vertex(str(destination), distance(destination, target)*76.4)
    graphy.add_edge(str(origin), str(destination), float(length_str) * 1/(1.00001 - float(row['harassmentRisk'])), bool(row['oneway']))

print("Finished. Calculating Shortest Path...")
print(graphy.a_star(str(source), str(target), pretty=True))
