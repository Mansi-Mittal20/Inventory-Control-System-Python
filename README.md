## *** Important Logic ***

- When placing an order:
  - Customer and product are validated first
  - Stock is checked before placing order
  - Stock gets reduced after order

- Orders store complete details (customer + product info)
  so even if product/customer is deleted, order history remains.

## *** Bug Faced & Solution ***

While testing, I found an issue:

** When a customer was deleted and a new customer was added,  
old orders were getting linked with the new customer.

## Reason:
- IDs were getting reused or mismatched
- Orders were only relying on CID reference

## Solution:
- Used auto-increment ID system (`cid.txt` and `pid.txt`)
- Ensured every new customer/product gets a unique ID
- Added status check in order view:
  - `(Deleted Customer)`
  - `(Deleted Product)`

This fixed the issue and made order history reliable.

## *** Improvements Added ***

- Status check in orders (Active / Deleted)
- Stock update after order
- Low stock alert feature
- Cleaner output formatting

## *** Technologies Used ***

- Python
- File Handling
- Pickle Module

## *** How to Run ***

1. Open terminal / command prompt
2. Navigate to project folder
3. Run:
python main.py

## *** Note ***

This is a basic project for learning purposes.  
It can be improved further by adding GUI or database.

## *** Author ***

Mansi  
B.Tech 
