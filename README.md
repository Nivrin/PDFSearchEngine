# PDF Processor API

The PDF Processor API is a FastAPI-based application for efficiently handling PDF documents. It offers a range of endpoints to manage PDF files, extract text, and perform diverse processing tasks.

## Features
- 📤 Upload and process PDF documents
- 📄 Extract text content from PDFs
- 🔄 Perform additional processing tasks on PDFs

## Getting Started

### Prerequisites
- Python 3.11.4 installed on your machine.
- Docker (optional, for running with Docker).

### Installation
```bash
git clone https://github.com/yourusername/pdf-processor-api.git
cd pdf-processor-api
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn src.main:app --reload
```
## Using Docker

### Prerequisites
- Docker installed on your machine.

### Build and Run
```bash
git clone https://github.com/yourusername/pdf-processor-api.git
cd pdf-processor-api
docker build -t pdf-processor-api .
docker run -p 80:80 pdf-processor-api
```
