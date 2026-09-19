# Dockerfile Generation using Local LLMs (Beginner)

An automated tool to generate production-ready, secure, multi-stage, and distroless `Dockerfile`s for any programming language using local Large Language Models (LLMs) with [Ollama](https://ollama.com/).

Run completely locally on your machine—no API keys, subscriptions, or external network requests required.

---

## Features

- **100% Local & Private**: Runs entirely offline using local LLMs via Ollama (default: `llama3`).
- **Language Agnostic**: Generates customized Dockerfiles for Python, Node.js, Go, Rust, Java, and any other technology stack.
- **Docker Best Practices Baked In**:
  - Multi-stage builds for minimal image size.
  - Distroless/minimal runtime base images for enhanced security.
  - Layer caching optimization (dependency installation separated from source copy).
  - Explicit port exposure and clean entrypoints.
- **Automated Output**: Directly outputs and writes a ready-to-build `Dockerfile` to the current working directory.

---

## Project Structure

```text
.
├── src/
│   └── dockerfile_generation_using_local_llms_beginner/
│       ├── __init__.py
│       └── generate_dockerfile.py   # Core script interacting with Ollama
├── pyproject.toml                   # Project metadata & dependency configuration
├── uv.lock                          # Dependency lockfile
└── README.md                        # Documentation
```

---

## Prerequisites

1. **Python**: Version `3.12` or later.
2. **[uv](https://docs.astral.sh/uv/)** (recommended) or `pip`: Modern Python package and project manager.
3. **[Ollama](https://ollama.com/)**: Installed and running locally.
4. **LLM Model**: Download the model specified in the script (default is `llama3`):

   ```bash
   # Make sure Ollama service is running
   ollama serve

   # Pull the llama3 model
   ollama pull llama3
   ```

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Arif-Badhon/Dockerfile-Generation-using-Local-LLMs-Beginner-.git
cd Dockerfile-Generation-using-Local-LLMs-Beginner-
```

### Using `uv` (Recommended)

Sync and create the virtual environment automatically:

```bash
uv sync
```

### Using `pip` / `venv`

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install .
```

---

## Usage

### 1. Ensure Ollama is Running

Make sure Ollama is active and listening on `http://localhost:11434`:

```bash
ollama list
```

### 2. Run the Generator

Using `uv`:

```bash
uv run python src/dockerfile_generation_using_local_llms_beginner/generate_dockerfile.py
```

Or with your activated virtual environment:

```bash
python src/dockerfile_generation_using_local_llms_beginner/generate_dockerfile.py
```

### 3. Enter Your Target Language / Stack

When prompted, input the programming language or framework:

```text
Enter programming language for which you want to generate Dockerfile: Python
```

Once completed, you will see:

```text
Dockerfile generated successfully
```

A freshly generated `Dockerfile` will be saved directly in your working directory.

---

## Customization

### Switching Models

If you prefer to use another local model (e.g., `mistral`, `deepseek-coder`, `qwen2.5-coder`, `codellama`), update the model parameter in [`generate_dockerfile.py`](src/dockerfile_generation_using_local_llms_beginner/generate_dockerfile.py):

```python
# Pull the model first: ollama pull qwen2.5-coder
response = ollama.Client().chat(
    model="qwen2.5-coder",
    messages=[{"role": "user", "content": full_prompt}]
)
```

### Tuning Prompts

You can adjust the prompt in [`generate_dockerfile.py`](src/dockerfile_generation_using_local_llms_beginner/generate_dockerfile.py) to incorporate organization-specific base registries, non-root users, health check instructions, or custom security constraints.

---

## Troubleshooting

- **Connection Error (`Failed to connect to Ollama`)**:
  Verify that the Ollama daemon is running:
  ```bash
  curl http://localhost:11434/
  # Expected output: "Ollama is running"
  ```
- **Model Not Found Error**:
  Ensure you have pulled the model defined in the code:
  ```bash
  ollama pull llama3
  ```

---

## Author

- **Arif** - [arifuzzaman.badhon1@gmail.com](mailto:arifuzzaman.badhon1@gmail.com)
- GitHub: [@Arif-Badhon](https://github.com/Arif-Badhon)
