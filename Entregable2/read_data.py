import pandas as pd
from Graph import Graph

graphy = Graph()

df = pd.read_csv('data.csv', sep=';')

for i in range(len(df)):
    row = df.iloc[i]
    length_str = row['length'].split('.')

    if len(length_str) > 2:
        length_str = ''.join(length_str)
    else:
        length_str = row['length']

    graphy.add_edge(row['origin'], row['destination'], float(length_str), float(row['harassmentRisk']), bool(row['oneway']))

print(graphy.dijkstra('(-75.5666955, 6.1860806)', '(-75.5807143, 6.2966117)', pretty=True))

#print(df.to_string())
