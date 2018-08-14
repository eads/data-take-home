import normalize
import pandas as pd
import pytest


DATESTRINGS = [
    ('March 12, 2000', ('2000-03-12', None)),
    ('July 1994', (None, 'Incomplete: July 1994')),
    ('02/07', (None, 'Incomplete: 02/07')),
    ('Impedit eum ipsam.', (None, 'Invalid: Impedit eum ipsam.')),
    ('04/09/1970', ('1970-04-09', None)),
    ('1970-09-05', ('1970-09-05', None)),
]

df = pd.read_csv('../../files/data.csv')
state_abbreviation_crosswalk = pd.read_csv('../../files/state_abbreviations.csv', index_col='state_abbr')


def test_join():
    test_df = normalize.join_crosswalk(df, state_abbreviation_crosswalk)
    assert test_df.ix[0].to_dict()['state_name'] == 'Kansas'


def test_clean_bio():
    test_df = df.copy()
    test_df['bio'] = normalize.clean_bio(test_df)
    assert test_df.ix[2].to_dict()['bio'] == 'Sed vitae dolorem quae totam sequi fuga odit. Eaque alias quisquam blanditiis veniam. Aut perferendis sint deleniti accusamus quod.'


@pytest.mark.parametrize("datestring,expected", DATESTRINGS)
def test_clean_dates(datestring, expected):
    assert normalize._clean_dates(datestring) == expected
