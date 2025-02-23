import pandas as pd

class Custom_Error(Exception):
    pass

def data_completness(file_path_source,file_path_target):
    source_employee=pd.read_csv(file_path_source)
    target_employee= pd.read_csv(file_path_target)

    source_rows =  len(source_employee)
    target_rows = len(target_employee)
    if source_rows!=target_rows:
        raise Custom_Error("source and target are not equal")

    return source_rows,target_rows