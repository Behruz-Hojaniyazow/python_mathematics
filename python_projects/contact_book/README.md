# 📒 KRYOS Contact Book

A simple and professional command-line Contact Book application built with Python.  
This project allows users to manage contacts, save them into a text file, and read saved contact information with proper formatting and exception handling.

---

# 🚀 Features

- ➕ Add new contacts
- 📋 Show all contacts
- 🔍 Search contacts
- ❌ Delete contacts
- 💾 Save contacts to a text file
- 📂 Read contacts from saved file
- 🚫 Duplicate contact protection
- ✅ Phone number validation
- ⚠️ Exception handling for file operations
- 🧹 Clean and formatted terminal output

---

# 🛠️ Technologies Used

- Python 3
- File Handling
- Exception Handling
- Functions
- Lists & Dictionaries
- UTF-8 Encoding

---

# 📁 Project Structure

```bash
contact_book/
│
├── contact_book.py          # Main contact book application
├── contact_file_reader.py   # Reads saved contact data
├── contacts_info.txt        # Saved contacts file
└── README.md
```

---

# ▶️ How to Run

## Run the main application

```bash
python contact_book.py
```

## Run the contact file reader

```bash
python contact_file_reader.py
```

---

# 📌 Example Menu

```text
========================================
Welcome to KRYOS Contact Book!
----------------------------------------
1 -> Add Contact
2 -> Show Contacts
3 -> Search Contact
4 -> Delete Contact
5 -> Save Contacts
6 -> Exit
========================================
```

---

# 📂 File Saving Format

Saved contacts are stored in a formatted structure:

```text
John Doe        | +998901234567
Jane Smith      | +998991112233
```

---

# ⚡ Error Handling

The project handles common file-related errors such as:

- File not found
- Empty file
- Input validation errors
- Unexpected exceptions

---

# 🎯 Future Improvements

- Edit existing contacts
- Export contacts to CSV
- GUI version with Tkinter
- Database integration (SQLite)
- Password protection

---

# 👨‍💻 Author

Developed by Behruz

---

# 📜 License

This project is open-source and available for learning and educational purposes.