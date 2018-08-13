import pandas as pd
import sys


def normalize(infile, abbreviation_file):
    df = pd.read_csv(infile)

    # Join the state name crosswalk file
    state_abbreviation_crosswalk = pd.read_csv(abbreviation_file, index_col='state_abbr')
    df = df.join(state_abbreviation_crosswalk, on="state")

    # Strip multiple spaces, line breaks from bio
    df['bio'] = df['bio'].str.replace(r'\s+', ' ')

    # Write to stdout
    df.to_csv(sys.stdout)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Wrong number of arguments. You must provide a filename to be processed and a path to the abbreviation crosswalk. See the README for more details.', file=sys.stderr)

    infile = sys.argv[1]
    abbreviationfile = sys.argv[2]

    normalize(infile, abbreviationfile)
