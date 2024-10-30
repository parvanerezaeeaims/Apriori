from tabulate import tabulate  
from apyori import apriori
import pandas as pd


def apriori_product(data,min_support, min_confidence, min_lift):
    data.rename(columns={
    'شماره مشتری': 'CID', 
    'تاریخ': 'date',
    'نام کالا': 'stock_name'
    }, inplace=True)  
    df = data[data.quantity > 0]  
    data_temp = df.copy()  
    data_temp['stock_name'] = data_temp['stock_name'] + ','  
    grouped = data_temp.groupby(['CID', 'date']).agg({'stock_name': 'sum'})  
    records = []  
    
    for line in grouped['stock_name']:  
        items = line.split(',')  
        temp = []  
        for item in items:  
            if item.strip() != '':  
                temp.append(item)  
        records.append(temp)  

    result = apriori(records, min_support=min_support,min_confidence=min_confidence, min_lift=min_lift)  
    
    # Prepare the table data  
    table = []  
    for res in result:  
        for item in res[2]:  
            table.append([  
                ', '.join(list(item.items_base)) ,  
                ', '.join(list(item.items_add)),  
                res[1],            # Support  
                item.confidence,   # Confidence  
                item.lift         # Lift  
            ])  
    
    # Create a formatted table  
    headers = ["Items Base", "Items Add", "Support", "Confidence", "Lift"]  
    table_output = pd.DataFrame(table,columns=headers)  
    
    return table_output


 