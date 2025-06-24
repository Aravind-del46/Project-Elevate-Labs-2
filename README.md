# Password Strength Analyzer with Custom Wordlist Generator

This project is a GUI-based tool built with Python that helps users analyze the strength of their passwords and generate custom wordlists using leetspeak transformations. It's designed as part of the Elevate Labs Cybersecurity Internship (June 2025) to promote password awareness and demonstrate practical security concepts.

---

## Features

- Analyze password strength using the `zxcvbn` library
- Get real-time feedback and crack-time estimates
- Custom wordlist generator with leetspeak variations
- Simple GUI built with Tkinter for ease of use

---

## Technologies Used

- Python 3.x
- [`zxcvbn`](https://github.com/dropbox/zxcvbn) – Password strength estimator
- Tkinter – Built-in Python GUI library

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Aravind-del46/Project-Elevate-Labs-2.git
cd Project-Elevate-Labs-2

pip install zxcvbn

python main.py

Wordlist Generator Logic

    Accepts a base keyword (like a name or date)

    Applies common leetspeak transformations (a → @, e → 3, o → 0, etc.)

    Generates variations for use in cracking simulations or training


## Project-Elevate-Labs-2/
│
├── main.py             # Main application file with GUI logic
├── README.md           # Project documentation
├── requirements.txt    # (Optional) Python dependencies
└── screenshots/        # (Optional) Folder for screenshots or demo images


Aravind Kumar
Elevate Labs Cybersecurity Internship - June 2025 
