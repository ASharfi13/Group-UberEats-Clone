# Group 1 UberEats Clone (Name Pending) 
Introducing "SupremeEats", a dynamic collaboration poised to revolutionize the online dining experience. SupremeEats is a vibrant web application, meticulously crafted by a team of aspiring full stack web developers and software engineers, eager to showcase our talents in a playful, engaging manner. At its core, SupremeEats boasts comprehensive CRUD (Create, Read, Update, Delete) functionality for both restaurants and menu items, empowering administrators to curate and manage their offerings effortlessly. Users are greeted with a colorful interface, inviting them to explore a diverse array of dining options with ease. The standout feature of SupremeEats lies in its intuitive shopping cart and checkout functionality, ensuring a seamless and enjoyable ordering process for customers. From browsing to payment, every interaction is designed to bring joy and convenience to the dining experience. We are currently polishing the styling to ensure pixel perfection to provide an unparalleled user experience. In the future, we will implement Google Maps for even user engagement.

# Live Link
https://ahmed-joel-khobe-royce-ubereats-project.onrender.com

# Contributors
- Ahmed Sharfi: [LinkedIn](https://www.linkedin.com/in/ahmedsharfi/) | [GitHub](https://github.com/asharfi13)
- Joel Abitzen: [LinkedIn](https://www.linkedin.com/in/joel-abitzen/) | [GitHub](https://github.com/jabitzen)
- Khobe Arzadon: [LinkedIn](https://www.linkedin.com/in/khobe-arzadon-4b985a202/) | [GitHub](https://github.com/khobearzadon24)
- Royce Jiang: [LinkedIn](https://www.linkedin.com/in/jiangroyce/) | [GitHub](https://github.com/jiangroyce)

# Tech Stack
## Framework and Libraries
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Flask](https://img.shields.io/badge/Express.js-404D59?style=for-the-badge)![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-%2523323330.svg?style=for-the-badge&logo=sqlalchemy)![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

## Database
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Hosting
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

## Database Schema
![alt text](<DatabaseSchema.png>)
## User Stories

## Users

### Unauthorized & Not Logged In User Permission

* As an unauthorized and unregistered user, I should have access to the website’s `"/"` home page:
    * When on the Home Page:
        * I can navigate across different restaurants
        * I can click on a Restaurant and be redirected to the its Details page at `“/restaurants/:restaurant_id"`.
            * On the Restaurant Details page, I can select Menu Items and add them to the cart, while logged out and unauthorized
        * Clicking the ‘Check-Out’ button on the Shopping Cart Modal, while logged out & unauthorized, will take me to the sign-up/log-in page at `“/auth-login”`.

### Log-In / Sign-Up
* As an unauthorized and unregistered user, I should have access to the login form to enter my email and password.
    * If I am an existing user, I will enter my credentials and upon successful validation, be redirected to the checkout page at `“/checkout”`.
    * If I am not an existing user, I will have the option to click a button called “Sign Up” and be redirected to the sign-up page at `“/auth-signup”`.
* As an unauthorized and unregistered user, after clicking the      ‘Sign-Up’ button, I should have access to the sign-up form.
    * I should be able to enter my full name, email address, password, address
    * After successfully entering my information, I should be redirected to the checkout page at `“/checkout”`if there’s a current cart.
    * Otherwise, I should be redirected back to the home page at `“/”`.
    * If I am redirected to the checkout page, I should have the option of clicking a button called ‘Add Funds’ where I will be redirected to a page at `“/add-funds”` where I can enter how much money I want in my wallet.

### Shopping-Cart
* Either a logged-in or unauthorized user can add Menu Items to the shopping cart from the Restaurant details page.
    * On the Restaurant Details page, I can click on a menu item, and a modal will pop up and allow me to add it to the shopping cart via a button called “Add To Cart”.
    * I should be able to access my cart on any page in the Nav Bar.
    * Clicking on my cart will allow me to see a summarized list of all the menu items in the cart and if I click on a menu item in the cart, a modal will pop up and allow me to remove it from the cart via the button “Remove Item”.
    * I should also see a plus sign at the bottom of the summarized list and when I click on it, it should redirect me to the Restaurant’s Detail page at `“/restaurants/:restaurant_id"`.
    * If I attempt to add Menu Items from a different Restaurant to my cart, a warning modal will pop up and inform me if I want to create a new cart. It will also inform me that creating a new cart will delete the old cart.

### Check-out (logged-in only)
* As a logged-in user at the checkout page, I should be able to see how much money I have in my wallet, the menu items (details of each menu item and price) I have in my cart, the total price at the bottom, and a purchase button.
    * If I have enough funds in my wallet, the purchase button will be active and I can checkout successfully.
    * If not the button will be disabled and an ‘Add Funds’ button will appear on the page. Clicking on the ‘Add Funds’ button will take me to the Add Funds page at `“/add-funds”` where I can add more money to my wallet.
    * After successfully checking out, it should take me to the orders page at `“/orders”` where I will be able to see my latest order.
    * If I click on my latest order, it should take me to the Order Details page at `“/orders/order_id”` where I will be able to see all of the Menu Items I ordered and their price (digital receipt) and an ETA on when it will arrive.

### Creating A New Restaurant (logged-in only)
* As a logged-in user, if I am on the home page I should see and be able to click on my profile icon and that should redirect me to my profile page at `"/users/user_id”`. While on my profile page, I should be able to see and click on a button that says “Create New Restaurant”.
    * After clicking the button, I should be redirected to a new form page at `“/restaurants/new”` where I can enter the following information for my new restaurant:
        * I should be able to provide a name, location, type, one image file.
    * After successfully submitting the form, I should be relocated to my new Restaurant Details page at `“/restaurants/:restaurant_id"`.

### Restaurant Details
* On the Restaurant Details page, if I am the owner of the Restaurant I should be able to see an edit button called “Edit” on all components of the Restaurant Details page.
* If I click on the ‘Edit’ button, I should be redirected to the new Restaurant form page at `“restaurants/restaurant_id/edit”` where all of the previously filled information will be present in the inputs for each form component.
* At the bottom of the Restaurant Details page, I should see a red button called ‘Delete Restaurant’.
* If I click on the ‘Delete’ button, a modal should appear that should ask me if I’m sure I want to delete the Restaurant. There should be two options in the modal, “Yes” or “No”.
* If I click “Yes”, the modal should disappear and I should be redirected to the home page at `"/"` where the restaurant will no longer exist review.
* If I click “No”, the modal should disappear and the review should remain there.

### Creating A New Menu Item (logged-in and owner only)
* As a logged-in user, if I am the owner of a restaurant I should be able to click on the plus sign on the Restaurant Details page and be redirected to a new Menu Items form page at `“menu-items/new”` where I can input the following to create a new Menu Item.
    * I should be able to provide a name, type, price, and a single image file
    * After successfully submitting the form for a new Menu Item, I should be redirected to the Restaurant Details page at `“restaurants/restaurant_id”` where my new Menu Item will be present.

### Menu Item Details
* On the Restaurant Details page, if I am the owner of the Restaurant I should be able to see an edit button called “Edit” and a delete button called “Delete” on all of the Menu Items.
* If I click on the ‘Edit’ button, I should be redirected to the new Menu-Items form page at `“menu-items/menu-item_id/edit”` where all of the previously filled information will be present in the inputs for each form component.
* If I click on the ‘Delete’ button, a modal should appear that should ask me if I’m sure I want to delete the Menu Item. There should be two options in the modal, “Yes” or “No”.
* If I click “Yes”, the modal should disappear and after the page refreshes, the review I deleted should be gone.
* Navigating to the Restaurant Details page at `“restaurants/restaurant_id”` should also not display the Menu Item.
* If I click “No”, the modal should disappear and the Menu Item should remain there.

### Reviews
* If I am not logged in and an unauthorized user or logged in, If I am at the Restaurant Details page I should be able to see a section containing all of the reviews for that Restaurant.
* Each Review should contain a star rating, the name of the person who left the review, and the actual review content.
* If I am logged in and navigate to the Orders page at `“/orders”`, I should be able to click on an order and after being directed to the Order Details page at `"/orders/order_id"`, I should be able to see and click on a button called “Leave A Review”.
* If I am logged in and the Restaurant I am ordering from is a Restaurant that I own/created, I should not be able to see the “Leave A Review” button on the Order Details page and not be able to leave a review.
* After clicking on the button, I should be redirected to the Review form page at `“/reviews/new”` where I should be able to put the following information.
    * I should be able to click on anywhere from 1 to 5 stars when leaving a star rating and enter a description of what I liked or disliked in a text box.
    * After successfully filling out the description and providing a star rating, I should be able to click a ‘Submit’ button and be redirected to the respective Restaurant Details page at `“restaurants/restaurant_id”` where I can see my new review.
* If I navigate back to the Order Details page at `"/orders/order_id"` for the Restaurant I left a review for, I should be able to see all of my reviews and in each review component, I should see a button called ‘Delete”.
* If I click on the ‘Delete’ button, a modal should appear that should ask me if I’m sure I want to delete the review. There should be two options in the modal, “Yes” or “No”.
* If I click “Yes”, the modal should disappear and after the page refreshes, the review I deleted should be gone.
* Navigating to the Restaurant Details page at `“restaurants/restaurant_id”` should also not display the review.
* If I click “No”, the modal should disappear and the review should remain there.
