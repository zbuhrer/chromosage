# ChromoSage

ChromoSage is a project analysis tool that uses embedding techniques and AI to provide insights into project contents.

## Features

- Analyzes code (.py) and documentation (.md) files
- Generates embeddings for project files
- Allows querying of project contents using natural language
- Customizable file type and directory processing

## Installation

Clone this repo, and then:

```bash
cd chromosage
pip install -r requirements.txt
```

## Configuration

ChromoSage is currently hard-coded to use a local instance of LM Studio for embeddings. If you're using a different setup, you'll need to modify the `embedding_model.py` file to match your environment.

## Usage

1. Run the application:

```bash
python main.py
```

1. Select your project directory through the GUI.
1. Wait for file processing and embedding generation to complete.
1. Use the query interface to ask questions about your project.

## Requirements

- Python 3.7+
- Local LM Studio instance (or alternative embedding service)
- Dependencies in `requirements.txt`

## TODO

- [ ] Add support for additional file types
- [ ] Integrate with version control systems
- [ ] Implement project insight visualization
- [ ] Add configuration options for different embedding services
