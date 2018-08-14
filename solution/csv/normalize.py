import pandas as pd
import sys

from datetime import datetime
from dateutil.parser import parse


def join_crosswalk(df, state_abbreviation_crosswalk):
    """
    Join dataframe with state abbreviations to add full state name column.
    """
    return df.join(state_abbreviation_crosswalk, on="state")


def clean_bio(df):
    """
    Strip line breaks, multiple spaces, leading/trailing whitespace from bio
    field.
    """
    series = df['bio'].str.replace(r'\s+', ' ')
    return series.str.strip()


def clean_dates(df):
    """
    Return cleaned date columns
    """
    return zip(*df['start_date'].map(_clean_dates))


def _clean_dates(datestring):
    """
    Parse valid dates to YYYY-MM-DD format, dump bad dates into
    start_date_description field.
    """
    try:
        parsed = datetime.strptime(datestring, '%m/%y')
        start_date = parsed.strftime('%Y-%m-%d')
        start_date_description = None
    except ValueError:
        try:
            parsed = parse(datestring)
            start_date = parsed.strftime('%Y-%m-%d')
            start_date_description = None
        except ValueError:
            start_date = None
            start_date_description = datestring

    return start_date, start_date_description


def normalize(infile, abbreviation_file):
    df = pd.read_csv(infile)

    # Join the state name crosswalk file
    state_abbreviation_crosswalk = pd.read_csv(abbreviation_file, index_col='state_abbr')
    df = join_crosswalk(df, state_abbreviation_crosswalk)

    # Strip multiple spaces, line breaks from bio
    df['bio'] = clean_bio(df)

    # Clean dates
    df['start_date'], df['start_date_description'] = clean_dates(df)

    # Write to stdout
    df.to_csv(sys.stdout)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Wrong number of arguments. You must provide a filename to be processed and a path to the abbreviation crosswalk. See the README for more details.', file=sys.stderr)

    infile = sys.argv[1]
    abbreviationfile = sys.argv[2]

    normalize(infile, abbreviationfile)
