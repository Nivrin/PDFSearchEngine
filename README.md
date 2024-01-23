# PDF Processor API

The PDF Processor API is a FastAPI-based application for processing PDF documents. It provides a set of endpoints to handle PDF files, extract text, and perform various processing tasks.

## Features
- Upload and process PDF documents
- Extract text content from PDFs
- Perform additional processing tasks on PDFs

## Getting Started
### Prerequisites
- [Python 3.11.4](https://www.python.org/downloads/release/python-3114/) installed on your machine.
- [Docker](https://www.docker.com/) (optional, for running with Docker).

### Installation
```bash
git clone https://github.com/yourusername/pdf-processor-api.git
cd pdf-processor-api
pip install -r requirements.txt
Usage
bash
Copy code
python main.py
Visit http://localhost:8000/docs in your browser to access the interactive API documentation.

Using Docker
Prerequisites
Docker installed on your machine.
Building and Running with Docker
bash
Copy code
git clone https://github.com/yourusername/pdf-processor-api.git
cd pdf-processor-api
docker build -t pdf-processor-api .
docker run -p 80:80 pdf-processor-api
The FastAPI application will be accessible at http://localhost:80/docs in your browser.

Notes
The Dockerfile uses Python 3.11.4 as the base image and installs the required dependencies specified in requirements.txt.
The SpaCy English language model (en_core_web_sm) is downloaded during the Docker image build.
The FastAPI application is launched using Uvicorn on port 80.
Project Structure
plaintext
Copy code
pdf-processor-api/
├── main.py
├── routers/
│   ├── __init__.py
│   ├── pdf_processor_api.py
├── models/
│   ├── __init__.py
│   ├── pdf_models.py
├── ...
Dependencies
FastAPI
Pydantic
[Other dependencies...]
