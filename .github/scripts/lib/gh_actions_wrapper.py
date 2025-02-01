import os
import dotenv
import requests
import json


class GHActionsWrapper:
    def __init__(self):
        self.github_env_path = os.environ.get("GITHUB_ENV")
        dotenv.load_dotenv(self.github_env_path)

    def append_to_github_env(self, key, value):
        if self.github_env_path:
            with open(self.github_env_path, "a") as f:
                f.write(f"{key}={value}\n")
            dotenv.load_dotenv(self.github_env_path)
        else:
            print("GITHUB_ENV environment variable not set.")


gh_actions_wrapper = GHActionsWrapper()