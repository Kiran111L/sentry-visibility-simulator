# 👁️ Sentry Visibility Simulator

## 🚀 Overview

A Python-based interactive simulation that determines whether a point (sentry) inside a bounded 2D environment can "see" the outside world. The system uses ray-casting and computational geometry to evaluate visibility against obstacles.

## 🔥 Key Features

* 📐 Ray Casting Algorithm (360° visibility check)
* 🧮 Line segment intersection detection
* 🖥️ Interactive GUI using Tkinter
* 🎯 Dynamic placement of sentry and obstacles
* 📊 Visual coordinate system with axes

## 🧠 Core Concept

The simulator uses **ray casting geometry**:

* Rays are emitted from the sentry in multiple directions
* Each ray checks for intersection with boundary segments
* If at least one ray escapes without intersection → visibility exists
* Otherwise → sentry is enclosed

## 🛠 Tech Stack

* Python 3
* Tkinter (GUI)
* Math (geometry calculations)

## 📂 Project Structure

```bash id="qkhhkp"
sentry_visibility.py
README.md
```

## ⚡ How to Run

```bash id="cawkb3"
python sentry_visibility.py
```


## 📈 Learning Outcome

* Practical implementation of ray-casting algorithms
* Understanding computational geometry concepts
* Building interactive GUI applications in Python

## 🎯 Use Case

This project demonstrates how geometric algorithms can be applied in:

* Game development (line of sight, visibility checks)
* Robotics navigation
* Computer graphics
