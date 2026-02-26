# Password Generator

### 🎯 Purpose
The main goal of this project is to provide a **crash-proof** and **user-friendly** environment for generating secure passwords. It focuses on solving common terminal-input issues and ensuring the application remains stable regardless of user behavior.

---

### 🚀 Core Features

- **Input Armor:** Uses advanced `try-except` logic to prevent crashes from invalid data (letters, symbols, or empty inputs).
- **Sanitized Logic:** Every user input is automatically cleaned (stripped of spaces and case-sensitized) to ensure smooth transitions.
- **Smart Terminal Management:** Dynamically clears the screen based on the Operating System (Windows/Linux/Mac) for a professional look.
- **Secure Entropy:** Combines uppercase, lowercase, numbers, and special characters to maximize password strength.
- **Controlled Loop System:** Allows infinite retries and password generations without memory leaks or application restarts.

---

### 🛠️ Technical Stack
- **Language:** Python 3.x
- **Modules:** `random`, `os`, `string`, `time`
- **Architecture:** Nested while-loops with granular flow control (`break`, `continue`).

---
*A reliable tool for secure digital identity.*
