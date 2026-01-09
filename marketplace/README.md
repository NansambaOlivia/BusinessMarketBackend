# Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)

# Core Features
- Authentication and users
- Role-based permissions
- Product approval workflow
- API design

# Business & User Management
- Each Business can have multiple users
- Users belong to exactly one business
- Users are assigned a Role that defines their permissions

# Permissions
- can_manage_users: allows creating and managing users in the same business
- can_create_products: allows creating products
- can_edit_products: allows editing products
- can_approve_products: allows approving products
- can_delete_products: allows deleting products

# Business executives (users with can_manage_users = True) can:
- Create new users and assign roles to them
- create roles to users within their business

