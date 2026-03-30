import pandas as pd
import random
from faker import Faker
from sqlalchemy import create_engine
from collections import defaultdict

fake = Faker()

engine = create_engine('mysql+pymysql://root:<pwd>@127.0.0.1/wms_db', echo=False)

# Employee Table

fake_data = defaultdict(list)
employee_roles = ['Regional', 'Inventory', 'Supply Chain']

for _ in range(1000):
    fake_data["ssn"].append(int(fake.unique.ssn().replace("-", "")))
    fake_data["emp_name"].append(fake.name())
    fake_data["salary"].append(int(fake.pydecimal(left_digits=6, right_digits=2, min_value=40000, max_value=120000)))
    fake_data["emp_role"].append(random.choice(employee_roles))

df_emp = pd.DataFrame(fake_data)

df_emp.to_sql('Employee', con=engine, index=False, if_exists='append')
print("Inserted", len(df_emp), "rows into Employee table")

fake_data.clear()

# Warehouse Table

fake_data = defaultdict(list)
regional_ssns = df_emp[df_emp["emp_role"] == "Regional"]["ssn"].tolist()

for i in range(50):
    fake_data["warehouse_id"].append((i+1))
    fake_data["address"].append(fake.unique.address())
    fake_data["regional_manager_ssn"].append(random.choice(regional_ssns))

df_ware = pd.DataFrame(fake_data)

df_ware.to_sql('Warehouse', con=engine, index=False, if_exists='append')
print("Inserted", len(df_ware), "rows into Warehouse table")

fake_data.clear()

# Rack Table

fake_data = defaultdict(list)
warehouses = df_ware["warehouse_id"].tolist()

for i in range(200):
    fake_data["rack_id"].append((i+1))
    fake_data["warehouse_id"].append(random.choice(warehouses))
    fake_data["aisle_section"].append(f"Section-{random.randint(1,10)}")
    fake_data["aisle_header"].append(f"Header-{random.randint(1,20)}")

df_rack = pd.DataFrame(fake_data)

df_rack.to_sql('Rack', con=engine, index=False, if_exists='append')
print("Inserted", len(df_rack), "rows into Rack table")

fake_data.clear()

# Clothing Table

fake_data = defaultdict(list)
clothing_types = ['Shirt', 'Pants', 'Jacket', 'Dress', 'Shoes']
materials = ['Cotton', 'Polyester', 'Wool', 'Denim']
colors = ['Red', 'Blue', 'Black', 'White']
sizes = ['S', 'M', 'L', 'XL']

for i in range(300):
    fake_data["clothing_id"].append((i+1))
    fake_data["clothing_type"].append(random.choice(clothing_types))
    fake_data["material"].append(random.choice(materials))
    fake_data["color"].append(random.choice(colors))
    fake_data["size"].append(random.choice(sizes))

df_cloth = pd.DataFrame(fake_data)

df_cloth.to_sql('Clothing', con=engine, index=False, if_exists='append')
print("Inserted", len(df_cloth), "rows into Clothing table")

fake_data.clear()

# Supplier Table

fake_data = defaultdict(list)

for i in range(50):
    fake_data["supplier_id"].append((i+1))
    fake_data["supplier_name"].append(fake.company())

df_supplier = pd.DataFrame(fake_data)

df_supplier.to_sql('Supplier', con=engine, index=False, if_exists='append')
print("Inserted", len(df_supplier), "rows into Supplier table")

fake_data.clear()

# Distributor Table

for i in range(50):
    fake_data["distributor_id"].append((i+1))
    fake_data["distributor_name"].append(fake.company())

df_distributor = pd.DataFrame(fake_data)

df_distributor.to_sql('Distributor', con=engine, index=False, if_exists='append')
print("Inserted", len(df_distributor), "rows into Distributor table")

fake_data.clear()

# Inventory Table

cloths = df_cloth["clothing_id"].tolist()
racks = df_rack["rack_id"].tolist()

for i in range(500):
    fake_data["inventory_id"].append((i+1))
    fake_data["clothing_id"].append(random.choice(cloths))
    fake_data["rack_id"].append(random.choice(racks))
    fake_data["quantity"].append(random.randint(1, 100))

df_inv = pd.DataFrame(fake_data)

df_inv.to_sql('Inventory', con=engine, if_exists='append', index=False)
print("Inserted", len(df_inv), "rows into Inventory table")

fake_data.clear()

# Supplies Table

cloths = df_cloth["clothing_id"].tolist()
suppliers = df_supplier["supplier_id"].tolist()

for _ in range(300):
    fake_data["supplier_id"].append(random.choice(suppliers))
    fake_data["clothing_id"].append(random.choice(cloths))

df_supplies = pd.DataFrame(fake_data).drop_duplicates()

df_supplies.to_sql('Supplies', con=engine, if_exists='append', index=False)
print("Inserted", len(df_supplies), "rows into Supplies table")

fake_data.clear()

# Distributes Table

distributors = df_distributor["distributor_id"].tolist()
cloths = df_cloth["clothing_id"].tolist()

for _ in range(300):
    fake_data["distributor_id"].append(random.choice(distributors))
    fake_data["clothing_id"].append(random.choice(cloths))

df_distributes = pd.DataFrame(fake_data).drop_duplicates()

df_distributes.to_sql('Distributes', con=engine, if_exists='append', index=False)
print("Inserted", len(df_distributes), "rows into Distributes table")

fake_data.clear()

print("All Fake Data Inserted Successfully!")
