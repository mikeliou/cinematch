from llama_index import (
    VectorStoreIndex,
    ServiceContext
)
from llama_index.storage.storage_context import StorageContext

from data_loader import DataLoader
from models_server import ModelsServer
from vector_db import VectorDb


class ChatEngine():

    _chat_engine = None

    def __init__(self):
        data_loader = DataLoader()
        models_server = ModelsServer()
        vector_db = VectorDb()

        service_context = ServiceContext.from_defaults(llm=models_server.llm_model, embed_model=models_server.embeddings_model)
        storage_context = StorageContext.from_defaults(vector_store=vector_db.vector_store)
        index = VectorStoreIndex.from_documents(data_loader.documents,
                                                storage_context=storage_context,
                                                service_context=service_context,
                                                show_progress=True)
        self._chat_engine = index.as_chat_engine(chat_mode="condense_plus_context",
                                                 streaming=True)

    def chat(self, input):
        return self._chat_engine.chat(input)
