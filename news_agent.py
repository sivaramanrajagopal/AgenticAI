{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO8F4/mWsmSAOyeX4tdzLo+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sivaramanrajagopal/AgenticAI/blob/main/news_agent.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install feedparser"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DC4ZrFd0srlW",
        "outputId": "2cb48ef0-e55d-4fa3-d6dd-920e761a12a9"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting feedparser\n",
            "  Downloading feedparser-6.0.11-py3-none-any.whl.metadata (2.4 kB)\n",
            "Collecting sgmllib3k (from feedparser)\n",
            "  Downloading sgmllib3k-1.0.0.tar.gz (5.8 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Downloading feedparser-6.0.11-py3-none-any.whl (81 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m81.3/81.3 kB\u001b[0m \u001b[31m877.1 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hBuilding wheels for collected packages: sgmllib3k\n",
            "  Building wheel for sgmllib3k (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for sgmllib3k: filename=sgmllib3k-1.0.0-py3-none-any.whl size=6047 sha256=ccb1826392c68bebaf76a1a10ae7ffdf21dcdd2090e0140ea6b4bcb226ea3fd6\n",
            "  Stored in directory: /root/.cache/pip/wheels/3b/25/2a/105d6a15df6914f4d15047691c6c28f9052cc1173e40285d03\n",
            "Successfully built sgmllib3k\n",
            "Installing collected packages: sgmllib3k, feedparser\n",
            "Successfully installed feedparser-6.0.11 sgmllib3k-1.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "UF9oOESKrWCY"
      },
      "outputs": [],
      "source": [
        "# news_agent.py\n",
        "\n",
        "# 1. Importing necessary libraries\n",
        "import feedparser  # For parsing RSS feeds\n",
        "from transformers import pipeline  # For text summarization using Hugging Face Transformers\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 2. Function to fetch news articles from an RSS feed\n",
        "def fetch_news(rss_url):\n",
        "    \"\"\"Fetches the top 5 news articles from a given RSS feed URL.\"\"\"\n",
        "    feed = feedparser.parse(rss_url)  # Parse the RSS feed\n",
        "    articles = []\n",
        "    for entry in feed.entries[:5]:  # Iterate through the first 5 entries (articles)\n",
        "        articles.append({\n",
        "            'title': entry.title,  # Extract the article title\n",
        "            'link': entry.link,  # Extract the article link\n",
        "            'summary': entry.summary  # Extract the article summary\n",
        "        })\n",
        "    return articles  # Return the list of extracted articles"
      ],
      "metadata": {
        "id": "hbH8NJCztKo7"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 3. Function to summarize an article's text (currently commented out in usage)\n",
        "def summarize_article(article_text):\n",
        "    \"\"\"Summarizes the given article text using a pre-trained summarization model.\"\"\"\n",
        "    summarizer = pipeline(\"summarization\")  # Load the summarization pipeline\n",
        "    summary = summarizer(article_text, max_length=60, min_length=30, do_sample=False)\n",
        "    # Generate the summary with specified length constraints\n",
        "    return summary[0]['summary_text']  # Return the summarized text"
      ],
      "metadata": {
        "id": "vjxBMYlBtPFT"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 4. Main execution block\n",
        "if __name__ == \"__main__\":\n",
        "    rss_url = \"http://feeds.bbci.co.uk/news/rss.xml\"  # Define the RSS feed URL\n",
        "    articles = fetch_news(rss_url)  # Fetch the news articles\n",
        "\n",
        "    # Print the title and link of each fetched article\n",
        "    for article in articles:\n",
        "        print(\"Title:\", article['title'])\n",
        "        print(\"Link:\", article['link'])\n",
        "        print(\"-\" * 50)  # Print a separator line\n",
        "\n",
        "        # (Optional) Fetch full article text and summarize it using summarize_article()\n",
        "        # This part is currently commented out but can be uncommented and implemented\n",
        "        # summary = summarize_article(article_text)\n",
        "        # print(\"Summary:\", summary)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MLFAL3q6tTDD",
        "outputId": "c55832e7-7b8f-40d5-d394-b7017f0856d0"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Title: Second Labour MP apologises over WhatsApp comments\n",
            "Link: https://www.bbc.com/news/articles/c1lv1gqgmdzo\n",
            "--------------------------------------------------\n",
            "Title: Teenagers say they were assaulted and mocked by nurses at psychiatric unit\n",
            "Link: https://www.bbc.com/news/articles/cx2kg2djkk2o\n",
            "--------------------------------------------------\n",
            "Title: Swift, Trump and a dynasty in ruins - how Super Bowl 59 unfolded\n",
            "Link: https://www.bbc.com/sport/american-football/articles/ckgyvyygd12o\n",
            "--------------------------------------------------\n",
            "Title: Kendrick Lamar's Super Bowl show was one big tease\n",
            "Link: https://www.bbc.com/news/articles/cz0l5m5m943o\n",
            "--------------------------------------------------\n",
            "Title: 'Billionaires own my mouldy rental property'\n",
            "Link: https://www.bbc.com/news/articles/c0rq2g0kz1lo\n",
            "--------------------------------------------------\n"
          ]
        }
      ]
    }
  ]
}