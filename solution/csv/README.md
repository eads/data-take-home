# Homework solution: Normalize CSV

We strongly recommend creating a virtualenv before performing the steps below.

Edgar must be running locally.

This script takes two input files, the datafile to be a cleaned and state abbreviation file, and writes results to stdout.

## Prerequisites

* Python 3

## Install requirements

`pip install -r requirements.txt`

## Clean the data

```
python normalize.py ../../files/data.csv ../../files/state_abbreviations.csv > enriched.csv
```

The script's arguments refer to the data file to be processed and a state abbreviation file. You may use absolute paths or refer to files outside the repository.

## Date parsing behavior

Partial dates are transformed into "None" values and the `start_date_description` field is set to `Incomplete: <original date string>`.

Unparseable dates are transformed into "None" values and the `start_date_description` field is set to `Invalid: <original date string>`.

Parseable dates are transformed into `YYYY-MM-DD` format and `start_date_description` is set to a "None" value.

## Run tests

```
pytest
```
