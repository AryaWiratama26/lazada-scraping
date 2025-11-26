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
- file_type: file type (csv, txt, xlsx). Default = csv
"""
bot = LazadaBot()
bot.scrap(keyword="iphone", n_data=40, output_file="iphone_price", file_type="csv")
bot.scrap(keyword="iphone", n_data=40, output_file="iphone_price", file_type='txt')
bot.scrap(keyword="iphone", n_data=40, output_file="iphone_price", file_type='xlsx')
```

4. Run

```bash
python3 main.py
```

5. Output Format

```csv
Title,Price,Sold
Apple iPhone 16,14999000,29
```

```txt
Title,Price,Sold
Apple iPhone 16,14999000,29
```

```xlsx
Title,Price,Sold
Apple iPhone 16,14999000,29
```

## How to use website (Flask)

1. Clone This Repo

```bash
git clone https://github.com/AryaWiratama26/lazada-scraping.git
```

2.  Install Requirements

```bash
pip install -r requirements.txt
```

3. Change Directory to website

```bash
cd website
```

4. Run

```bash
python3 app.py
```

5. Open Browser (Localhost)

```bash
http://127.0.0.1:5000
```

## Demo Video
[Demo Video](https://youtu.be/4KoSwTOvX2o?si=Cp5EZ8T4uLWd3MpF)

[Output CSV Example](/iphone_price.csv) <br>
[Output TXT Example](/iphone_price.txt) <br>
[Output XLSX Example](/iphone_price.xlsx)

