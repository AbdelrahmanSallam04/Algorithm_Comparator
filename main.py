from PySide6.QtCore import QTimer
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QHBoxLayout

from views.Home import Ui_MainWindow
from views.Input import Ui_SortingApp
from views.InputChoice import Ui_Input

from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                               QComboBox, QCheckBox, QRadioButton, QGridLayout,
                               QVBoxLayout, QWidget, QFileDialog, QMessageBox)
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import math
import matplotlib.pyplot as plt
import time
import csv

from views.Home import Ui_MainWindow


# Data generation
# csv file data to be tested lesa
def load_data_from_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.extend([int(x) for x in row])
        return data
    except FileNotFoundError:
        QMessageBox.critical(None, "Error", "File not found.")
        return None
    except ValueError:
        QMessageBox.critical(None, "Error", "Invalid data in CSV file. Please ensure data is numerical.")
        return None


# Data Generation
# random data
def generate_test_data(size):
    return [random.randint(0, size) for _ in range(size)]


# already sorted lost
def generate_best_case_data(size):
    return list(range(size))


# r sorted lost
def generate_worst_case_data(size):
    return list(range(size, 0, -1))




# The Sorting Algorithms
# Insertion sort

def insertion_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(1, n):
        steps += 1  # for-loop iteration: int i = 1; i < n; i++
        key = arr[i]
        steps += 1  # key assignment
        j = i - 1
        steps += 1  # j initialization

        while j >= 0 and arr[j] > key:
            steps += 1  # while condition check
            arr[j + 1] = arr[j]
            steps += 1  # shifting element
            j -= 1
            steps += 1  # decrement j
        steps += 1  # final condition check when exiting while
        arr[j + 1] = key
        steps += 1  # final placement of key
    return steps


# Merge sort
def merge_sort(arr, l, r, step_count=0):
    def merge(arr, l, m, r, step_count):
        n1 = m - l + 1
        n2 = r - m
        # Create temporary arrays
        left = arr[l:l + n1]
        right = arr[m + 1:m + 1 + n2]

        # Merge the temporary arrays back into arr
        i = j = 0
        for k in range(l, r + 1):
            if i < n1 and (j >= n2 or left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
                step_count += 1
            else:
                arr[k] = right[j]
                j += 1
                step_count += 1  # Counting assignment
        return step_count

    if l < r:
        step_count += 1  # Counting comparison
        m = (l + r) // 2
        step_count += 1  # Counting division for midpoint
        step_count = merge_sort(arr, l, m, step_count)
        step_count = merge_sort(arr, m + 1, r, step_count)
        step_count = merge(arr, l, m, r, step_count)
    return step_count

def bubble_sort(arr):
    steps = 0  # Initialize step counter
    n = len(arr)
    flag = False
    for i in range(n):
        steps += 1  # Increment for the outer loop iteration
        for j in range(0, n - i - 1):
            steps += 1  # Increment for the inner loop iteration (comparison)
            if arr[j] > arr[j + 1]: # Count comparison as one step
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                flag = True
                steps += 1  # Increment for the swap
        if not flag:
            break
    return steps  # Return the total number of steps
# Selection sort
def selection_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        steps += 1
        for j in range(i + 1, n):
            steps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
                steps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps += 1
    return steps


# heap sort
def heapify(arr, n, i):
    steps = 0
    largest = i  # Initialize largest as the root
    l = 2 * i + 1  # Left child index
    r = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    steps += 1  # Comparison: l < n
    if l < n:
        steps += 1  # Comparison: arr[l] > arr[largest]
        if arr[l] > arr[largest]:
            largest = l

    steps += 1  # Comparison: r < n
    if r < n:
        steps += 1  # Comparison: arr[r] > arr[largest]
        if arr[r] > arr[largest]:
            largest = r

    # If largest is not root, swap and continue heapifying
    steps += 1  # Comparison: largest != i
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        steps += 1  # For the swap
        steps += heapify(arr, n, largest)  # Recursive call

    return steps


def heap_sort(arr):
    steps = 0
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        steps += heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root with the last element
        steps += 1  # For the swap
        steps += heapify(arr, i, 0)  # Heapify the reduced heap

    return steps


# Quick sort
def quick_sort(arr, low, high):
    steps = 0
    if low < high:
        # Perform the partition and get the index of the pivot
        pi, p_steps = partition(arr, low, high)
        steps += p_steps  # Add the steps from the partition function
          # Counting the recursive call for the left part
        steps += quick_sort(arr, low, pi - 1)  # Recursive call for left subarray
          # Counting the recursive call for the right part
        steps += quick_sort(arr, pi + 1, high)  # Recursive call for right subarray
    return steps

def partition(arr, low, high):
    steps = 0
    pivot = arr[high]
      # For assigning the pivot

    i = low - 1
    # Loop over elements and compare them with the pivot
    for j in range(low, high):
        steps += 1  # Comparison: arr[j] < pivot
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            steps+=1 # Swap counts as one step
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Final swap
    steps+=1 # Final swap counts as one step
    return i + 1, steps  # Return the pivot index and the steps taken in partition


def count_sort(input_array):
    steps = 0  # Step counter

    # Handling empty input
    if not input_array:
        return steps

    # Finding the maximum element of input_array
    M = max(input_array)
    steps += len(input_array)  # O(n)

    # Initializing count_array
    count_array = [0] * (M + 1)
    steps += M + 1  # O(M)

    # Mapping each element of input_array
    for num in input_array:
        count_array[num] += 1
        steps += 2  # 1 for access, 1 for increment

    # Calculating prefix sum
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
        steps += 2  # 1 for access, 1 for addition

    # Creating output_array
    output_array = [0] * len(input_array)
    steps += len(input_array)  # O(n)

    # Placing elements in output_array
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
        steps += 3  # 1 for access, 1 for subtraction, 1 for assignment

    return steps



def countingSort(array, place, steps):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of occurrences
    for i in range(size):
        index = array[i] // place
        count[index % 10] += 1
        steps += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
        steps += 1

    # Place the elements in sorted order
    for i in range(size - 1, -1, -1):
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        steps += 1

    # Copy back to the original array
    for i in range(size):
        array[i] = output[i]
        steps += 1

    return steps


def radixSort(array):
    max_element = max(array)
    place = 1
    steps = 0  # Initialize step counter

    while max_element // place > 0:
        steps = countingSort(array, place, steps)
        place *= 10
        steps += 1  # Increment for the while loop iteration

    return steps


# Comparison Logic
def measure_steps(algorithm, dataset):
    if algorithm == "Insertion Sort":
        return insertion_sort(dataset.copy())
    elif algorithm == "Merge Sort":
        return merge_sort(dataset.copy(), 0, len(dataset) - 1)
    elif algorithm == "Bubble Sort":
        return bubble_sort(dataset.copy())
    elif algorithm == "Selection Sort":
        return selection_sort(dataset.copy())
    elif algorithm == "Heap Sort":
        return heap_sort(dataset.copy())
    elif algorithm == "Quick Sort":
        return quick_sort(dataset.copy(), 0, len(dataset) - 1)
    elif algorithm == "Counting Sort":
        return count_sort(dataset.copy())
    elif algorithm == "Radix Sort":
        return radixSort(dataset.copy())


# Visualization
def plot_graph(x_values, y_values_1, label_1, y_values_2=None, label_2=None, title="Algorithm Efficiency"):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_values, y_values_1, label=label_1, marker="o")
    if y_values_2:
        ax.plot(x_values, y_values_2, label=label_2, marker="x")
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Number of Steps")
    ax.set_title(title)
    ax.legend()
    ax.grid(True)
    return fig


def plot_time_graph(x_values, y_values_1, label_1, y_values_2=None, label_2=None, title="Algorithm Efficiency"):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_values, y_values_1, label=label_1, marker="o")
    if y_values_2:
        ax.plot(x_values, y_values_2, label=label_2, marker="x")
    ax.set_xlabel("Input Size")
    ax.set_ylabel("Execution Time (s)")
    ax.set_title(title)
    ax.legend()
    ax.grid(True)
    return fig


# GUI Functions
class SortingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorting Algorithm Analyzer")

        self.algorithms = ["Insertion Sort", "Merge Sort", "Bubble Sort", "Selection Sort", "Heap Sort", "Quick Sort",
                           "Counting Sort", "Radix Sort"]
        self.sizes = list(range(10, 100, 10))
        self.data = None  # To hold the loaded CSV data if used
        self.data_type = "Random Data"  # Default data type

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Mode selection buttons
        self.mode_var = "compare_two"
        self.compare_two_radio = QRadioButton("Compare Two Algorithms")
        self.compare_two_radio.setChecked(True)
        self.compare_async_radio = QRadioButton("Compare with Asymptotic Efficiency")
        self.compare_two_radio.toggled.connect(self.update_ui)
        self.compare_async_radio.toggled.connect(self.update_ui)

        # CSV checkbox and file load button
        self.csv_var = False
        self.csv_checkbox = QCheckBox("Use CSV Data")
        self.csv_checkbox.toggled.connect(self.update_ui)
        self.load_button = QPushButton("Load CSV")
        self.load_button.setEnabled(False)
        self.load_button.clicked.connect(self.load_csv_file)
        self.filename = QLabel("")
        self.filename.setStyleSheet('color: #ffffff; font-weight: regular ; font-size: 12px;')

        # Data type selection
        self.data_type_label = QLabel("Data Type:")
        self.data_type_combo = QComboBox()
        self.data_type_combo.addItems(["Random Data", "Best Case Data", "Worst Case Data"])
        self.data_type_combo.currentTextChanged.connect(self.update_data_type)
        self.stepsize_label = QLabel("Step Size:")
        self.stepsize_text = QLineEdit("")
        self.stepsize_text.setStyleSheet(
            'background-color: #00006e; color: #ffffff; font-weight: bold ; font-size: 12px;')

        self.stepsize_text.setEnabled(True)
        self.stepsize_text.textChanged.connect(self.update_plot_button)
        self.arraysize_label = QLabel("Array Size:")
        self.arraysize_text = QLineEdit("")
        self.arraysize_text.setStyleSheet(
            'background-color: #00006e; color: #ffffff; font-weight: bold ; font-size: 12px;')
        self.arraysize_text.setEnabled(True)
        self.arraysize_text.textChanged.connect(self.update_plot_button)


        # Algorithm selection for algorithm comparison
        self.algo1_label = QLabel("Algorithm 1:")
        self.algo1_combo = QComboBox()
        self.algo1_combo.addItems(self.algorithms)
        self.algo1_combo.setEnabled(False)
        self.algo1_combo.currentTextChanged.connect(self.update_plot_button)

        self.algo2_label = QLabel("Algorithm 2:")
        self.algo2_combo = QComboBox()
        self.algo2_combo.addItems(self.algorithms)
        self.algo2_combo.setEnabled(False)
        self.algo2_combo.currentTextChanged.connect(self.update_plot_button)

        # Algorithm selection for asymptotic comparison
        self.single_algo_label = QLabel("Algorithm:")
        self.single_algo_combo = QComboBox()
        self.single_algo_combo.addItems(self.algorithms)
        self.single_algo_combo.setEnabled(False)
        self.single_algo_combo.currentTextChanged.connect(self.update_plot_button)

        # Case Selection
        self.case_label = QLabel("Asymptotic Case:")
        self.case_combo = QComboBox()
        self.case_combo.addItems(["Worst Case", "Best Case", "Average Case"])
        self.case_combo.setEnabled(False)
        self.case_combo.currentTextChanged.connect(self.update_plot_button)

        # Plot Button
        self.plot_button = QPushButton("Plot Graph")
        self.plot_button.setEnabled(False)
        self.plot_button.clicked.connect(self.plot_data)

        # Output Area (for graph)
        self.fig = Figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.fig)
        self.output_layout = QVBoxLayout()
        self.output_layout.addWidget(self.canvas)

        # Layout setup
        mode_layout = QVBoxLayout()
        mode_layout.addWidget(self.compare_two_radio)
        mode_layout.addWidget(self.compare_async_radio)

        csv_layout = QVBoxLayout()
        csv_row = QVBoxLayout()
        csv_row.addWidget(self.csv_checkbox)
        csv_row.addWidget(self.load_button)
        csv_row.addWidget(self.filename)
        csv_layout.addLayout(csv_row)

        data_type_layout = QVBoxLayout()
        data_type_layout.addWidget(self.data_type_label)
        data_type_layout.addWidget(self.data_type_combo)
        data_type_row = QHBoxLayout()
        data_type_row.addWidget(self.stepsize_label)
        data_type_row.addWidget(self.stepsize_text)
        data_type_row.addWidget(self.arraysize_label)
        data_type_row.addWidget(self.arraysize_text)
        data_type_layout.addLayout(data_type_row)

        algo_compare_layout = QGridLayout()
        algo_compare_layout.addWidget(self.algo1_label, 0, 0)
        algo_compare_layout.addWidget(self.algo1_combo, 0, 1)
        algo_compare_layout.addWidget(self.algo2_label, 1, 0)
        algo_compare_layout.addWidget(self.algo2_combo, 1, 1)

        algo_async_layout = QGridLayout()
        algo_async_layout.addWidget(self.single_algo_label, 0, 0)
        algo_async_layout.addWidget(self.single_algo_combo, 0, 1)
        algo_async_layout.addWidget(self.case_label, 1, 0)
        algo_async_layout.addWidget(self.case_combo, 1, 1)

        self.layout.addLayout(mode_layout)
        self.layout.addLayout(csv_layout)
        self.layout.addLayout(data_type_layout)
        self.algo_compare_widget = QWidget()
        self.algo_compare_widget.setLayout(algo_compare_layout)
        self.layout.addWidget(self.algo_compare_widget)
        self.algo_async_widget = QWidget()
        self.algo_async_widget.setLayout(algo_async_layout)
        self.layout.addWidget(self.algo_async_widget)
        self.layout.addWidget(self.plot_button)
        self.layout.addLayout(self.output_layout)

        self.update_ui()

        # Styling
        self.set_styles()
        # Set custom sizes for the button and combo box
        self.load_button.setFixedSize(100, 30)  # Smaller Load CSV button
        self.data_type_combo.setFixedSize(200, 25)  # Smaller Data Type combo box

    def set_styles(self):
        # Apply styling to buttons, labels, and layout
        self.setStyleSheet("""
            QMainWindow {
                background-color: rgb(0, 0, 79);
            }
            QLabel, QRadioButton, QComboBox {
                font: bold 15pt "Century Gothic";
                color: white;
            }
            QPushButton {
                font: bold 15pt "Century Gothic";
                color: white;
                background-color: #4CAF50;
                border: none;
                padding: 5px 0px;
                border-radius: 5px;
            }
            QPushButton:disabled {
                background-color: grey;
                opacity: 0.5;
            }
            QComboBox {
                background-color: #00006e;
                color: white;
                padding: 5px;
                border-radius: 5px;
            }
            QComboBox:disabled {
                background-color: lightgray;
            }
        """)
    def update_data_type(self, text):
        self.data_type = text

    def update_ui(self):
        self.mode_var = "compare_two" if self.compare_two_radio.isChecked() else "compare_async"
        self.csv_var = self.csv_checkbox.isChecked()

        self.algo_compare_widget.setVisible(self.mode_var == "compare_two")
        self.algo_async_widget.setVisible(self.mode_var == "compare_async")
        self.data_type_label.setVisible(not self.csv_var)
        self.data_type_combo.setVisible(not self.csv_var)
        self.stepsize_label.setVisible(not self.csv_var)
        self.stepsize_text.setVisible(not self.csv_var)
        self.arraysize_label.setVisible(not self.csv_var)
        self.arraysize_text.setVisible(not self.csv_var)

        self.load_button.setEnabled(self.csv_var)

        # Update states of other widgets based on CSV usage and mode
        if self.csv_var and self.mode_var == 'compare_two':
            self.algo1_combo.setEnabled(True)
            self.algo2_combo.setEnabled(True)
            self.single_algo_combo.setEnabled(False)
            self.case_combo.setEnabled(False)
        elif self.csv_var and self.mode_var == 'compare_async':
            self.algo1_combo.setEnabled(False)
            self.algo2_combo.setEnabled(False)
            self.single_algo_combo.setEnabled(True)
            self.case_combo.setEnabled(True)
        elif self.mode_var == 'compare_two':
            self.algo1_combo.setEnabled(True)
            self.algo2_combo.setEnabled(True)
            self.single_algo_combo.setEnabled(False)
            self.case_combo.setEnabled(False)
        else:
            self.algo1_combo.setEnabled(False)
            self.algo2_combo.setEnabled(False)
            self.single_algo_combo.setEnabled(True)
            self.case_combo.setEnabled(True)

        self.update_plot_button()

    def load_csv_file(self):
        file_dialog = QFileDialog()
        filename, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV files (*.csv)")
        self.filename.setText(filename)
        if filename:
            self.data = load_data_from_csv(filename)
            if self.data is None:
                return
            if self.mode_var == 'compare_two':
                self.algo1_combo.setEnabled(True)
                self.algo2_combo.setEnabled(True)
            elif self.mode_var == 'compare_async':
                self.single_algo_combo.setEnabled(True)
                self.case_combo.setEnabled(True)
            self.update_plot_button()


    def update_plot_button(self):
        if self.mode_var == "compare_two":
            algo1_selected = self.algo1_combo.currentText()
            algo2_selected = self.algo2_combo.currentText()

            self.plot_button.setEnabled(bool(algo1_selected and algo2_selected))
        elif self.mode_var == "compare_async":
            algo_selected = self.single_algo_combo.currentText()
            case_selected = self.case_combo.currentText()
            self.plot_button.setEnabled(bool(algo_selected and case_selected))


    def plot_data(self):
        arraysize = 0
        stepsize = 0
        if not self.csv_var:
            if self.stepsize_text.text()=='' or self.arraysize_text.text()=='' :
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setWindowTitle("Error")
                error_dialog.setText("Please enter both array size and step size values.")
                error_dialog.exec_()
                return
            else:
                arraysize = int(self.arraysize_text.text())
                stepsize = int(self.stepsize_text.text())

            if int(self.arraysize_text.text()) > 1000:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setWindowTitle("Error")
                error_dialog.setText("Array size cannot exceed 1000.")
                error_dialog.exec_()
                return

            if int(self.stepsize_text.text())>int(self.arraysize_text.text()):
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setWindowTitle("Error")
                error_dialog.setText("Step size cannot exceed array size.")
                error_dialog.exec_()
                return
            if int(self.stepsize_text.text()) > 100:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setWindowTitle("Error")
                error_dialog.setText("Step size cannot exceed 100.")
                error_dialog.exec_()
                return
            if int(self.arraysize_text.text())/int(self.stepsize_text.text()) > 100:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setWindowTitle("Error")
                error_dialog.setText("Step size cannot exceed 100 times array size.")
                error_dialog.exec_()
                return


        use_csv = self.csv_var
        self.fig.clear()
        ax = self.fig.add_subplot(111)

        if self.mode_var == "compare_two":
            algo1 = self.algo1_combo.currentText()
            algo2 = self.algo2_combo.currentText()

            if use_csv and self.data:
                x_values = list(range(1, len(self.data)+5, 5))
                self.sizes = x_values
                y_values_1 = [measure_steps(algo1, self.data[:size]) for size in self.sizes]
                y_values_2 = [measure_steps(algo2, self.data[:size]) for size in self.sizes]
            else:
                self.sizes = list(range(1, arraysize+stepsize, stepsize))
                x_values = self.sizes
                data_type = self.data_type
                if data_type == "Random Data":
                    rvalues = generate_test_data(max(self.sizes))
                    y_values_1 = [measure_steps(algo1, rvalues[:size]) for size in self.sizes]
                    y_values_2 = [measure_steps(algo2, rvalues[:size]) for size in self.sizes]
                elif data_type == "Best Case Data":
                    y_values_1 = [measure_steps(algo1, generate_best_case_data(size)) for size in self.sizes]
                    y_values_2 = [measure_steps(algo2, generate_best_case_data(size)) for size in self.sizes]
                elif data_type == "Worst Case Data":
                    y_values_1 = [measure_steps(algo1, generate_worst_case_data(size)) for size in self.sizes]
                    y_values_2 = [measure_steps(algo2, generate_worst_case_data(size)) for size in self.sizes]

            ax.plot(x_values, y_values_1, label=algo1, marker="o")
            ax.plot(x_values, y_values_2, label=algo2, marker="x")
            ax.set_title(f"Comparison: {algo1} vs {algo2}")

        elif self.mode_var == "compare_async":
            algo = self.single_algo_combo.currentText()
            case = self.case_combo.currentText()

            if use_csv and self.data:
                x_values = list(range(1, len(self.data)+5, 5))
                self.sizes = x_values
                y_values_algo = [measure_steps(algo, self.data[:size]) for size in self.sizes]
            else:
                self.sizes = list(range(1, arraysize + stepsize, stepsize))
                x_values = self.sizes
                data_type = self.data_type
                if data_type == "Random Data":
                    y_values_algo = [measure_steps(algo, generate_test_data(size)) for size in self.sizes]
                elif data_type == "Best Case Data":
                    y_values_algo = [measure_steps(algo, generate_best_case_data(size)) for size in self.sizes]
                elif data_type == "Worst Case Data":
                    y_values_algo = [measure_steps(algo, generate_worst_case_data(size)) for size in self.sizes]

            # Calculate asymptotic efficiency
            if algo == "Merge Sort" or algo == "Heap Sort":
                y_values_asymptotic = [size * math.log2(size) for size in self.sizes]
            elif algo == "Quick Sort":
                if case == "Worst Case":
                    y_values_asymptotic = [size ** 2 for size in self.sizes]
                else:  # Best and Average Case
                    y_values_asymptotic = [size * math.log2(size) for size in self.sizes]
            elif algo == "Counting Sort" or algo == "Radix Sort":
                if case == "Worst Case" or case == "Average Case":
                    y_values_asymptotic = [size + max(self.sizes) for size in self.sizes]  # O(n+k)
                else:
                    y_values_asymptotic = [size + min(self.sizes) for size in self.sizes]
            else:  # Bubble Sort, Insertion Sort, Selection Sort
                if case == "Worst Case" or case == "Average Case":
                    y_values_asymptotic = [size ** 2 for size in self.sizes]
                else:  # Best Case
                    y_values_asymptotic = [size for size in self.sizes]

            ax.plot(x_values, y_values_algo, label=algo, marker="o")
            ax.plot(x_values, y_values_asymptotic, label=f"{algo} Asymptotic Efficiency ({case})", marker="x")
            ax.set_title(f"Comparison: {algo} vs Asymptotic Efficiency ({case})")

        ax.set_xlabel("Input Size")
        ax.set_ylabel("Number of Steps")
        ax.legend()
        ax.grid(True)
        self.canvas.draw()


# class SortingApp(QMainWindow):
#     def _init_(self):
#         super()._init_()
#         self.ui = SortingApp()
#         self.setWindowTitle("Sorting Algorithm Analyzer")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Ensure the UI is set up
        # Typing Effect Variables
        self.ui.Start.clicked.connect(self.start)
    def start(self):
        self.hide()
        self.ui = SortingApp()
        self.ui.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()