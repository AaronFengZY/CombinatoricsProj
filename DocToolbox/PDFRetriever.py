"""
    RAG PDFRetriever
    Written by Zhiyuan Feng

    This code defines a `PDFRetriever` class that extracts text from a PDF file, embeds the text chunks using a sentence transformer model, builds a FAISS index for efficient similarity search, and retrieves the most similar text chunks for a given query. The main methods include:

    - `extract_text()`: Extracts text from each page of the PDF and splits it into chunks.
    - `embed_chunks()`: Encodes the text chunks into embeddings using a pre-trained sentence transformer model.
    - `build_index()`: Builds a FAISS index from the chunk embeddings and saves it to a file.
    - `load_index()`: Loads the FAISS index from a file.
    - `retrieve(query, top_k)`: Retrieves the top_k most similar text chunks for a given query.
"""

import json
from collections import Counter
import concurrent.futures

from instance.problem import *
from instance.ref_problem import *
from utils.wrappers.FirstGrading import format_dify_inputs, format_openai_inputs
from utils.wrappers.ZeroToProcess_grading import format_single_rule_zero_score_recheck_inputs
from utils.apis.dify_api import completion_messages
from utils.apis.openai_api import openai_completion

from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import os

class PDFRetriever:
    def __init__(self, pdf_path, embedding_model='all-MiniLM-L6-v2', index_path='index.faiss'):
        self.pdf_path = pdf_path
        self.embedding_model = SentenceTransformer(embedding_model)
        self.index_path = index_path
        self.chunks = []
        self.chunk_embeddings = None
        self.index = None

    def extract_text(self):
        reader = PdfReader(self.pdf_path)
        for page in reader.pages:
            self.chunks.extend(page.extract_text().split('\n'))

    def embed_chunks(self):
        self.chunk_embeddings = self.embedding_model.encode(self.chunks, convert_to_numpy=True)

    def build_index(self):
        dimension = self.chunk_embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.chunk_embeddings)
        faiss.write_index(self.index, self.index_path)

    def load_index(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        else:
            raise FileNotFoundError("Index file not found. Build the index first.")

    def retrieve(self, query, top_k=5):
        query_embedding = self.embedding_model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)
        results = [self.chunks[i] for i in indices[0]]
        return results