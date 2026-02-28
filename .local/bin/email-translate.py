#!/usr/bin/env python3
import email
import sys
from email import policy

import requests


def translate(model, inpt):
    prompt = f"Translate to Ukrainian, print only translation nothing else: '{inpt}'"
    temperature = 0.1
    api_endpoint = "http://localhost:11434/api/generate"

    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": temperature},
        }

        response = requests.post(api_endpoint, json=payload, timeout=90)
        response.raise_for_status()
        result = response.json().get("response", "").strip()
        return result
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # model = "llama3.2:3b"
    model = "hf.co/INSAIT-Institute/MamayLM-Gemma-3-12B-IT-v1.0-GGUF:Q4_K_M"

    raw_email = sys.stdin.read()
    msg = email.message_from_string(raw_email, policy=policy.default)

    # Get preferred plain text body
    body = msg.get_body(preferencelist=("plain",))
    if body:
        plain_text = body.get_content()
        print(translate(model, plain_text))
