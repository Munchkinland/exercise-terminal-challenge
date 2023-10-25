#!/bin/bash

# Base directory
base_directory="/C/Users/Rubén/Documents/GitHub/exercise-terminal-challenge"

# CSV file headers
echo "Name,Size,Last Modification Date" > information_files.csv

# Use find to list files and obtain their information
find "$base_directory" -type f -exec stat --format="%n,%s,%Y" {} \; >> information_files.csv