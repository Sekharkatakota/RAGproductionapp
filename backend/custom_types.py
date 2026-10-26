from pydantic import BaseModel


class RAGChunkAndSRC(BaseModel):
    chunks: list[str]
    source_id: str | None = None


class RAGUPsertResult(BaseModel):
    ingested: int


class RAGSearchResult(BaseModel):
    contexts: list[str]
    sources: list[str]


class RAGQueryResult(BaseModel):
    answer: str
    sources: list[str]
    num_contexts: int


RAQQueryResult = RAGQueryResult