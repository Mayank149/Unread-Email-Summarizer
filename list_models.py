import google.generativeai as genai
import os
import sys

# Get API key from environment or command line
api_key = os.getenv("GEMINI_API_KEY")
if not api_key and len(sys.argv) > 1:
    api_key = sys.argv[1]
if not api_key:
    print("Error: GEMINI_API_KEY not set")
    print("Usage: python list_models.py [API_KEY]")
    print("Or set GEMINI_API_KEY environment variable")
    exit(1)

# Configure API
genai.configure(api_key=api_key)

# List all available models
print("Available Gemini models:")
print("=" * 60)
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Name: {model.name}")
        print(f"Display Name: {model.display_name}")
        print(f"Supported methods: {model.supported_generation_methods}")
        print("-" * 60)
