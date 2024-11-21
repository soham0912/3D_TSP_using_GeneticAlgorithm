# 3D Traveling Salesman Problem Solver

This project implements a **Genetic Algorithm (GA)** to solve the **3D Traveling Salesman Problem (3D TSP)**. The algorithm is optimized to find the shortest path that visits all given points in 3D space exactly once and returns to the starting point.

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Input Format](#input-format)
- [Output Format](#output-format)

---

## Features
- Efficient pathfinding for 3D coordinates using Genetic Algorithms.
- Hybrid initialization combining random and nearest-neighbor techniques.
- Adaptive mutation rates to improve convergence.
- Supports probabilistic elitism for maintaining diversity in the population.
- Dynamic population sizing based on the number of cities.

---

## Requirements
- **Python 3.8+**
- Libraries: `numpy`, `multiprocessing`

Install dependencies using:
```bash
pip install numpy
```

## How to Run

1. **Clone the repository**  
   Open your terminal and clone the repository using the following command:  
   ```bash
   git clone https://github.com/soham0912/3D_TSP_using_GeneticAlgorithm.git
   cd 3D_TSP_using_GeneticAlgorithm
   ```
2. **Prepare the input file**
   Ensure that your input file (`input.txt`) is created and formatted correctly (see [Input Format](#input-format))

3. **Run the program**
   ```bash
   python3 tsp_solver.py
   ```
4. **The results will be written to [Output Format](#output-format)**

## Input Format

The input should be a text file (`input.txt`) formatted as:
- The first line contains the number of cities, `N`.
- The next N lines list the 3D coordinates of each city (x, y, z) as space-separated integers.
```bash
7
199 173 30
120 199 34
144 39 130
137 199 93
153 196 97
175 53 76
173 101 186
```

## Output Format

The output is written to a file (`output.txt`) in the following format:
- The first line contains the total distance of the best path, rounded to three decimal places.
- Each subsequent line contains the 3D coordinates of the cities in the order they are visited.
```bash
576.125
120 199 34
199 173 30
175 53 76
144 39 130
173 101 186
153 196 97
137 199 93
120 199 34
```


