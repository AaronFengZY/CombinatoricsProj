import os
import sys
import json
import time
import random
import openai
from instance.problem import StudentPA
from instance.ref_problem import RefPA
from DocToolbox.checker import Checker
from DocToolbox.PDFRetriever import PDFRetriever
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from reporter.default_reporter import DefaultReporter
from langchain.embeddings import HuggingFaceEmbeddings  # or OpenAIEmbeddings if you used that
from langchain.vectorstores import FAISS
import pdfplumber

def load_faiss_retriever():
    # Make sure the embedding model is the same one used during saving.
    embeddings = HuggingFaceEmbeddings(model_name="GanymedeNil/text2vec-large-chinese")
    
    # Load the index from local files
    index_path = "/home/v-zhifeng/HPE/CombinatoricsProj/faiss_index"
    if not os.path.isdir(index_path):
        raise ValueError(f"FAISS index folder not found at {index_path}.")

    db = FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    # Build a retriever
    retriever = db.as_retriever(search_kwargs={"k": 3})
    print("PDF Retriever loaded from FAISS index.")
    return retriever

def main():
    # Load the configuration file containing hw_base and student_id mappings
    config_file = "hw_base_student_config.json"
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

    with open(config_file, "r") as f:
        config_data = json.load(f)

    # Local DeepSeek API key configuration
    api_configs = json.load(open("./api_config/deepseek.json", "r"))
    os.environ["OPENAI_API_KEY"] = api_configs["api_key"]
    os.environ["OPENAI_BASE_URL"] = api_configs["base_url"]

    # Parse command-line arguments for filtering and hyperparameters
    filter_hw_base = None
    filter_student_ids = []
    num_responses = 1  # Default to 1 response per question

    for arg in sys.argv[1:]:
        if arg.startswith("--hw_base="):
            filter_hw_base = arg.split("=", 1)[1]
        elif arg.startswith("--num_responses="):
            num_responses = int(arg.split("=", 1)[1])
        else:
            filter_student_ids.append(arg)

    # Create retriever (same as before)
    retriever = load_faiss_retriever()
    print("PDF Retriever initialized.")

    # # Now you can use the retriever to fetch relevant documents
    # query = "请给我这本书的主要内容概括？"
    # results = retriever.get_relevant_documents(query)

    # for i, doc in enumerate(results, start=1):
    #     print(f"--- Result {i} ---")
    #     print(doc.page_content[:200], '...')  # Print just the first 200 characters

    # while(True):
    #     pass

    # Initialize checker and reporter
    checker = Checker(pdf_retriever=retriever)
    base_path = os.path.dirname(os.path.realpath(__file__))

    for hw_base, student_ids in config_data.items():
        if filter_hw_base and filter_hw_base not in hw_base:
            continue
        for student_id in student_ids:
            if filter_student_ids and student_id not in filter_student_ids:
                continue
            
            # Divider line for clarity in output
            print("-" * 60)
            
            # Illustrative example for testing hw_base and student_id
            print(f"Testing hw_base: {hw_base}, student_id: {student_id}")

            # Construct paths
            ref_path = os.path.join(base_path, hw_base, "ref/ref.json")
            student_path = os.path.join(base_path, hw_base, f"testcases/{student_id}.json")

            # Ensure required files exist
            if not os.path.exists(ref_path):
                print(f"Reference file not found: {ref_path}")
                continue
            if not os.path.exists(student_path):
                print(f"Student file not found: {student_path}")
                continue

            # Load and check
            ref_pa = RefPA.from_json(ref_path)
            student_pa = StudentPA.load_raw(student_path)
            student_pa = checker.check(ref_pa, student_pa, num_responses=num_responses)

            # Generate reports
            results_dir = os.path.join(base_path, hw_base, "results")
            os.makedirs(results_dir, exist_ok=True)
            reporter = DefaultReporter(results_dir)
            reporter.generate_reports(student_pa, f"{student_id}.json", f"{student_id}.md")
            print(f"Processed: hw_base={hw_base}, student_id={student_id}")

    print("Processing complete.")

if __name__ == "__main__":
    main()
