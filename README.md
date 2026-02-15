# JSON to VCF Converter

A simple and offline web application to convert JSON contact files to VCF (vCard) format.

This tool allows users to upload a JSON file containing contact information and convert it into a downloadable VCF file. It works entirely offline, with no need for an internet connection after the page is loaded.

## Features

- **Offline processing**: No server or internet connection required.
- **JSON to VCF conversion**: Upload a JSON file and download the converted VCF file instantly.
- **Easy to use**: Just upload the JSON file, and click to download the VCF file.
- **Minimalistic design**: Clean and simple interface to enhance user experience.

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Fonts**: Google Fonts (Poppins)

## How It Works

1. The user uploads a JSON file through the provided file input.
2. The uploaded JSON is processed by the backend Python script (`app.py`).
3. The user can download the converted VCF file immediately after processing.
