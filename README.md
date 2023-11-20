# GPT Knowledge Base Generator

## Overview

This tool serves as a data scraper to generate knowledge bases tailored for GPT-related applications, such as training assistants and GPTs. It utilizes DuckDuckGo search to fetch relevant information, allowing users to create custom knowledge bases.

## Installation

To install, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alluding/gpt-knowledge-scraper.git
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
## Usage

### Basic Usage

```python
from typing import Optional, List
from scraper import DataScrape

scraper: DataScrape = DataScrape("lil uzi vert", max_results=50)
results: List[SearchResult] = scraper.search()

output_data: List[dict] = []
for info in results:
    output_data.append({
        "title": info.title,
        "body": info.body,
        "href": info.href,
        "scraped_content": info.scraped_content if info.scraped_content else "Not available"
    })

with open('output.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=4)
```

### Example Queries and Results

- **Query: "lil uzi vert"**
  - *Result 1:*
    - Title: `Lil Uzi Vert - Wikipedia`
    - Body: `Symere Bysil Woods...`
    - URL: `https://en.wikipedia.org/wiki/Lil_Uzi_Vert`
    - Scraped Content: `Lil Uzi Vert, is an American rapper, singer, and songwriter...`

- **Query: "GPT-3 assistants"**
  - *Result 1:*
    - Title: `How GPT-3 is revolutionizing AI Assistants`
    - Body: `The advent of GPT-3...`
    - URL: `https://example.com/gpt-3-assistants`
    - Scraped Content: `GPT-3, with its vast language understanding...`

### Contributing

I welcome contributions to enhance this tool! Feel free to submit issues or pull requests for improvements or new features.

### License

This project is licensed under the [MIT License](LICENSE).

---
