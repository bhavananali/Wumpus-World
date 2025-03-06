# 🏹 Wumpus World with A* Pathfinding

This project is part of my **MTech 1st year mini-project for the Artificial Intelligence 1st-semester course** at **IIT Bhubaneswar**. It implements the classic AI problem, **Wumpus World**, incorporating A* pathfinding to efficiently navigate the grid.

---

## 📋 Project Overview

**Wumpus World** is a grid-based environment with the following elements:
- **Agent** 🧍: Navigates the grid to find gold without getting killed.
- **Wumpus** 👹: A monster that kills the agent upon encounter.
- **Pits** 🕳️: Deadly traps that cause the agent to fall and die.
- **Gold** 💰: The goal is to find and grab the gold.

The agent perceives its environment through:
- **Stench**: Near the Wumpus.
- **Breeze**: Near pits.
- **Glitter**: When gold is nearby.

The project uses a **Knowledge Base (KB)** to infer safe paths and implements **A* pathfinding** to find an optimal path to the gold.

---

## 🚀 Features
- **Dynamic grid size** input.
- Multiple Wumpus and pits.
- Knowledge-based safe path inference.
- **A* algorithm** for efficient pathfinding.
- Console-based UI for input and output.

---

## 🛠️ How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wumpus-world.git
   cd wumpus-world
   ```
3. Run the script:
   ```bash
   python wumpus_world.py
   ```

---

## 🖋️ Sample Input
```
Enter grid size (e.g., 4 for 4x4 grid): 4
Enter number of Wumpus: 1
Enter Wumpus position (row col, 0-based index): 2 2
Enter number of Pits: 2
Enter Pit position (row col, 0-based index): 1 3
Enter Pit position (row col, 0-based index): 3 0
Enter Gold position (row col, 0-based index): 3 3
Enter agent's starting position (row col, 0-based index): 0 0
```

---

## 📤 Sample Output
```
Percepts at (0, 0): []
Knowledge Base: {(0, 0): {'Safe': True, 'Wumpus?': False, 'Pit?': False, 'Visited': True}, ...}
Safe path to gold using A*: [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
Gold Found! Exiting.
```

---

## 📚 Concepts Covered
- **Knowledge-based agents**
- **Inference rules** for safe paths
- **A* search algorithm** for pathfinding
- **Heuristic functions** for optimal path selection

---

## 👩‍💻 Author
**Nali Bhavana**  
- MTech 1st Year, IIT Bhubaneswar  

---

Feel free to explore, modify, and suggest improvements! 😊

