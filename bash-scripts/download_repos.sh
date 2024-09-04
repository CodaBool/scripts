#!/usr/bin/bash

# would need to run with each owner in the org

OWNER=OWNER_NAME

/d/Util/GithubCLI/gh repo list $OWNER --limit 1000 | while read -r repo _; do
  echo "$repo"
 /d/Util/GithubCLI/gh repo clone "$repo" "$repo" -- --depth 1
done
