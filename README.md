# GeoPipeline-StarterKit

A foundational template to build more complex geospatial pipelines

## Description

This project creates a basic geospatial data processing pipeline that extracts a small dataset from a public geospatial data source, performs a simple transformation (like reformatting or basic analysis), and then uploads it to AWS S3. This pipeline will be set up with a basic CI/CD process using GitLab CI and will serve as a template for future, more complex geospatial data processing projects.

## Modules Used

- `notebook`: Jupyter Notebooks provides an interactive environment for your data processing and visualization tasks.
- `pandas`: A powerful Python data analysis toolkit, ideal for data manipulation and cleaning.
- `rasterio`: Handles raster data (like satellite imagery) in Python, making it a crucial tool for geospatial data processing.
- `requests`: A simple, yet powerful, HTTP library for Python, used for making API calls (such as to retrieve data from NASA EarthData).
