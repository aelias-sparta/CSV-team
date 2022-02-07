from extract_csv import *
import unittest

class TestExtractCSV(unittest.TestCase):

    def test_academy(self):
        test_academy = ExtractCSV('data-26-final-project-files', 'Academy')

        assert isinstance(test_academy.csv_file_names, list)
        assert isinstance(test_academy.df, pd.DataFrame)
        assert 'Academy/Business_21_2019-03-18.csv' in test_academy.csv_file_names
        assert len(test_academy.csv_file_names) == 36
        assert len(test_academy.df) == 397
        assert len(test_academy.df.columns) == 62

    def test_talent(self):
        test_talent = ExtractCSV('data-26-final-project-files', 'Talent')

        assert isinstance(test_talent.df, pd.DataFrame)
        assert isinstance(test_talent.csv_file_names, list)
        assert 'Talent/April2019Applicants.csv' in test_talent.csv_file_names
        assert len(test_talent.csv_file_names) == 12
        assert len(test_talent.df) == 4691
        assert len(test_talent.df.columns) == 14


if __name__ == '__main__':
    unittest.main()