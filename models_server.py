from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms import OpenAI


class ModelsServer():

    _embeddings_model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    _llm_model_name = 'gpt-3.5-turbo'
    _llm_temperature = 0.0
    _embeddings_model = None
    _llm_model = None

    def __init__(self):
        self._embeddings_model = HuggingFaceEmbedding(model_name=self._embeddings_model_name)
        self._llm_model = OpenAI(model=self._llm_model_name,
                                 temperature=self._llm_temperature)

    @property
    def embeddings_model(self):
        return self._embeddings_model

    @property
    def llm_model(self):
        return self._llm_model
