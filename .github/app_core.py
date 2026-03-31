import logging
import json
import os

# Try importing Ollama
try:
    import ollama
    ollama_available = True
except ImportError:
    ollama_available = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomError(Exception):
    pass

class Configuration:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise CustomError(f"Configuration file not found: {self.config_file}")
        with open(self.config_file) as f:
            self.config = json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)

class InputValidator:
    @staticmethod
    def validate_input(user_input):
        if not user_input or not user_input.strip():
            raise ValueError("Input cannot be empty.")
        return True

class ModelSelector:
    def __init__(self, available_models):
        self.available_models = available_models

    def select_model(self, model_name):
        if model_name not in self.available_models:
            raise CustomError(f"Model '{model_name}' selection error.")
        return model_name

class ChatResponse:
    """Unified response object for ui-olam.py compatibility"""
    def __init__(self, text, model):
        self.text = text
        self.model = model

class App:
    def __init__(self, config_file='config.json', use_ollama=False):
        self.config = Configuration(config_file)
        self.validator = InputValidator()
        self.use_ollama = use_ollama

        if self.use_ollama:
            self.model_selector = ModelSelector(
                self.config.get("available_ollama_models", ["llama3:latest"])
            )
        else:
            self.model_selector = ModelSelector(
                self.config.get("available_models", ["Basic Analysis"])
            )

    def run(self, user_input, model_name=None):
        self.validator.validate_input(user_input)
        if not model_name:
            model_name = self.config.get("default_model", "Basic Analysis")

        selected_model = self.model_selector.select_model(model_name)

        # Ollama AI mode
        if self.use_ollama:
            if not ollama_available:
                return ChatResponse("Ollama SDK not installed or running.", selected_model)
            try:
                response = ollama.chat(
                    model=selected_model,
                    messages=[{"role": "user", "content": user_input}]
                )
                # ✅ Safely extract text from any SDK version
                if hasattr(response, "text"):
                    ai_text = response.text
                elif hasattr(response, "content"):
                    ai_text = response.content
                elif hasattr(response, "output") and len(response.output) > 0:
                    ai_text = response.output[0].content
                else:
                    ai_text = str(response)  # fallback

                return ChatResponse(ai_text, selected_model)
            except Exception as e:
                return ChatResponse(f"Error: {str(e)}", selected_model)

        # Basic models
        output = ""
        if selected_model == "Basic Analysis":
            output = "Root Cause: VIP or Pool members down.\nSuggested Command: tmsh show ltm pool"
        elif selected_model == "Pool Member Check":
            output = "Root Cause: Some pool members are down.\nSuggested Command: tmsh show ltm pool members"
        elif selected_model == "VIP Status Check":
            output = "Root Cause: VIP may be disabled.\nSuggested Command: tmsh show ltm virtual"
        elif selected_model == "Health Monitor Check":
            output = "Root Cause: Health monitor failed.\nSuggested Command: tmsh show ltm monitor"
        else:
            output = f"Selected model '{selected_model}' not recognized. Please check configuration."

        return ChatResponse(output, selected_model)


# Example usage
if __name__ == "__main__":
    app = App(use_ollama=True)
    user_input = "Check VIP and pool status"
    response = app.run(user_input)
    print(f"Model: {response.model}\nAI Output:\n{response.text}")
