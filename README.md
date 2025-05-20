# E-commerce Website
A full-featured e-commerce platform built with Django, designed to provide a seamless online shopping experience. This application encompasses user authentication, product browsing, shopping cart functionality, and more.

## Table of Contents
- Features
- Project Structure
- Installation
- Usage
- Technologies Used
- License

## Features
User Authentication: Secure registration and login system.

Product Management: Add, update, and display products with images.

Shopping Cart: Add products to the cart and manage quantities.

Responsive Design: Front-end templates optimized for various devices.

Admin Interface: Manage products, users, and orders through Django's admin panel.

## 🗂️ Project Structure

```bash
ecommerce/
├── core/                 # Core application logic
├── ecommerce/            # Project settings and URLs
├── front end templates/  # HTML templates for the front-end
├── media/product_images/ # Uploaded product images
├── services/             # Business logic and services
├── templates/            # Base templates
├── userauths/            # User authentication system
├── db.sqlite3            # SQLite database
└── manage.py             # Django's command-line utility
```
##  Installation
1. **Clone the Repository**
```bash
git clone https://github.com/suhanaislam52/ecommerce.git
cd ecommerce
```
2. **Create a virtual environment:**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Apply migrations:**
```bash
python manage.py migrate
```
5. **Create a superuser:**
```bash
python manage.py createsuperuser
```
6. **Run the development server:**
```bash
python manage.py runserver
```
## Usage
<b>User Side:</b>

- Browse products on the homepage.

- View product details and add items to the cart.

- Register or log in to place an order.

- Proceed through the checkout process.

<b>Admin Side:</b>

- Log in to the Django admin panel at /admin.

- Add, edit, or delete products and categories.

- Manage user accounts and view customer orders.

<b>Development & Testing:</b>

- Run the development server locally using python manage.py runserver.

- Use Django's built-in authentication system for user management.

- Modify templates and styles in the front end templates/ and static/ directories.

## Technologies Used
<b>Backend:</b>

- Django – High-level Python web framework for rapid development.

- SQLite3– Lightweight relational database for development.

<b>Frontend:</b>

- HTML5, CSS3, JavaScript – For responsive and interactive UI.

- Django Templating Engine – To render dynamic content on the frontend.

- Bootstrap (optional, if used) – For responsive and mobile-first design components.

<b>Authentication & Admin:</b>

- Django’s built-in User model and admin interface for secure management.

<b>Tools:</b>

- Python – Core programming language.

- pip – Python package installer.

- Virtualenv – For creating isolated Python environments.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
