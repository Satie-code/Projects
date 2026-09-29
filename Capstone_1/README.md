# AI/ML Capstone Project

## Autonomous Driving: Vehicle Detection and Tesla Safety Analysis

## Project Overview

This capstone project consists of two parts related to autonomous driving.

### Part 1: Vehicle Object Detection

Develop a deep-learning-based object detection model that:

- Identifies vehicles in images.
- Predicts the vehicle type or class supported by the dataset.
- Localizes detected vehicles using rectangular bounding boxes.
- Evaluates detection performance on test data.
- Performs inference on sample images.

### Part 2: Tesla Deaths Data Science Analysis

Perform exploratory data analysis on the Tesla deaths dataset to investigate:

- Accident event distributions over time and geography.
- Deaths per accident and Tesla driver/occupant deaths.
- Cyclist and pedestrian involvement.
- Collisions involving other vehicles.
- Event distributions across Tesla models.
- Verified Tesla autopilot deaths.

## Project Structure

- Part_1/: Object detection project.
- Part_2/: Tesla deaths data analysis project.

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- OpenCV
- A suitable deep learning framework and object detection architecture

The final framework and architecture will be selected after inspecting
the dataset and its annotation format.

## Dataset Requirements

Part 1:

- Images.zip
- Corresponding object detection annotations, if supplied separately.

Part 2:

- Tesla-Deaths.csv

The datasets must be inspected before model development or analysis.

## Execution Plan

1. Set up the Python environment.
2. Inspect the supplied datasets.
3. Prepare and validate the data.
4. Implement and execute Part 1.
5. Implement and execute Part 2.
6. Evaluate results and prepare project documentation.

## Reproducibility

Record the Python version, dependency versions, random seeds,
data split configuration, model configuration, and evaluation results
where applicable.

## Important Limitations

Conclusions about autopilot and road safety must account for the
available data, missing information, and the distinction between
descriptive associations and causal evidence.
