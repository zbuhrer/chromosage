import os
import json
from ui import UI
from file_processor import process_directory, save_embeddings
from chat_model import get_chat_response
from embedding_model import get_embedding, cosine_similarity

class Controller:
    def __init__(self, ui: UI):
        self.ui = ui
        self.ui.query_button.on_click = self.query_embeddings

    def process_project(self):
        if not self.ui.project_path.value:
            self.ui.output_text.value = "Please select a project directory."
            self.ui.output_text.visible = True
            self.ui.page.update()
            return

        json_file = os.path.join(self.ui.project_path.value, "project_embeddings.json")
        
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                data = json.load(f)
            self.ui.output_text.value = f"Existing JSON file found:\n\nFile: {json_file}\nNumber of embeddings: {len(data)}\nTotal size: {os.path.getsize(json_file) / 1024:.2f} KB"
        else:
            embeddings = process_directory(self.ui.project_path.value)
            save_embeddings(embeddings, json_file)
            self.ui.output_text.value = f"Embeddings generated and saved:\n\nFile: {json_file}\nNumber of embeddings: {len(embeddings)}\nTotal size: {os.path.getsize(json_file) / 1024:.2f} KB"
        
        self.ui.output_text.visible = True
        self.ui.query_input.visible = True
        self.ui.query_button.visible = True
        self.ui.page.update()

    def query_embeddings(self, e):
        query = self.ui.query_input.value
        if not query:
            self.ui.query_result.value = "Please enter a query."
            self.ui.query_result.visible = True
            self.ui.page.update()
            return

        project_dir = self.ui.project_path.value if self.ui.project_path.value else ""
        if not project_dir:
            self.ui.query_result.value = "Project directory is not set. Please select a directory first."
            self.ui.query_result.visible = True
            self.ui.page.update()
            return

        json_file = os.path.join(project_dir, "project_embeddings.json")
        if not os.path.exists(json_file):
            self.ui.query_result.value = f"Embeddings file not found in {project_dir}. Please generate embeddings first."
            self.ui.query_result.visible = True
            self.ui.page.update()
            return

        with open(json_file, 'r') as f:
            embeddings = json.load(f)

        query_embedding = get_embedding(query)

        similar_files = sorted(embeddings, key=lambda x: cosine_similarity(x['embedding'], query_embedding), reverse=True)[:3]

        context = "\n\n".join([f"File: {file['path']}\n\nContent:\n{file['content'][:500]}..." for file in similar_files])

        self.ui.chat_history.append({"role": "system", "content": f"You are an AI assistant helping with a Python project. Here's some context from the most relevant files:\n\n{context}"})
        self.ui.chat_history.append({"role": "user", "content": query})

        ai_response = get_chat_response(self.ui.chat_history)
        self.ui.chat_history.append({"role": "assistant", "content": ai_response})

        self.ui.query_result.value = f"AI Assistant's response:\n\n{ai_response}"
        self.ui.query_result.visible = True
        self.ui.page.update()