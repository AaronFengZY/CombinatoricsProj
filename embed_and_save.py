from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_and_save_faiss_index(pdf_path: str, save_path: str):
    # 1. Read PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # 2. Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(documents)
    
    # 3. Create local (Chinese) embeddings
    embeddings = HuggingFaceEmbeddings(model_name="GanymedeNil/text2vec-large-chinese")

    # 4. Build FAISS index
    db = FAISS.from_documents(docs, embeddings)

    # 5. Save FAISS index to disk
    db.save_local(save_path)
    print(f"FAISS index saved to: {save_path}")

create_and_save_faiss_index(
    pdf_path="/home/v-zhifeng/HPE/CombinatoricsProj/combinatorics.pdf",
    save_path="./faiss_index"
)
