# Maze-Using-Backtracking
Maze Game developed using Backtracking Technique

This project implements a **maze solver** in Python that finds a path from the **start point (S)** to the **exit (E)** in a given maze using **backtracking and pathfinding logic**.

--

## 📜 Problem Description

The program takes a predefined maze represented as a **2D grid of characters**:

* `*` → Wall (not traversable)
* `" "` → Open path (traversable)
* `E` → Entry point of the maze
* `S` → Exit point of the maze

The algorithm explores the maze step by step until it reaches the exit, marking the found path with `#`.

---

## 🛠️ Features

* Prints the original maze layout.
* Automatically identifies entry (`E`) and exit (`S`) positions.
* Uses **depth-first search (DFS)**-like exploration with backtracking.
* Displays the maze again with the **solution path** highlighted using `#`.
* Handles cases where no path exists.

---

## 📂 Project Structure

```
maze_solver.py   # Main Python script containing the maze and solving logic
```

---

## ▶️ Usage

1. Clone or download the project.
2. Run the script with Python:

```bash
python maze_solver.py
```

3. The output will display:

   * The **original maze**.
   * The **solved maze** (with the path marked as `#`).

---

## 🖼️ Example Output

### Problem Maze

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~PROBLEM~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**************************************************
*******                             ********* ****
******* ************* ************* E******** ****
...
*************************************            S
**************************************************
```

### Solution Maze

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~SOLUTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**************************************************
*******                             ********* ****
******* ************* ************* E******** ****
...                                 #
************************************############S
**************************************************
```

---
