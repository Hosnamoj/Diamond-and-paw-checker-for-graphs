# Diamond-and-paw-checker-for-graphs
This Python utility allows you to detect paw, diamond, co-paw, and co-diamond subgraphs in small undirected graphs. It works for any graph given as an adjacency matrix and checks all 4-vertex subsets for forbidden induced subgraphs. The complement graph is automatically checked for co-paws and co-diamonds.
## Features
- Detects **paw** and **diamond** in a graph.
- Detects **co-paw** and **co-diamond** in the complement graph.
- Works with graphs of arbitrary size (limited by Python performance).
- Simple input: adjacency matrix row by row, space-separated.
- Clear output showing which forbidden subgraphs are present and their vertices.
