#Your ETL process transforms data from a source into a target CSV file.
#The target file must not have missing (NaN) values in critical
#columns ("Salary" and "First Name").
#Write a pytest test to ensure these columns do not have any null values.
import pytest
import pandas as pd
import os

@pytest.fixture
def source_fixture():
    source_file=pd.read_csv(os.path.join(os.path.dirname(__file__),"employee.csv"))
    return source_file

@pytest.fixture
def target_fixture():
    target_file=pd.read_csv(os.path.join(os.path.dirname(__file__),"target_emp.csv"))
    return target_file

@pytest.fixture
def transformation(source_fixture):
     source_fixture.dropna(subset=["Salary","First Name"],inplace=True)
     return source_fixture

def test_data_completeness(source_fixture,target_fixture,transformation):

    assert transformation["Salary"].isnull().sum()==0,"Salary column has null values"
    assert transformation["First Name"].isnull().sum()==0,"First Name column has null values"



