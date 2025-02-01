#!/bin/bash

curl https://windsurf-stable.codeium.com/api/update/linux-x64/stable/latest -o /tmp/windsurf-update.json
jq -r '.version' /tmp/windsurf-update.json
curl https://windsurf-stable.codeium.com/api/update/linux-x64/stable/$(jq -r '.version' /tmp/windsurf-update.json) -o /tmp/windsurf-update.tar.gz
tar -xf /tmp/windsurf-update.tar.gz -C /opt/windsurf