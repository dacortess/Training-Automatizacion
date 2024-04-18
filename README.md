# Employment Page Web Scraper

This project is a web scraper designed to extract employmet information from web pages. It utilizes the BeautifulSoup library to parse HTML and extract relevant data. Each employee's information is encapsulated within an object for easy manipulation and analysis.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/dacortess/Training-Automatizacion.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Training-Automatizacion
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the scraper, simply run the `main.py` script and provide the URL of the employee page you want to scrape. The script will extract the necessary information using objects and store it in a csv file.

```bash
python scraper.py https://example.com/employee-page
```

## Features

- Scrapes employment information from web pages
- Uses BeautifulSoup for HTML parsing
- Manage data with objects for easy manipulation
