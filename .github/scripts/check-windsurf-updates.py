import os
import dotenv
import requests
import json
from lib.custom_dataclasses import WindsurfRelease
from lib.gh_actions_wrapper import gh_actions_wrapper as gh



def get_latest_windsurf() -> str:
    response = requests.get("https://windsurf-stable.codeium.com/api/update/linux-x64/stable/latest")
    response.raise_for_status()
    return response.json()

def main():
    with open("build_config.json", "r") as f:
        build_config = json.load(f)
    
    latest = WindsurfRelease.from_json(get_latest_windsurf())
    current = WindsurfRelease.from_json(build_config)
    
    if current.sha256hash == latest.sha256hash:
        gh.append_to_github_env("UPDATE_AVAILABLE", "false")
    else:
        latest.save_json('build_config.json')
        gh.append_to_github_env("UPDATE_AVAILABLE", "true")
        gh.append_to_github_env("WINDSURF_SHA256HASH", latest.sha256hash)
        gh.append_to_github_env("WINDSURF_VERSION", latest.windsurfVersion)


if __name__ == "__main__":
    main()