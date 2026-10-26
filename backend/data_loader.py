import os

from dotenv import load_dotenv
from openai import OpenAI

try:
    from llama_index.core.node_parser import SentenceSplitter
    from llama_index.readers.file import PDFReader
except ImportError as exc:  # pragma: no cover - import-time guard
    raise RuntimeError(
        "Missing LlamaIndex dependencies. Install with: pip install llama-index llama-index-readers-file"
    ) from exc


load_dotenv()

EMBED_MODEL = "text-embedding-3-large"
EMBED_DIM = 3072


def _get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Add it to your environment or .env file before using the RAG endpoints.")
    return OpenAI(api_key=api_key)

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)


def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [doc.text for doc in docs if getattr(doc, "text", None)]
    chunks: list[str] = []
    for text in texts:
        chunks.extend(splitter.split_text(text))
    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    response = _get_openai_client().embeddings.create(model=EMBED_MODEL, input=texts)
    return [item.embedding for item in response.data]