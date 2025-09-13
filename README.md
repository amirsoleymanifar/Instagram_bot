# Instagram_bot
# Instagram Bot 🤖

A simple Instagram automation bot built with **Python** and **Selenium**.

This bot is designed to automate some Instagram actions such as:
- Logging in to your account
- Browsing posts under specific hashtags
- Following users
- Liking posts
- Occasionally leaving comments

> ⚠️ **Disclaimer:** Using automation on Instagram is against their Terms of Service.  
> Excessive use may result in temporary or permanent account bans.  
> Use this bot **at your own risk**.

---

## 📝 Features

1. **Login Automation**
   - Automatically logs into Instagram using credentials from `.env`.
   
2. **Hashtag Browsing**
   - Visits posts under a configurable list of hashtags.

3. **Follow Users**
   - Follows users who have not been followed before.

4. **Like Posts**
   - Likes the current post automatically.

5. **Comment Randomly**
   - Posts one of several predefined comments with a probability (~30%) to reduce detection.

6. **Configurable Limits**
   - You can limit the number of posts visited per hashtag to reduce the risk of account restrictions.

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/instagram-bot.git
cd instagram-bot
