---

# WebScribe - AI Web Summarizer

**WebScribe** is a Python-based command-line tool that turns any webpage into a concise, readable summary using **Llama 2** via **Ollama**. It extracts the main text from web articles and generates a human-friendly summary with optional multi-language support.

WebScribe is lightweight, privacy-friendly, and perfect for quickly understanding long articles without reading them fully.

---

## Features

* Accepts a **URL input** from the user in a loop until `exit`
* **Validates URLs** and ensures content is sufficient for summarization
* Extracts main article text using **newspaper3k**
* Summarizes content using **Llama 2** via **Ollama**
* Displays **word count and estimated reading time** for both original and summary
* Supports **multi-language summarization**
* **Colorful CLI** interface with spinners for a smooth user experience

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/webscribe.git
cd webscribe
```

2. **Create and activate a virtual environment**:

```powershell
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

> Make sure you have **Ollama running locally** with Llama 2 models installed.

---

## Usage

Run the main script:

```bash
python main.py
```

### Commands

* Enter a **valid URL** to summarize a webpage.
* Type `exit` to quit the application.
* Optionally, enter a **summary language** when prompted (default: English).

Example:

```
Enter a URL to summarize (or type 'exit' to quit): https://example.com/article
Enter summary language (default: English): English
```

Output includes:

* Original word count and estimated reading time
* Summary text
* Summary word count and estimated reading time

---

## Converting to Executable

You can convert WebScribe to a standalone `.exe` using **PyInstaller**:

```powershell
# Activate venv first
.\venv\Scripts\Activate.ps1

# Install PyInstaller
pip install pyinstaller

# Build executable
python -m PyInstaller --onefile --console main.py
```

The `.exe` will be located in the `dist` folder.

---

## Requirements

See `requirements.txt`:

```
colorama==0.4.6
yaspin==2.1.0
newspaper3k==0.2.8
ollama==0.2.0
requests==2.31.0
```

---

## Notes

* **Ollama** must be installed and running locally to summarize text.
* Reading time is estimated at **200 words per minute**.
* Works best with news articles, blogs, and well-formatted web pages.

---

## License

This project is licensed under the MIT License.

---
