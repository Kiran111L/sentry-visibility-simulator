#  Algorithms : Sentry Visibility Simulator

**Algo-LL** is an interactive Python tool that visually simulates **sentry visibility** on a 2D coordinate plane.  
It helps determine whether a sentry (a point) placed inside a bounded area can "see" the outside world, using **ray casting geometry**.

---

##  Features

- **Geometric Computation** — Detects if rays from the sentry intersect with obstacles (segments).
- **Graphical Interface** — Built using **Tkinter**, allowing users to draw segments and sentries easily.
- **Ray Casting Algorithm** — Uses intersection logic to test visibility in all 360° directions.
- **Coordinate System Visualization** — Displays axes and labeled points for clarity.
- **Dynamic Interaction** — Add, test, and clear setups instantly.

---

##  Concept

This project is based on **ray-casting geometry**:
- The sentry emits rays in multiple directions (every few degrees).
- If *any* ray does **not** intersect with a segment (wall), the sentry can see “outside”.
- Otherwise, the sentry is considered “inside” a closed enclosure.

---

## Tech Stack

- **Language:** Python 3  
- **Libraries Used:**
  - `tkinter` — GUI framework
  - `math` — trigonometric and geometry operations

---

##  How to Run
python sentry_visibility.py

