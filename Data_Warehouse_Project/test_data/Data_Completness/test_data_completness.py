import pytest
from main_data_completness import data_completness

def test_data_completness():
    file_path_source = r"/Data_Warehouse_Project/test_data/Data_Completness/employee_completness.csv"
    file_path_target = r"/Data_Warehouse_Project/test_data/Data_Completness/employee_completness_target.csv"

    target_rows = 100
    source_rows,target_rows=data_completness(file_path_source,file_path_target)
    with pytest.raises(Custom_Error):
        data_completness(file_path_source,file_path_target)
    assert source_rows==target_rows,f"expected records {source_rows} but got {target_rows}"
