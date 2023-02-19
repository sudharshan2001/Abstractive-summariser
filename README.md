# Abstractive-summariser

## Schlumberger's New Year Hackathon (Finalist)

Problem Statement: scrape the given URL of News feed and summarize the texts

# Approach

I used a pre-trained transformer called Pegasus which was trained on CNN-daily mail.

Pegasus(Pre-training with Extracted Gap-sentences for Abstractive Summarization) is an abstractive summarization model. It summarises the whole text instead of extracting its important parts.

I fine-tuned the Pegasus model on News summarization data (Xsum and Multi-News dataset) and trained it
