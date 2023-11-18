def select_all(table_name:str, ):
    return f"SELECT * FROM {table_name};"

print(select_all('sales'))