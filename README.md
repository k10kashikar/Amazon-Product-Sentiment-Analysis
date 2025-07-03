# Amazon Product Sentiment Analysis

This project extracts product details and customer reviews from Amazon, performs sentiment analysis on the reviews, and provides a visual report of the sentiments using bar graphs and pie charts. Additionally, it offers a suggestion on whether to consider buying the product based on the sentiment analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/amazon-product-sentiment-analysis.git
    ```
2. Navigate to the project directory:
    ```sh
    cd amazon-product-sentiment-analysis
    ```
3. Install the required packages:
    ```sh
    pip install pandas numpy matplotlib beautifulsoup4 selenium textblob
    ```
4. Download and install [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your PATH.

## Usage

1. Update the `URL` variable in the `main()` function with the Amazon product URL you want to analyze.
2. Run the script:
    ```sh
    python main.py
    ```
3. The script will output the product details, perform sentiment analysis on the reviews, and display the sentiment analysis report as bar graphs and pie charts. It will also provide a suggestion on whether to buy the product based on the sentiment analysis.

## Functions

### `get_title(soup)`

Extracts the product title from the BeautifulSoup object.

### `get_price(soup)`

Extracts the product price from the BeautifulSoup object.

### `get_rating(soup)`

Extracts the product rating from the BeautifulSoup object.

### `get_review_count(soup)`

Extracts the number of user reviews from the BeautifulSoup object.

### `get_availability(soup)`

Extracts the availability status of the product from the BeautifulSoup object.

### `get_reviews(url)`

Fetches customer reviews using Selenium and returns a list of review texts.

### `analyze_sentiment(review)`

Performs sentiment analysis on a review text and returns the sentiment as 'positive', 'negative', or 'neutral'.

## Examples

Here is an example of how to use this project:

```python
# The webpage URL
URL = "https://www.amazon.in/..."

# Run the main function
main()
