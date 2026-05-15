# Instagram Message Extractor

A lightweight Python utility equipped with a graphical user interface (GUI) to parse, clean, and convert Instagram JSON message exports into a readable, chronological text log with precise timestamps.

## Features

- **GUI File Selection:** Easily select your `message_1.json` export file via a native file dialog.
- **Chronological Sorting:** Automatically reverses raw chat entries to arrange messages in a natural oldest-to-newest order.
- **Timestamp Formatting:** Converts raw millisecond timestamps into a clean, readable format (`[DD.MM.YY - HH:MM]`).
- **Encoding Fixer:** Automatically resolves common Latin1/UTF-8 character corruption issues typical in Instagram data exports.
- **Clean Output Export:** Generates a neat `clean_timestamped_log.txt` file right in the source directory.

## Requirements

- Python 3.x (Standard libraries only: `json`, `os`, `datetime`, `tkinter`)

## Setup & Installation

**1. Clone the repository:**
`git clone https://github.com/typh403/instagram-message-extractor.git`

**2. Run the script:**
`python main.py`