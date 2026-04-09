# Password Manager

A secure way to store your login credentials locally using Python and Fernet encryption.

## Prerequisites
* **Python 3.x** installed on your system.

## Setup Instructions

1. **Clone the project** to your local machine.

2. **Install dependencies**:
    ```bash
    pip install python-dotenv cryptography
    ```

3. **Generate your Encryption Key**:
    Run this command in your terminal to get a unique secret key:
    ```bash
    python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
    ```

4. **Create a new file** named `.env` in the root folder.

5. **Configure the key**:
    Add the following line to the file, pasting your key after the `=` (no spaces):
    ```text
    ENCRYPTION_KEY=your_copied_key_here
    ```

6. **Run the Program**:
    ```bash
    python3 main.py
    ```

## Security Note
Your `.env` file is excluded from Git via `.gitignore`. Never share your encryption key, as it is required to decrypt your `password_manager.json` data.
