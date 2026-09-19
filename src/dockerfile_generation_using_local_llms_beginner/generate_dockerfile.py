import ollama

PROMPT = """

ONLY Generate an ideal DOckerfile for {language} with best practices. Do not provide any description.
Include:
- Base Image
- Installing depndencies
- Setting working directory
- Adding source code
- Running application
- Multi stage distoroless docker image
- Expose port
"""

def generate_dockerfile(language: str) -> str:
    """
    Generates Dockerfile using Ollama LLM.

    Args:
        language: Programming language for the application

    Returns:
        Dockerfile content as string
    """
    full_prompt = PROMPT.format(language=language)
    response = ollama.Client().chat(model="llama3", messages=[{"role": "user", "content": full_prompt}])
    return response['message']['content']


if __name__ == "__main__":
    try:
        language = input("Enter programming language for which you want to generate Dockerfile: ").strip()
        dockerfile_content = generate_dockerfile(language)
        with open("Dockerfile", "w") as f:
            f.write(dockerfile_content)
        print("Dockerfile generated successfully")  
    except Exception as e:
        print(f"Error: {e}")
        print("Please ensure Ollama is running and model 'llama3' is available.")