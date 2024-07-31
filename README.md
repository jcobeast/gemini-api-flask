# Generative AI with Gemini API and Flask

This project demonstrates the use of Generative AI with the Gemini API integrated into a Flask web application.

## Table of Contents

-   [Introduction](#introduction)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [API Endpoints](#api-endpoints)
-   [Dependencies](#dependencies)

## Introduction

This project showcases how to use Generative AI capabilities through the Gemini API within a Flask web application. It allows users to generate content based on provided inputs through a web interface.

## Features

-   Generate AI content using the Gemini API.
-   Simple and user-friendly web interface.
-   Extensible codebase for further customization and features.

## Installation

To get started with this project, follow the steps below:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/jcobeast/gemini-api-flask.git
    gemini-api-flask

    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    ```bash
    GEMINI_API_KEY=your_gemini_api_key # Go to your .env file and change to your own API key
    ```

5. **Run the flask application:**
    ```bash
    flask run
    ```

## Usage

Once the Flask server is running, navigate to http://127.0.0.1:9000/ in your web browser. You can use the provided interface to generate content by interacting with the Generative AI model through the Gemini API.

## API Endpoints

GET /: Home page with input form for content generation.
POST /generate: Endpoint to handle content generation requests.

## Dependencies

The project requires the following dependencies to be installed:

Flask: A micro web framework for Python.
Python-dotenv: A library to load environment variables from a .env file.
Gemini API SDK: The SDK provided by Gemini API (if available) or direct API calls using requests.
All dependencies are listed in the requirements.txt file.
