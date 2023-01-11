# LAB 17 - Class 401d20

## Web Scraper

### Author: DeShon Dixon

---

## Overview

- Scrapes Wikipedia page and records which passages need citations.
- Web scraper reports the number of citations needed.
- Web scraper identifies those cases and includes the relevant passage.
- The “relevant passage” is the parent element that contains the passage.
---
- get_citations_needed_count function
  - Takes in an url string and returns an integer.

- get_citations_needed_report function
  - Takes in an url string and returns a report string
  - The string is formatted with each citation listed in the order found.

---

## Setup

- Create repo on desktop

- Create virtual environment: python3.11 -m venv .venv

- Activate environment: source .venv/bin/activate

- Install requests: pip install requests

- Install beautifulsoup: pip install beautifulsoup4

## Sources

https://www.crummy.com/software/BeautifulSoup/bs4/doc/


