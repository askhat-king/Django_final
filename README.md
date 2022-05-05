### Online book store

## What the point of project
The point is to create website that can users help to find interesting books,
comicses or items related to moviesand if user wants he can buy it using shopping cart.
The user can perform the following functions:
- A user can view the different books and comicses that are available.
- A user can find similar books or comicses
- A user can add book, comics, item to shopping cart
- A user can watch his order history
- A user can add creditcard to make payment
- A user can use filters
- A user can login

## Models
MainUser, Profile, Advertising,ShoppingCart, CreditCard, Order,
Publisher, Author, Book,Item,Comics, SimilarBook, SimilarComics, Comment, Review, Reply

## Technologies Used
- Installed python version 3+

## Project Setup Instructions
1) download repository 
2. cd into Bookshop
```
Bookshop> cd Bookshop
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```