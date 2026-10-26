# RAG Production App

This project is a simple PDF-based Retrieval-Augmented Generation (RAG) application built with Python. It ingests PDF files, chunks and embeds the content, stores the vectors in Qdrant, and answers questions using OpenAI's LLM with retrieved document context.

## Features

- Upload PDFs through a Streamlit interface
- Chunk PDF text using LlamaIndex sentence splitting
- Generate embeddings with OpenAI's embedding model
- Store vectors and metadata in Qdrant
- Query the vector database and answer questions with GPT-4o-mini
- Use Inngest event-driven workflows for ingestion and QA

## Architecture

- `backend/main.py` - FastAPI app and Inngest functions
- `backend/streamlit_app.py` - Streamlit UI for uploading PDFs and asking questions
- `backend/data_loader.py` - PDF loading, chunking, and OpenAI embeddings
- `backend/vector_db.py` - Qdrant storage operations
- `backend/custom_types.py` - Pydantic models for RAG workflow payloads
- `qdrant_storage/` - Local persistent Qdrant data directory

## Tech Stack

- Python
- FastAPI
- Streamlit
- Qdrant
- OpenAI API
- Inngest
- LlamaIndex

## Prerequisites

- Python 3.10+
- Docker (for running Qdrant locally)
- OpenAI API key
- Node.js + npm only if you plan to run the Inngest dev server via the CLI

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

pip install uv

uv init 
uv add fastapi inngest llama-index-core llama-index-readers-file python-dotenv qdrant-client uvicorn streamlit openai

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Optional:

```env
INNGEST_API_BASE=http://127.0.0.1:8288/v1
```

## Run Local Services

### 1) Start Qdrant

```bash
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

### 2) Start Inngest dev server

If you have the Inngest CLI installed:

```bash
inngest dev
```

This app is configured to use the local Inngest API at:

```text
http://127.0.0.1:8288/v1
```

## Start the App

### Start the API server

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

### Start the Streamlit UI

```bash
streamlit run backend/streamlit_app.py
```

Then open the local Streamlit URL shown in the terminal.

## Usage

1. Upload a PDF in the Streamlit UI.
2. The app triggers an Inngest ingestion event.
3. The backend reads the PDF, splits it into chunks, embeds each chunk, and stores them in Qdrant.
4. Ask a question about the uploaded document.
5. The app retrieves the most relevant chunks, sends them to GPT-4o-mini, and returns a grounded answer with source references.

## Inngest Events

The app exposes two workflow events:

- `rag/ingest_pdf` - Reads and embeds a PDF
- `rag/query_pdf_ai` - Searches relevant chunks and asks the LLM to answer

## Notes

- The Qdrant collection name is `docs` and is created automatically if it does not exist.
- The default embedding model is `text-embedding-3-large`.
- The default LLM is `gpt-4o-mini`.
- The app expects the uploaded PDF to be accessible from the server environment.

## Troubleshooting

### No answer returned

- Check that `OPENAI_API_KEY` is set correctly.
- Confirm Qdrant is running on `http://localhost:6333`.
- Confirm the Inngest dev server is running and reachable.

### PDF not ingested

- Verify the uploaded file is a valid PDF.
- Check the FastAPI and Inngest logs for errors.
- Ensure the project root has write access for the local upload directory.

## License

This project is provided as a local development sample for PDF RAG workflows and is intended for educational or internal use.


## environment setting 

.\.venv\Scripts\Activate.ps1; uvicorn backend.main:app 

