#!/usr/bin/env python3

import subprocess

import requests

# Write commit message  based on gitt diff out with LLM.


def gen_commit(model, in_diff):

    prompt = f"""
                  Generate only a git commit message in the following format:
                  <Type>: <Short summary>
                  <Blank line>
                  1. <Detailed first change>
                  2. <Detailed second change>
                  3. <Detailed third change>
                  ... 
                  Keep the header under 50 characters. Wrap body lines at 92 characters.
                  No extra explanation or text.
                  Diff:\n{in_diff}\n
              """
    temperature = 0.1
    api_endpoint = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature},
    }

    response = requests.post(api_endpoint, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        return f"API Error: {response.status_code}"


if __name__ == "__main__":
    diff_input = subprocess.check_output(
        ["git", "--no-pager", "diff", "--no-color", "--cached"], text=True, cwd="."
    )

    model = "qwen2.5-coder"
    print(gen_commit(model, diff_input))
