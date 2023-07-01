import csv
from src.node import Node

def parse(csv_file_path):

    # Create an empty list to store the nodes
    nodes = []

    # Read from the CSV file and create Node objects
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
            # Extract the x and y values from the CSV row
                x = float(row[0])
                y = float(row[1])
                node = Node(x, y)
                nodes.append(node)
            except ValueError:
                continue
    return nodes

