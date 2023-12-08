#!/bin/bash

# This assumes that sha was used as a tag in the build job 
# See https://github.com/docker/metadata-action/issues/164 for discussion about the list
# of tags returned from metadata-action and using github.sha

if [ "$#" -ne 1 ]; then
  echo "Error: Expected 1 arg: github.sha "
  exit 1
fi

echo "debug $1"

echo "sha-"$(echo $1 | cut -c -7)
