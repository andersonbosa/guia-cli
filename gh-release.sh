#!/bin/bash

# Defines the release version and the message
VERSION="v$1"
RELEASE_MESSAGE="$2"

if [ -z "$1" ]; then
  echo '[ERROR] Please enter the release version as an argument.'
  echo '[USAGE] bash .release.sh <version>'
  echo '        bash .release.sh 0.0.1'
  exit 1
fi

git add --all && git commit --allow-empty --message "release: $VERSION" && git push

# Creates the release
gh release create $VERSION --title "$VERSION" --notes "$RELEASE_MESSAGE"

# Checks if the command was successful
if [ $? -eq 0 ]; then
  echo "[INFO] Release created successfullyo"
  
  # Upload the build files (replace with the right path)
  gh release upload $VERSION dist/*

  # Check if upload was successful
  if [ $? -eq 0 ]; then
    echo "[INFO] Build files sent successfully"
  else
    echo "[ERROR] Failure when sending build files"
  fi

else
  echo "[ERROR] Failure when creating release"
fi
