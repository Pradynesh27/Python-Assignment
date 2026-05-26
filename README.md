# Logistics Simulation Engine

This repository contains a Python-based logistics simulation tool designed to model, process, and analyze delivery workflows from warehouse environments.

# Overview

The system automates the assignment of packages to delivery agents based on geographic proximity and calculates operational performance metrics. It is designed to handle batch processing of multiple test scenarios stored in a standardized JSON format.

# Key Features

Automated Batch Processing: Scans a `test_cases` directory and generates structured reports for every simulation found.
Distance-Based Routing: Uses Euclidean distance calculations to assign packages to the nearest agent and tracks travel paths from starting positions to warehouses and final destinations.
Performance Analytics: Automatically evaluates agent performance by tracking packages delivered and total distance traveled.
Efficiency Scoring: Computes an efficiency metric for each agent, calculated by dividing the total distance traveled by the number of packages delivered.
Automated Reporting: Identifies the "best agent" (highest efficiency) and exports detailed results into individual JSON report files.

# How It Works

1. Input: The engine reads agent starting positions, warehouse coordinates, and delivery destinations.
2. Simulation: The engine calculates the optimal assignment based on the initial distance to the warehouse. It then updates the agent's position as they complete deliveries, accumulating the total distance traveled.
3. Output: Results are saved to a `reports` folder, providing insights into individual agent performance and identifying the top-performing agent based on efficiency.


