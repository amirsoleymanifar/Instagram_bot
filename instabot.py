import os
import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv


# ---------------------------
# Load environment variables
# ---------------------------
# Credentials are stored in a separate .env file for security
# Example .env file:
# IG_USERNAME=your_username
# IG_PASSWORD=your_password
load_dotenv()

INSTAGRAM_USER = os.getenv("IG_USERNAME")
INSTAGRAM_PASS = os.getenv("IG_PASSWORD")

if not INSTAGRAM_USER or not INSTAGRAM_PASS:
    raise ValueError("⚠️ Please set IG_USERNAME and IG_PASSWORD in your .env file")


# ---------------------------
# Setup WebDriver
# ---------------------------
CHROMEDRIVER_PATH = "C:/Users/ASUS/Desktop/New folder/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
wait = WebDriverWait(driver, 15)


# ---------------------------
# Functions
# ---------------------------
def login(username, password):
    """
    Log into Instagram using provided credentials.
    """
    driver.get("https://www.instagram.com/accounts/login/")
    wait.until(EC.presence_of_element_located((By.NAME, "username")))

    user_input = driver.find_element(By.NAME, "username")
    pass_input = driver.find_element(By.NAME, "password")

    user_input.send_keys(username)
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.ENTER)

    # Handle "Not Now" pop-up if it appears
    try:
        not_now = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9--._a9_1"))
        )
        not_now.click()
    except:
        pass


def follow_user():
    """
    Follow the owner of the current post if not already followed.
    Returns True if a follow action was performed, otherwise False.
    """
    try:
        follow_button = driver.find_element(By.XPATH, "//header//button")
        if follow_button.text.lower() == "follow":
            follow_button.click()
            return True
    except:
        return False
    return False


def like_post():
    """
    Like the current post.
    Returns True if a like action was performed, otherwise False.
    """
    try:
        like_button = driver.find_element(
            By.XPATH, "//section//span[@class='_aamw']/button"
        )
        like_button.click()
        return True
    except:
        return False


def comment_post():
    """
    Leave a random comment on the current post with ~30% probability.
    Returns True if a comment was posted, otherwise False.
    """
    try:
        comm_prob = randint(1, 10)
        if comm_prob > 7:  # Only comment occasionally to reduce risk
            comment_btn = driver.find_element(
                By.XPATH, "//section//span[@class='_aamx']/button"
            )
            comment_btn.click()

            comment_box = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "textarea"))
            )

            messages = [
                "Really cool!",
                "Nice work :)",
                "Nice gallery!!",
                "So cool! :)",
            ]
            comment_box.send_keys(messages[randint(0, len(messages) - 1)])
            comment_box.send_keys(Keys.ENTER)
            return True
    except:
        return False
    return False


# ---------------------------
# Main Script
# ---------------------------
def main():
    """
    Main execution of the bot:
    - Login
    - Browse hashtags
    - Follow users
    - Like posts
    - Occasionally comment
    """
    login(INSTAGRAM_USER, INSTAGRAM_PASS)

    hashtag_list = ["bmw", "panamera", "mercedes"]
    new_followed = []
    likes = 0
    comments = 0

    for hashtag in hashtag_list:
        driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        time.sleep(randint(3, 5))

        # Open the first post from the hashtag
        first_thumbnail = wait.until(EC.element_to_be_clickable((By.XPATH, "//article//a")))
        first_thumbnail.click()
        time.sleep(2)

        for i in range(1, 15):  # Limited to reduce ban risk
            # Follow user
            if follow_user():
                username = driver.find_element(By.XPATH, "//header//a").text
                new_followed.append(username)
                time.sleep(randint(3, 6))

            # Like post
            if like_post():
                likes += 1
                time.sleep(randint(2, 4))

            # Comment on post
            if comment_post():
                comments += 1
                time.sleep(randint(5, 7))

            # Go to the next post
            try:
                next_btn = driver.find_element(By.LINK_TEXT, "Next")
                next_btn.click()
                time.sleep(randint(3, 6))
            except:
                break

    print(f"✅ Done! Liked {likes} posts, Commented {comments}, Followed {len(new_followed)} users.")
    driver.quit()


if __name__ == "__main__":
    main()
