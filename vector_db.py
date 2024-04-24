import pandas as pd

from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


class VectorDb():

    _client = None
    _vector_store = None
    _movies_collection_name = "movies"
    _vector_db_host = "localhost"
    _vector_db_grpc_port = 6334

    def __init__(self):
        self._client = QdrantClient(host=self._vector_db_host,
                                    grpc_port=self._vector_db_grpc_port,
                                    prefer_grpc=True)

        self._vector_store = QdrantVectorStore(client=self._client,
                                               collection_name=self._movies_collection_name)

    def delete_collection(self):
        self._client.delete_collection(self._movies_collection_name)

    @property
    def vector_store(self):
        return self._vector_store
