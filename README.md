# 🧮 Simple Python Calculator

A beginner-friendly command-line calculator built with Python that supports basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with division-by-zero protection)
- Input validation (handles non-numeric input gracefully)
- Clean, interactive menu-driven interface

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/simple-calculator.git
   cd simple-calculator
   ```

2. **Run the calculator:**
   ```bash
   python calculator.py
   ```

## Example Usage

```
===================================
       Simple Python Calculator
===================================

Select an operation:
  1. Addition       (+)
  2. Subtraction    (-)
  3. Multiplication (*)
  4. Division       (/)
  5. Exit
-----------------------------------
Enter your choice (1-5): 1
Enter the first number:  10
Enter the second number: 5

  10.0 + 5.0 = 15
```

## Project Structure

```
simple-calculator/
│
├── calculator.py   # Main calculator script
└── README.md       # Project documentation
```

## Pushing to GitHub

If you're uploading this for the first time:

```bash
git init
git add .
git commit -m "Initial commit: Simple Python Calculator"
git branch -M main
git remote add origin https://github.com/your-username/simple-calculator.git
git push -u origin main
```

## License

This project is open-source and free to use.
