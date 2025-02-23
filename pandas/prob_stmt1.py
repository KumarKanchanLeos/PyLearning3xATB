#You have a source CSV file and a target CSV file generated
# by an ETL process. The ETL pipeline should ensure that all
# rows from the source are transformed and loaded into the target.
# Write a pytest function to compare the row counts of the source
# and target files.import pytest
import pandas as pd
import pytest
import os

@pytest.fixture
def source_fixture():
    source_file=pd.read_csv(os.path.join(os.path.dirname(__file__),"employee.csv"))
    return source_file

@pytest.fixture
def target_fixture():
    target_file=pd.read_csv(os.path.join(os.path.dirname(__file__),"target_emp.csv"))
    return target_file

def test_data_completeness(source_fixture,target_fixture):
    assert source_fixture.shape[0]==target_fixture.shape[0],"source and target are not same"



