import subprocess

commands = [
    "pip install openai",
    "pip install langchain",
    "pip install langchain-chroma",
    "pip install -U langchain-community",
    "pip install tiktoken",
    "pip install unstructured",
    "pip install --upgrade --force-reinstall pandas scipy numba"
]

for command in commands:
    subprocess.run(command, shell=True, check=True)