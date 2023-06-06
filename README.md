# URL Shortener

The URL Shortener is a web application built with Python and Flask that allows users to generate shortened URLs for long URLs. It provides a simple and convenient way to share long URLs in a concise format.

## Purpose

The purpose of this project is to demonstrate how to create a basic URL shortener using the Flask web framework. It showcases the use of Flask for handling HTTP requests, generating random short URLs, and redirecting users to the original long URLs.

## How It Works

The URL Shortener project utilizes the following components and concepts:

- Flask: A lightweight web framework for building web applications in Python.
- Random string generation: Randomly generated strings are used to create unique short URLs for each long URL.
- Dictionary storage: The original long URLs and their associated short URLs are stored in a Python dictionary.

### Setup

To set up and run the URL Shortener project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/url-shortener.git```
   
2. Navigate to the project directory:

  ```bash
    cd url-shortener
  ```
3. Create a virtual environment (optional but recommended):
```bash
    python3 -m venv venv
  ```
5. Activate the virtual environment:
* On macOS and Linux:
  ```bash
    source venv/bin/activate
  ```
* On Windows:
  ```bash
    venv\Scripts\activate
  ```
7. Install the required packages:
```bash
    pip install -r requirements.txt
  ```

### Running the Application

1. Start the Flax development server:
  ```bash
    python app.py
  ```
  
2. Access the URL Shortener application in your web browser at `http://localhost:5000/`.

### Usage

1. Enter a long URL into the input field on the homepage and click the "Shorten" button.
2. The application will generate a short URL for the entered long URL.
3. Copy the short URL and share it with others.
4. When someone visits the short URL, they will be redirected to the original long URL.

### Contributing
Contributions to the URL Shortener project are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or create an issue.

### License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).
