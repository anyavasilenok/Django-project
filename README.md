# Django-project
Django-progect for inventory accounting in the warehouses of the enterprise.


Verbal description of the subject area: 
The enterprise has several warehouses where working equipment is located. Each warehouse has a number, name, phone number. 
The inventory is brought to the warehouse in accordance with the receipt invoice, which has a date, a list of the inventory, the number of units of each inventory. 
The full name and position of the warehouse employee who accepted the inventory is also indicated. The consumption of inventory from the warehouse is carried out according to the outgoing invoice, which has the same structure as the receipt invoice. The receipt of inventory at the warehouse is reflected in the warehouse accounting card, which is started for each item of inventory. 

The program implements the following features:
- Adding/editing/deleting information about work inventory.
- Adding/editing/deleting information about warehouses.
- Adding / editing / deleting information about the arrival and consumption of working inventory.
- View a list of inventory of a given type in a given warehouse and its quantity for the current date.
- Viewing a list of all receipts and expenditures of inventory of a given name in all warehouses - date, inventory name, list - receipt date, quantity, consumption date, quantity.
- View a list of all warehouses sorted by name for the current date.

Use-case diagram:
![image](https://user-images.githubusercontent.com/103070585/226994827-de8eda1b-d54c-4a41-8be9-65d48d053793.png)

ER diagram:
![image](https://user-images.githubusercontent.com/103070585/226995072-b9a1bff7-bf68-43ae-a11d-2ef99409d74e.png)
![image](https://user-images.githubusercontent.com/103070585/226995670-a10ba462-76f5-4c43-893b-d531713ce860.png)

