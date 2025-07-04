# 📊 Sorting Algorithm Visualizer and Analyzer (Python GUI)

A Python-based educational tool that compares the efficiency of common sorting algorithms using step-counting and visual graphing. It includes a GUI for loading data, generating test cases, plotting results, and comparing empirical performance to theoretical asymptotic complexity.

🧪 Ideal for analyzing real-time sorting behavior and understanding algorithmic efficiency under various conditions (best, worst, average case).

---

## 🚀 Project Features

- 🧠 Built-in sorting algorithms with step counting
- 📈 Graphical plotting of algorithm performance
- 📊 Compare two algorithms side-by-side
- 📚 Compare algorithm vs asymptotic complexity
- 🔁 Random, best-case, and worst-case data generation
- 📂 CSV file support for custom datasets
- 🧩 Robust input validation & error handling
- 🎨 PyQt5 GUI for interactivity

---

## 🧮 Sorting Algorithms Implemented

| Algorithm        | Complexity (Best / Avg / Worst) |
|------------------|-------------------------------|
| Insertion Sort   | O(n) / O(n²) / O(n²)          |
| Merge Sort       | O(n log n) / O(n log n) / O(n log n) |
| Bubble Sort      | O(n) / O(n²) / O(n²)          |
| Selection Sort   | O(n²) / O(n²) / O(n²)         |
| Heap Sort        | O(n log n) / O(n log n) / O(n log n) |
| Quick Sort       | O(n log n) / O(n log n) / O(n²) |
| Counting Sort    | O(n + k)                      |
| Radix Sort       | O(n · k)                      |

Each algorithm is implemented with a step-count tracker to provide a detailed empirical performance profile.

---

## 🧪 Test Case Generator

Supports generating the following types of test data:

| Data Type       | Description                                       |
|------------------|---------------------------------------------------|
| Random Data      | Simulates real-world average case input           |
| Best-Case Data   | Already sorted (ascending)                        |
| Worst-Case Data  | Reversely sorted (descending)                     |
| CSV Import       | Load custom data from CSV files                   |

The application uses these inputs to test and visualize how algorithms behave under different conditions.

---

## 🖼 GUI Features (PyQt5)

| Component       | Description |
|------------------|-------------|
| Load CSV         | Import external data for testing |
| Choose Mode      | Compare two algorithms or compare vs asymptotic |
| Select Case      | Choose between random, best-case, or worst-case |
| Plot Button      | Dynamically enabled based on valid input |
| Error Dialogs    | Clear messages for invalid input (size limits, missing values, etc.) |

---

## 📊 Plotting Capabilities

✔️ Plot performance of two algorithms vs input size  
✔️ Plot actual steps vs asymptotic curve for a single algorithm  
✔️ Analyze impact of input type on algorithm performance  
✔️ Plots are auto-refreshed upon interaction or data changes

Includes:

- Step counts as Y-axis
- Input size as X-axis
- Matplotlib-based plotting
- Labels, legends, titles, and grid for readability

---

## 🛠 Requirements

- Python 3.8+
- PyQt5
- matplotlib
- numpy

Install dependencies:
```bash
pip install pyqt5 matplotlib numpy
```
---

🖥 How to Run:
python main.py

