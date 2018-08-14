import normalize
import pandas as pd

df = pd.read_csv('../../files/data.csv')
state_abbreviation_crosswalk = pd.read_csv('../../files/state_abbreviations.csv', index_col='state_abbr')


def test_join():
    test_df = normalize.join_crosswalk(df, state_abbreviation_crosswalk)
    assert test_df.ix[0].to_dict()['state_name'] == 'Kansas'


def test_clean_bio():
    test_df = df.copy()
    test_df['bio'] = normalize.clean_bio(test_df)
    assert test_df.ix[2].to_dict()['bio'] == 'Sed vitae dolorem quae totam sequi fuga odit. Eaque alias quisquam blanditiis veniam. Aut perferendis sint deleniti accusamus quod.'


def test_clean_partial_date():
    test_df = df.copy()
    test_df['start_date'], test_df['start_date_description'] = normalize.clean_dates(test_df)
    assert test_df.ix[0].to_dict()['start_date'] == '2006-10-01'
    assert test_df.ix[0].to_dict()['start_date_description'] is None


def test_clean_bad_date():
    test_df = df.copy()
    test_df['start_date'], test_df['start_date_description'] = normalize.clean_dates(test_df)
    assert test_df.ix[1].to_dict()['start_date'] is None
    assert test_df.ix[1].to_dict()['start_date_description'] == 'Voluptatem odio.'

def test_clean_good_date():
    test_df = df.copy()
    test_df['start_date'], test_df['start_date_description'] = normalize.clean_dates(test_df)
    assert test_df.ix[7].to_dict()['start_date'] == '1994-10-20'
    assert test_df.ix[7].to_dict()['start_date_description'] is None
