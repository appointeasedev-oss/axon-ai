import os
import json
import torch
import subprocess
from openai import OpenAI

client = OpenAI()

def get_source_code():
    source_files = {}
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    source_files[path] = f.read()
    return source_files

def analyze_and_improve():
    print("Starting self-improvement cycle...")
    
    # 1. Gather context
    source_code = get_source_code()
    
    # Load latest metrics if available
    metrics = {}
    if os.path.exists("metrics.json"):
        with open("metrics.json", "r") as f:
            metrics = json.load(f)
            
    prompt = f"""
    You are AXON, a self-improving AI. Your goal is to analyze your own source code and performance metrics, then propose improvements.
    
    Current Source Code:
    {json.dumps(source_code, indent=2)}
    
    Current Metrics:
    {json.dumps(metrics, indent=2)}
    
    Task:
    1. Identify bottlenecks or areas for improvement in the architecture or training logic.
    2. Propose specific code changes.
    3. Output the changes in a structured JSON format: {{"file_path": "new_content"}}.
    
    Focus on:
    - Optimizing the Transformer architecture.
    - Improving the training loop efficiency.
    - Enhancing the self-improvement logic itself.
    
    Only output the JSON.
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "system", "content": "You are AXON's self-improvement core."},
                  {"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    
    improvements = json.loads(response.choices[0].message.content)
    
    # 2. Apply improvements
    for path, content in improvements.items():
        print(f"Applying improvement to {path}...")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
            
    # 3. Commit changes
    try:
        subprocess.run(["git", "config", "user.name", "Axon AI"], check=True)
        subprocess.run(["git", "config", "user.email", "axon@self-improvement.ai"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Axon self-improvement: autonomous code update"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Improvements committed and pushed.")
    except Exception as e:
        print(f"Failed to commit changes: {e}")

if __name__ == "__main__":
    analyze_and_improve()
