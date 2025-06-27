import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from textblob import TextBlob

# Function to extract Product Title

# Function to extract Product Title
def get_title(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'})
        title_value = title.text
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
    except AttributeError:
        try:
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
        except:
            price = ""
    return price

# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""
    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review_count = ""
    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()
    except AttributeError:
        available = "Not Available"
    return available

# Function to fetch customer reviews using Selenium
def get_reviews(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)  # You need to have Chrome WebDriver installed
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = soup.find_all("span", {"data-hook": "review-body"})
    review_texts = [review.get_text(strip=True) for review in reviews]
    driver.quit()
    return review_texts

# Function to perform sentiment analysis
def analyze_sentiment(review):
    blob = TextBlob(review)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0.2:
        return 'positive'
    elif sentiment_score < -0.2:
        return 'negative'
    else:
        return 'neutral'


# Main function
def main():
    # The webpage URL
    URL = "https://www.amazon.in/Amazon-Brand-Symbol-Regular-AW-SY-MCS-1143_Light/dp/B08JR292QM/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.s1uAyCO-VxedSda5J9t-TM-ndRr0_CTKGmQuGntUMr6IvMCLHf-t3bZ1SpLOCbAGxQwn8PfdKvGf0-t5Vv3XJNAkjDlLpUN91ttJY-2aGKXF3TXim5QX8qxWiS518yJbY-vmltj_XNnI3HtT4NVnDkz41sGiB4cmS0Klykp5y9XuxJKeIE4b6DxdLXZOGQftka0ovwuhxA_W_q2R7R3TYOrvLRoR_-ojXkZxevRoD3n0c5Uvxt7BN2vLinTscbgUJbq6pAYWcCG89ErUic0kLeDR0GE8A9GXjbLmG9fQamo.8zpZBmaxVQv6Qe_ViZmlXKiFdCk0DsV2EDwqK9TiZtg&dib_tag=se&keywords=shirts&qid=1713976623&refinements=p_72%3A1318478031&rnid=1318475031&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1"

    # Soup Object containing all data
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    title = get_title(soup)
    price = get_price(soup)
    rating = get_rating(soup)
    review_count = get_review_count(soup)
    availability = get_availability(soup)

    reviews = get_reviews(URL)

    print("Title:", title)
    print("Price:", price)
    print("Rating:", rating)
    print("Review Count:", review_count)
    print("Availability:", availability)

    # Perform sentiment analysis on reviews
    sentiments = [analyze_sentiment(review) for review in reviews]

    # Generate data analysis report (bar graph and pie chart)
    sentiment_counts = pd.Series(sentiments).value_counts()
    labels = ['positive', 'negative', 'neutral']  # Ensure all labels are included
    sizes = [sentiment_counts.get(label, 0) for label in labels]
    colors = {'positive': 'lightgreen', 'negative': 'lightcoral', 'neutral': 'lightskyblue'}

    # Plotting
    plt.figure(figsize=(14, 6))

    # Bar graph
    plt.subplot(1, 2, 1)
    plt.bar(labels, sizes, color=[colors[label] for label in labels], edgecolor='black')
    plt.xlabel('Sentiment', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.title('Sentiment Analysis of Amazon Product Reviews (Bar Graph)', fontsize=14)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(sizes, labels=labels, colors=[colors[label] for label in labels], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Sentiment Analysis of Amazon Product Reviews (Pie Chart)', fontsize=14)

    # Add legend
    plt.legend(labels, loc="upper right", fontsize=10)

    plt.tight_layout()
    plt.show()

    # Suggest whether to buy the product based on sentiment analysis
    if sentiment_counts.get('positive', 0) > sentiment_counts.get('negative', 0):
        print("Based on sentiment analysis, it is suggested to consider buying the product.")
    else:
        print("Based on sentiment analysis, it is suggested to reconsider buying the product.")

    driver.quit()

if __name__ == "__main__":
    main()
