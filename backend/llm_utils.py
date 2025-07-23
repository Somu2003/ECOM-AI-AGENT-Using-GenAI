import subprocess

def ask_ollama(prompt, model='gemma:2b'):
    result = subprocess.run(['ollama', 'run', model], input=prompt.encode(), capture_output=True)
    return result.stdout.decode().strip()
