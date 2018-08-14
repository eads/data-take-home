# Homework solution: Scraper

We strongly recommend creating a virtualenv before performing the steps below.

Edgar must be running locally.

## Prerequisites

* Python 3

## Install requirements

`pip install -r requirements.txt`

## Clean the data

```
python normalize.py ../../files/data.csv ../../files/state_abbreviations.csv > enriched.csv
```

## Run tests

```
pytest
```
