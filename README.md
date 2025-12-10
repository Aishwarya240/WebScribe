
---

# WebScribe - AI Web Summarizer

**WebScribe** is a Python command-line tool that converts any webpage into a concise, readable summary using **Llama 2** via **Ollama**. It extracts the main text from web articles and generates a human-friendly summary.

It’s lightweight, privacy-friendly, and perfect for quickly understanding long articles without reading them fully.

---

## Features

* Interactive URL input in a loop until `exit`
* URL validation and content sufficiency check
* Extracts main article text using **newspaper3k**
* Summarizes content using **Llama 2** via **Ollama**
* Shows **word count and estimated reading time** for original text and summary
* Optional multi-language summarization
* Colorful CLI interface with progress spinners for better UX

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

> Make sure **Ollama** is installed and running locally with Llama 2 models.

---

## Usage

Run the main script:

```bash
python main.py
```

### Instructions

1. Enter a **valid URL** to summarize a webpage.
2. Enter the **summary language** when prompted (default: English).
3. Type `exit` to quit.

Example:

```
Enter a URL to summarize (or type 'exit' to quit): https://example.com/article
Enter summary language (default: English): English
```

The output includes:

* Original article word count and reading time
* Summary text
* Summary word count and reading time

---

## Converting to Executable

You can create a standalone `.exe` using **PyInstaller**:

```powershell
# Activate virtual environment first
.\venv\Scripts\Activate.ps1

# Install PyInstaller
pip install pyinstaller

# Build executable
python -m PyInstaller --onefile --console main.py
```

The `.exe` will be in the `dist` folder.

---

## Requirements

```
colorama==0.4.6
yaspin==2.1.0
newspaper3k==0.2.8
ollama==0.2.0
requests==2.31.0
```

---

## Notes

* **Ollama** must be installed and running locally for summarization.
* Reading time is estimated at **200 words per minute**.
* Works best with news articles, blogs, and standard web pages.

---

## License

This project is licensed under the MIT License.

---

