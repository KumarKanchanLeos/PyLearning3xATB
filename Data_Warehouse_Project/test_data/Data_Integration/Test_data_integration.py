import pytest
from .Data_Integration import merged_records,mismatched_records

def test_data_integration():
    assert len(merged_records)>0,"no matching record"
    assert len(mismatched_records)>0,"no mismathed records"
    print("passed the dataintegration")


test_data_integration()