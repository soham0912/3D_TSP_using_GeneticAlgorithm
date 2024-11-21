# 3D Traveling Salesman Problem Solver

This project implements a **Genetic Algorithm (GA)** to solve the **3D Traveling Salesman Problem (3D TSP)**. The algorithm is optimized to find the shortest path that visits all given points in 3D space exactly once and returns to the starting point.

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Input Format](#input-format)
- [Output Format](#output-format)
- [Key Concepts](#key-concepts)
- [License](#license)

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

