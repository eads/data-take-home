import pandas as pd
import sys

from dateutil.parser import parse


def clean_dates(datestring):
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
    df = df.join(state_abbreviation_crosswalk, on="state")

    # Strip multiple spaces, line breaks from bio
    df['bio'] = df['bio'].str.replace(r'\s+', ' ')

    # Clean dates
    df['start_date'], df['start_date_description'] = zip(*df['start_date'].map(clean_dates))

    # Write to stdout
    df.to_csv(sys.stdout)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Wrong number of arguments. You must provide a filename to be processed and a path to the abbreviation crosswalk. See the README for more details.', file=sys.stderr)

    infile = sys.argv[1]
    abbreviationfile = sys.argv[2]

    normalize(infile, abbreviationfile)
