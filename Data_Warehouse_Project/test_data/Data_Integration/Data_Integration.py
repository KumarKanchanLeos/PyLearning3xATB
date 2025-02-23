import pandas as pd

Customer=pd.DataFrame({
    "CustomerId":[123,456,789,1011],
    "CustomerName":["Alice","Bob","Kalavati","Rani"]
})

Transactions= pd.DataFrame({
    "TransactionId":[1,2,3,4,5],
    "CustomerId":[123,456,789,999,1011],
    "Amount":[100,200,150,300,400]
})

Customer["CustomerId"]=Customer["CustomerId"].astype(str).str.strip()
Transactions["CustomerId"]=Transactions["CustomerId"].astype(str).str.strip()

merged_records=pd.merge(Customer,Transactions,on ='CustomerId',how="inner",indicator = True)

All_records=pd.merge(Customer,Transactions,on ='CustomerId',how ="outer",indicator=True)
mismatched_records= All_records[All_records["_merge"]!="both"]

print(mismatched_records)