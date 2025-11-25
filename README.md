# Lazada Scraping

Scraping data from Lazada using selenium. This is a simple project to learn selenium and scraping data from website.

## How to use

1. Clone This Repo

```bash
git clone https://github.com/AryaWiratama26/lazada-scraping.git
```

2.  Install Requirements

```bash
pip install -r requirements.txt
```

3. Scrap Data

```python
from sources import LazadaBot

"""

- keyword: keyword to search
- n_data: number of data to scrap
- output_file: output file name
- file_type: file type. Default = csv
"""
bot = LazadaBot()
bot.scrap(keyword="iphone", n_data=40, output_file="iphone_price", file_type="csv")
bot.scrap(keyword="iphone", n_data=40, output_file="iphone_price", file_type='txt')
```

4. Run

```bash
python3 main.py
```