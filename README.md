# Begin Code with Python

A collection of beginner Python exercises and projects based on the **Begin to Code with Python** book and its [sample materials](https://github.com/Begintocodewithpython/samples). Each chapter folder explores a new set of Python concepts, progressing from a simple Hello World all the way to loops, conditions, user input, and alarm-clock programs.

## Prerequisites

- **Python 3.x** — [download here](https://www.python.org/downloads/)
- A terminal or command prompt

Verify your installation:

```bash
python3 --version
```

## Clone the repository

```bash
git clone https://github.com/mohamed-hashicorp/begin-code-with-python
cd begin-code-with-python
```

---

## Chapters

### Chapter 1 — Hello World

**Path:** [`chapter1/`](chapter1/)

The classic first program. Prints `Hello World!` to the console and introduces the `print()` function.

```bash
cd chapter1
python3 hello.py
```

---

### Chapter 3 — Using Modules (`time` & `random`)

**Path:** [`chapter3/`](chapter3/)

Three mini-projects that introduce Python's standard library modules `time` and `random`.

| Project | File | What it does |
|---|---|---|
| **Time** | [`time/test-time.py`](chapter3/time/test-time.py) | Uses `time.sleep()` to pause before printing the answer |
| **Throw Die** | [`throw-die/throwDie.py`](chapter3/throw-die/throwDie.py) | Simulates rolling a six-sided die with `random.randint()` |
| **Egg Timer** | [`egg-timer/egg-timer.py`](chapter3/egg-timer/egg-timer.py) | A 5-minute countdown timer using `time.sleep()` |

```bash
python3 chapter3/time/test-time.py
python3 chapter3/throw-die/throwDie.py
python3 chapter3/egg-timer/egg-timer.py
```

---

### Chapter 4 — User Input & Combined Modules

**Path:** [`chapter4/`](chapter4/)

Introduces reading input from the user and combining `time` with `random`.

| Project | File | What it does |
|---|---|---|
| **Input** | [`input/input.py`](chapter4/input/input.py) | Asks for the user's name and prints a personalised greeting |
| **Self Timer** | [`self-timer/self-timer.py`](chapter4/self-timer/self-timer.py) | A standing-game timer: picks a random wait time and announces when it is up |

```bash
python3 chapter4/input/input.py
python3 chapter4/self-timer/self-timer.py
```

---

### Chapter 5 — Conditions & Alarm Clocks

**Path:** [`chapter5/`](chapter5/)

Introduces `if`/`elif`/`else` conditions and working with the system clock. Builds up to a full alarm clock with sound.

| File | What it does |
|---|---|
| [`OneHandedClock.py`](chapter5/OneHandedClock.py) | Reads the current hour from the system clock and prints it |
| [`SimpleAlarmClock.py`](chapter5/SimpleAlarmClock.py) | Checks whether it is after 07:30 and prints a wake-up message |
| [`WeatherHelper.py`](chapter5/WeatherHelper.py) | Fetches the local temperature and gives clothing advice based on conditions |
| [`SirenAlarmClock.py`](chapter5/SirenAlarmClock.py) | Full alarm clock — displays a message and plays `siren.wav` when it is time to get up |

```bash
python3 chapter5/OneHandedClock.py
python3 chapter5/SimpleAlarmClock.py
python3 chapter5/SirenAlarmClock.py
```

> **Note:** `WeatherHelper.py` and `SirenAlarmClock.py` use the `snaps` library from the Begin to Code with Python environment.

---

### Chapter 6 — Loops

**Path:** [`chapter6/`](chapter6/)

Introduces the `while` loop for repeating blocks of code.

| File | What it does |
|---|---|
| [`loop1.py`](chapter6/loop1.py) | Basic `while` loop that prints `"Inside loop"` five times |
| [`countdown.py`](chapter6/countdown.py) | Counts down from 10 to 1 (one step per 3 seconds) and prints `"Countdown complete!"` |

```bash
python3 chapter6/loop1.py
python3 chapter6/countdown.py
```

---

### Chapter 7 — Functions

**Path:** [`chapter7/`](chapter7/)

Introduces defining and calling functions, parameters, return values, keyword and default arguments, variable scope, and the debugger.

| File | What it does |
|---|---|
| [`EG7-01_Pathfinder.py`](chapter7/EG7-01_Pathfinder.py) | Explores how functions are defined and called in sequence |
| [`EG7-02_Times_Table.py`](chapter7/EG7-02_Times_Table.py) | Prints a times table using a function with one parameter |
| [`EG7-03_Safer_Times_Table.py`](chapter7/EG7-03_Safer_Times_Table.py) | Adds input validation with `isinstance()` and `raise Exception` |
| [`EG7-04_Two_Parameter_Times_Table.py`](chapter7/EG7-04_Two_Parameter_Times_Table.py) | Extends the times table with a `limit` parameter |
| [`EG7-05_Keyword_Arguments.py`](chapter7/EG7-05_Keyword_Arguments.py) | Demonstrates calling functions with keyword arguments |
| [`EG7-06_Default_parameters.py`](chapter7/EG7-06_Default_parameters.py) | Shows how to set default values for function parameters |
| [`EG7-07_Parameters_as_values.py`](chapter7/EG7-07_Parameters_as_values.py) | Investigates that parameters are passed by value, not by reference |
| [`EG7-08_get_value_investigation_1.py`](chapter7/EG7-08_get_value_investigation_1.py) | First investigation into building a `get_value` function with `return` |
| [`EG7-09_get_value_investigation_2.py`](chapter7/EG7-09_get_value_investigation_2.py) | Second investigation — returning `None` and handling empty returns |
| [`EG7-10_complete_get_value.py`](chapter7/EG7-10_complete_get_value.py) | Complete `get_value` with a `while` loop, `try/except`, and range validation |
| [`EG7-11_Local_Variables.py`](chapter7/EG7-11_Local_Variables.py) | Demonstrates that variables declared inside a function are local |
| [`EG7-12_Reading_Global_Variables.py`](chapter7/EG7-12_Reading_Global_Variables.py) | Shows how functions can read global variables |
| [`EG7-13_Shadowing_Global_Variables.py`](chapter7/EG7-13_Shadowing_Global_Variables.py) | Illustrates shadowing — a local variable hiding a global one |
| [`EG7-14_Storing_Global_Variables.py`](chapter7/EG7-14_Storing_Global_Variables.py) | Uses the `global` keyword to write back to a global variable |
| [`EG7-15_Using_the_input_module.py`](chapter7/EG7-15_Using_the_input_module.py) | Uses the `BTCInput` module to read validated text from the user |
| [`EG7-16_Investigating_the_debugger.py`](chapter7/EG7-16_Investigating_the_debugger.py) | Hands-on exercise to step through code with the Python debugger |

```bash
python3 chapter7/EG7-02_Times_Table.py
python3 chapter7/EG7-10_complete_get_value.py
```

---

### Chapter 8 — Lists, Sorting, Files & Tuples

**Path:** [`chapter8/`](chapter8/)

Introduces lists, bubble sort, file I/O, multi-dimensional data, and tuples. Builds a complete sales-tracking program step by step.

| File | What it does |
|---|---|
| [`EG8-01_Finding_the_largest_sales.py`](chapter8/EG8-01_Finding_the_largest_sales.py) | Reads individual sales values and finds the largest using `BTCInput` |
| [`EG8-02_Read_and_Display.py`](chapter8/EG8-02_Read_and_Display.py) | Reads sales into a list and displays them |
| [`EG8-03_Read_and_Display_loop.py`](chapter8/EG8-03_Read_and_Display_loop.py) | Refactors read-and-display using a `while` loop |
| [`EG8-04_Functions.py`](chapter8/EG8-04_Functions.py) | Extracts read and display logic into separate functions |
| [`EG8-05_Functions_and_Menu.py`](chapter8/EG8-05_Functions_and_Menu.py) | Adds a menu to choose between reading and displaying data |
| [`EG8-06_Functions_and_Menu_Elif.py`](chapter8/EG8-06_Functions_and_Menu_Elif.py) | Improves the menu using `elif` chains |
| [`EG8-07_Bubble_sort_first_pass.py`](chapter8/EG8-07_Bubble_sort_first_pass.py) | Implements a single pass of the bubble sort algorithm |
| [`EG8-08_Bubble_sort_multiple_passes.py`](chapter8/EG8-08_Bubble_sort_multiple_passes.py) | Extends bubble sort to run multiple passes until sorted |
| [`EG8-09_Efficient_Bubble_Sort.py`](chapter8/EG8-09_Efficient_Bubble_Sort.py) | Optimises bubble sort to stop early when no swaps occur |
| [`EG8-10_Sort_low_to_high.py`](chapter8/EG8-10_Sort_low_to_high.py) | Sorts the sales list from lowest to highest |
| [`EG8-11_High_and_low.py`](chapter8/EG8-11_High_and_low.py) | Finds the highest and lowest values from the sorted list |
| [`EG8-12_Total_Sales.py`](chapter8/EG8-12_Total_Sales.py) | Calculates the total of all sales values |
| [`EG8-13_Average_Sales.py`](chapter8/EG8-13_Average_Sales.py) | Computes the average sales value |
| [`EG8-14_Complete_Program.py`](chapter8/EG8-14_Complete_Program.py) | Combines all features into a complete sales analysis program |
| [`EG8-15_Load_and_Save.py`](chapter8/EG8-15_Load_and_Save.py) | Adds load and save menu options to the complete program |
| [`EG8-16_File_Output.py`](chapter8/EG8-16_File_Output.py) | Demonstrates writing lines to a text file with `open()` in write mode |
| [`EG8-17_Sales_save.py`](chapter8/EG8-17_Sales_save.py) | Saves the sales list to a file, one value per line |
| [`EG8-18_File_Input.py`](chapter8/EG8-18_File_Input.py) | Demonstrates reading lines back from a text file |
| [`EG8-19_Complete_file_read.py`](chapter8/EG8-19_Complete_file_read.py) | Reads all lines from a file using append mode and a loop |
| [`EG8-20_Sales_load.py`](chapter8/EG8-20_Sales_load.py) | Loads previously saved sales data from a file back into a list |
| [`EG8-21_Sales_load_using_with.py`](chapter8/EG8-21_Sales_load_using_with.py) | Refactors file loading to use the `with` statement |
| [`EG8-22_Tables_of_sales_data.py`](chapter8/EG8-22_Tables_of_sales_data.py) | Works with multi-dimensional lists (a list of daily sales lists) |
| [`EG8-23_Day_Name_If.py`](chapter8/EG8-23_Day_Name_If.py) | Maps a day number to a name using `if`/`elif` |
| [`EG8-24_Day_Name_List.py`](chapter8/EG8-24_Day_Name_List.py) | Replaces the `if` chain with a list index lookup |
| [`EG8-25_Day_Name_Tuple.py`](chapter8/EG8-25_Day_Name_Tuple.py) | Uses an immutable tuple instead of a list for day names |
| [`EG8-26_Pirate_Treasure_Tuple.py`](chapter8/EG8-26_Pirate_Treasure_Tuple.py) | Returns multiple values from a function using a tuple |
| [`EG8-27_Pirate_Treasure_Tuple_Function.py`](chapter8/EG8-27_Pirate_Treasure_Tuple_Function.py) | Extends the treasure example with a dedicated function returning a tuple |

```bash
python3 chapter8/EG8-14_Complete_Program.py
python3 chapter8/EG8-21_Sales_load_using_with.py
```

> **Note:** Files EG8-01 through EG8-15 require the `BTCInput` module included in [`chapter8/BTCInput.py`](chapter8/BTCInput.py).

---

## Repository structure

```
begin-code-with-python/
├── chapter1/          # Hello World
├── chapter3/          # time & random modules
│   ├── egg-timer/
│   ├── throw-die/
│   └── time/
├── chapter4/          # User input & combined modules
│   ├── input/
│   └── self-timer/
├── chapter5/          # Conditions & alarm clocks
├── chapter6/          # While loops
├── chapter7/          # Functions, scope & the debugger
└── chapter8/          # Lists, sorting, file I/O & tuples
```
