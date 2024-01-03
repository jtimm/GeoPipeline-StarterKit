#!/bin/bash

# Downloaded Earthdata URLs text file
urls_file="input/earthdata-ges-disc/urls/subset_GPM_3IMERGDL_06_20240102_235953_.txt"

# Directory to save the files
output_dir="input/earthdata-ges-disc/dataset"

# Ensure the output directory exists
mkdir -p "$output_dir"

# Save the current directory
original_dir=$(pwd)

# Construct the absolute path of the urls_file
urls_file_abs_path="${original_dir}/${urls_file}"

# Change to the output directory
cd "$output_dir"

# Download the files
cat "$urls_file_abs_path" | tr -d '\r' | xargs -n 1 curl -LJO -n -c ~/.urs_cookies -b ~/.urs_cookies

# Return to the original directory
cd "$original_dir"
