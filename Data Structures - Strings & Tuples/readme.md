<div align="center">

# 🐍 Python Data Structures

### Strings & Tuples

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Topic-Data%20Structures-6A5ACD?style=for-the-badge" alt="Data Structures">
  <img src="https://img.shields.io/badge/Status-Completed-2E8B57?style=for-the-badge" alt="Completed">
</p>

<p>
  A practical implementation of Python <b>Strings</b> and <b>Tuples</b> covering
  concatenation, indexing, slicing, string methods, tuple operations, and element access.
</p>

</div>

---

## 📌 Overview

This project demonstrates the fundamental operations of two important Python data structures:

* 🔤 **Strings**
* 📦 **Tuples**

The programs focus on understanding how to create, manipulate, access, and work with these data types using simple Python operations and built-in methods.

---

## 🧩 Topics Covered

### 🔤 Strings

* String concatenation
* User input
* String indexing
* String slicing
* Reverse string
* `.upper()`
* `.lower()`
* `.capitalize()`
* `.count()`
* `.replace()`

### 📦 Tuples

* Tuple creation
* Tuple concatenation
* Tuple repetition
* Tuple indexing
* Tuple slicing
* Accessing first and last elements

---

## 🗂️ Program Structure

```text
📁 Data Structures - Strings & Tuples
│
├── 🐍 Data_Structures.py
└── 📄 README.md
```

---

# 🔤 String Operations

## 1️⃣ String Concatenation

The program takes the user's name and combines it with the string `"Hello "`.

### Example

```text
Enter your name: Dinesh
Hello Dinesh
```

It then adds a welcome message:

```text
Hello Dinesh , welcome to Python programming
```

### Concepts Used

```python
string1 + string2
```

---

## 2️⃣ String Indexing & Slicing

The concatenated string is used to demonstrate different indexing and slicing operations.

| Operation          | Python Syntax         | Result        |
| ------------------ | --------------------- | ------------- |
| First character    | `input_string[0]`     | `H`           |
| Last character     | `input_string[-1]`    | `g`           |
| First 5 characters | `input_string[:5]`    | `Hello`       |
| Last 11 characters | `input_string[-11:]`  | `programming` |
| Reverse string     | `input_string[::-1]`  | Reversed text |
| Extract `"Python"` | `input_string[26:32]` | `Python`      |

### Example Output

```text
First character of the string: H
Last character of the string: g
First 5 characters of the string: Hello
Last 11 characters of the string: programming
String in reverse: gnimmargorp nohtyP ot emoclew , hseniD olleH
Word 'Python' from the existing string: Python
```

---

## 3️⃣ String Methods

The following string is used:

```python
strM = "Python beginner tutorial"
```

### Operations Performed

| Method          | Purpose                         | Example                              |
| --------------- | ------------------------------- | ------------------------------------ |
| `.upper()`      | Converts text to uppercase      | `PYTHON BEGINNER TUTORIAL`           |
| `.lower()`      | Converts text to lowercase      | `python beginner tutorial`           |
| `.capitalize()` | Capitalizes the first character | `Python beginner tutorial`           |
| `.count()`      | Counts character occurrences    | `3`                                  |
| `.replace()`    | Replaces specified text         | `Machine Learning beginner tutorial` |

### Example Output

```text
Python beginner tutorial
PYTHON BEGINNER TUTORIAL
python beginner tutorial
Python beginner tutorial
3
Machine Learning beginner tutorial
```

---

# 📦 Tuple Operations

Two tuples are created:

```python
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
```

## 1️⃣ Concatenation

```python
t_combine = tuple1 + tuple2
```

Output:

```text
(10, 20, 30, 40, 50, 60)
```

---

## 2️⃣ Tuple Repetition

The combined tuple is repeated three times:

```python
repeated_tuple = t_combine * 3
```

Output:

```text
(10, 20, 30, 40, 50, 60,
 10, 20, 30, 40, 50, 60,
 10, 20, 30, 40, 50, 60)
```

---

## 3️⃣ Accessing the 3rd Element

```python
t_combine[2]
```

Output:

```text
30
```

> Python indexing starts from `0`, so index `2` represents the third element.

---

## 4️⃣ Accessing the First Three Elements

```python
t_combine[:3]
```

Output:

```text
(10, 20, 30)
```

---

## 5️⃣ Accessing the Last Three Elements

```python
t_combine[-3:]
```

Output:

```text
(40, 50, 60)
```

---

# 💻 Complete Output

```text
Enter your name: Dinesh

Hello Dinesh
Hello Dinesh , welcome to Python programming

First character of the string: H
Last character of the string: g
First 5 characters of the string: Hello
Last 11 characters of the string: programming
String in reverse: gnimmargorp nohtyP ot emoclew , hseniD olleH
Word 'Python' from the existing string: Python

Python beginner tutorial
PYTHON BEGINNER TUTORIAL
python beginner tutorial
Python beginner tutorial
3
Machine Learning beginner tutorial

Concatenated tuple: (10, 20, 30, 40, 50, 60)
Repeated tuple: (10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60)
3rd element from t_combine: 30
First three elements from t_combine: (10, 20, 30)
Last three elements from t_combine: (40, 50, 60)
```

---

# 🧠 Key Concepts

```text
String
 ├── Concatenation
 ├── Indexing
 ├── Slicing
 ├── Reverse
 └── Built-in Methods

Tuple
 ├── Creation
 ├── Concatenation
 ├── Repetition
 ├── Indexing
 └── Slicing
```

---

# 🛠️ Technologies Used

* 🐍 Python 3.x
* 💻 Command Line / Terminal
* 📝 VS Code / Any Python IDE

---

# ▶️ How to Run

### 1. Open the project folder

```bash
cd "Data Structures - Strings & Tuples"
```

### 2. Run the Python file

```bash
python Data_Structures.py
```

### 3. Enter your name when prompted

```text
Enter your name: Dinesh
```

The program will display the string and tuple operations with their results.

---

<div align="center">

### 🚀 Python Practice — Strings & Tuples

**Learn → Practice → Execute → Improve**

</div>
