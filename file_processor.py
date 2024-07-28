import os
import json
from embedding_model import get_embedding

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return {
        'path': file_path,
        'content': content,
        'embedding': get_embedding(content)
    }

def process_directory(directory, file_extensions=('.py', '.md'), ignore_dirs=('venv',)):
    embeddings = []
    for root, dirs, files in os.walk(directory):
        # Remove ignored directories
        for ignore_dir in ignore_dirs:
            if ignore_dir in dirs:
                dirs.remove(ignore_dir)
        
        for file in files:
            if file.endswith(file_extensions):
                file_path = os.path.join(root, file)
                embeddings.append(process_file(file_path))
    return embeddings

def save_embeddings(embeddings, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(embeddings, f, indent=2)

def load_embeddings(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        return json.load(f)