#!/bin/bash

version=$(curl -s https://windsurf-stable.codeium.com/api/update/linux-x64/stable/latest | jq -r .productVersion)

curl https://windsurf-stable.codeium.com/api/update/linux-x64/stable/latest -o /tmp/windsurf-update.json
jq -r '.version' /tmp/windsurf-update.json