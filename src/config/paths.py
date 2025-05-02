from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Directories root
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
DB_DIR = DATA_DIR / "db"
DOCS_DIR = PROJECT_ROOT / "docs"
IMAGES_DIR = DOCS_DIR / "images"
HTML_DIR = RAW_DIR / "html"
CSV_DIR = RAW_DIR / "csv"
PDF_DIR = RAW_DIR / "pdf"
TXT_DIR = RAW_DIR / "txt"


# Specific files
WEBAI_FILE = HTML_DIR / "webai.html"
CSVAI_FILE = CSV_DIR / "csvai.csv"
PDFAI_FILE = PDF_DIR / "pdfai.pdf"
TXTAI_FILE = TXT_DIR / "txtai.txt"
