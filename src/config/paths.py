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

# Specific files
WEBAI_FILE = HTML_DIR / "webai.html"