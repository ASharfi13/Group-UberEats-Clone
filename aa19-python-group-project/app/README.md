# Uber Eats API Endpoints

## User

## User Authentication/Authorization

### All endpoints that require authentication

All endpoints that require a current user to be logged in.

- Request: endpoints that require authentication
- Error Response: Require authentication

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Authentication required"
    }
    ```

### All endpoints that require proper authorization

All endpoints that require authentication and the current user does not have the
correct role(s) or permission(s).

- Request: endpoints that require proper authorization
- Error Response: Require proper authorization

  - Status Code: 403
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Forbidden"
    }
    ```

### Get the Current User

Returns the information about the current user that is logged in.

- Require Authentication: false
- Request

  - Method: GET
  - URL: /api/session
  - Body: none

- Successful Response when there is a logged in user

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "user": {
        "id": 1,
        "name": "John",
        "email": "john.smith@gmail.com"
      }
    }
    ```

- Successful Response when there is no logged in user

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "user": null
    }
    ```

### Log In a User

Logs in a current user with valid credentials and returns the current user's
information.

- Require Authentication: false
- Request

  - Method: POST
  - URL: /api/session
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "credential": "john.smith@gmail.com",
      "password": "secret password"
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "user": {
        "id": 1,
        "name": "John",
        "email": "john.smith@gmail.com"
      }
    }
    ```

- Error Response: Invalid credentials

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Invalid credentials"
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "credential": "Email is required",
        "password": "Password is required"
      }
    }
    ```

### Sign Up a User

Creates a new user, logs them in as the current user, and returns the current
user's information.

- Require Authentication: false
- Request

  - Method: POST
  - URL: /api/users
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "name": "John",
      "email": "john.smith@gmail.com",
      "password": "secret password",
      "location": "22 Colonization ave "
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "user": {
        "id": 1,
        "name": "John",
        "email": "john.smith@gmail.com"
      }
    }
    ```

- Error response: User already exists with the specified email

  - Status Code: 500
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "User already exists",
      "errors": {
        "email": "User with that email already exists"
      }
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "email": "Invalid email",
        "name": "Name is required" //add in the name length (no special characters)
      }
    }
    ```

## RESTAURANTS

### Get all restaurants

Returns all the restaurants

- Require Authentication: false
- Request

  - Method: GET
  - URL: /api/restaurants
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "restaurants": [
        {
          "id": 1,
          "ownerId": 1,
          "location": "123 Disney Lane",
          "name": "App Academy",
          "type": "Place where web developers are created",
          "avgRating": 4.5,
          "imageUrl": "image url"
        }
      ]
    }
    ```

### Get all restaurants owned by the Current User

Returns all the restaurants owned (created) by the current user.

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/restaurants/current
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "restaurants": [
        {
          "id": 1,
          "ownerId": 1,
          "location": "123 Disney Lane",
          "name": "App Academy",
          "type": "Place where web developers are created",
          "avgRating": 4.5,
          "imageUrl": "image url"
        }
      ]
    }
    ```

### Get details of a restaurant from an id

Returns the details of a restaurant specified by its id.

- Require Authentication: false
- Request

  - Method: GET
  - URL: /api/restaurants/:restaurantId
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "ownerId": 1,
      "location": "123 Disney Lane",
      "name": "App Academy",
      "type": "Place where web developers are created",
      "avgRating": 4.5,
      "numReview": 1,
      "imageUrl": "image url",
      "Reviews": [
        {
          "User.name": "Jane Doe",
          "description": "The place was tasty.",
          "stars": 5,
          "createdAt": "June 12, 2024"
        }
      ],
      "MenuItems": [
        {
          "id": 1,
          "name": "Cheeseburger",
          "type": "Burger",
          "price": 7.99,
          "imageUrl": "fakeImage.png"
        }
      ]
    }
    ```

- Error response: Couldn't find a restaurant with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Restaurant couldn't be found"
    }
    ```

### Create a Restaurant

Creates and returns a new restaurant.

- Require Authentication: true
- Request

  - Method: POST
  - URL: /api/restaurants
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "ownerId": 1,
      "location": "123 Disney Lane",
      "name": "Burger King",
      "type": "Place where food creators are created",
      "imageUrl": "image url"
    }
    ```

- Successful Response

  - Status Code: 201
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "ownerId": 1,
      "location": "123 Disney Lane",
      "name": "Burger King",
      "type": "Place where food creators are created",
      "imageUrl": "image url",
      "createdAt": "June 22, 2024"
    }
    ```

- Error Response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "name": "Name is required",
        "location": "Location is required",
        "type": "Type is required",
        "ownerId": "OwnerId is required",
        "imageUrl": "Image Url is required"
      }
    }
    ```

### Edit a Restaurant

Updates and returns an existing restaurant.

- Require Authentication: true
- Require proper authorization: Restaurant must belong to the current user
- Request

  - Method: PUT
  - URL: /api/restaurants/:restaurantId
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "location": "123 Disney Lane",
      "name": "Burger King",
      "type": "Place where food creators are created",
      "imageUrl": "image url"
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "ownerId": 1,
      "location": "123 Disney Lane",
      "name": "Burger King",
      "type": "Place where food creators are created",
      "imageUrl": "image url",
      "createdAt": "June 22, 2024",
      "updatedAt": "June 28, 2024"
    }
    ```

- Error Response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "name": "Name is required",
        "location": "Location is required",
        "type": "Type is required",
        "imageUrl": "Image is required"
      }
    }
    ```

- Error response: Couldn't find a Restaurant with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Restaurant couldn't be found"
    }
    ```

### Delete a Restaurant

Deletes an existing restaurant.

- Require Authentication: true
- Require proper authorization: Restaurant must belong to the current user
- Request

  - Method: DELETE
  - URL: /api/restaurants/:restaurantId
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Successfully deleted"
    }
    ```

- Error response: Couldn't find a Restaurant with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Restaurant couldn't be found"
    }
    ```

## MENU_ITEMS

### Get details of a menu_item from an id

Returns the details of a menu_item specified by its id.

- Require Authentication: false
- Request

  - Method: GET
  - URL: /api/menu-items/:itemId
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "price": 7.99,
      "restaurantId": 2,
      "name": "Cheeseburger",
      "type": "Burger",
      "imageUrl": "image url"
    }
    ```

- Error response: Couldn't find a menu item with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Menu item couldn't be found"
    }
    ```

### Create a Menu Item

Creates and returns a new item.

- Require Authentication: true
- Require Authorization: current user must be owner of restaurant
- Request

  - Method: POST
  - URL: /api/restaurants/:restaurantId/menu-items
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "price": 7.99,
      "restaurantId": 2,
      "name": "Cheese Pizza",
      "type": "Pizza",
      "imageUrl": "image url"
    }
    ```

- Successful Response

  - Status Code: 201
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 2,
      "price": 7.99,
      "restaurantId": 2,
      "name": "Cheese Pizza",
      "type": "Pizza",
      "imageUrl": "image url",
      "createdAt": "March 25, 2024"
    }
    ```

- Error Response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "name": "Name is required",
        "restaurantId": "RestaurantId is required",
        "type": "Type is required",
        "price": "Price must be greater than 0"
      }
    }
    ```

### Edit a Menu Item

Updates and returns an existing menu item.

- Require Authentication: true
- Require proper authorization: Restaurant must belong to the current user
- Request

  - Method: PUT
  - URL: /api/menu-items/:itemId
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "price": 7.99,
      "restaurantId": 2,
      "name": "Cheese Pizza",
      "type": "Pizza",
      "imageUrl": "image url"
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 2,
      "price": 7.99,
      "restaurantId": 2,
      "name": "Cheese Pizza",
      "type": "Pizza",
      "imageUrl": "image url",
      "createdAt": "March 25, 2024",
      "updatedAt": "March 28, 2024"
    }
    ```

- Error Response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "name": "Name is required",
        "restaurantId": "RestaurantId is required",
        "type": "Type is required",
        "price": "Price must be greater than 0"
      }
    }
    ```

- Error response: Couldn't find a Menu item with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Menu item couldn't be found"
    }
    ```

### Delete a Menu Item

Deletes an existing menu item.

- Require Authentication: true
- Require proper authorization: Restaurant must belong to the current user
- Request

  - Method: DELETE
  - URL: /api/menu_items/:itemId
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Successfully deleted"
    }
    ```

- Error response: Couldn't find a menu item with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Menu item couldn't be found"
    }
    ```

## REVIEWS

### Create a Review for a restaurant based on the restaurant's id

Create and return a new review for a restaurant specified by id.

- Require Authentication: true
- Request

  - Method: POST
  - URL: /api/restaurants/:restaurantId/reviews
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "description": "This was an awesome restaurant!",
      "stars": 5,
      "user_id": 1,
      "restaurant_id": 2
    }
    ```

- Successful Response

  - Status Code: 201
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "userId": 1,
      "restaurantId": 1,
      "description": "This was an awesome restaurant!",
      "stars": 5,
      "createdAt": "June 20, 2024"
    }
    ```

- Error Response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Bad Request",
      "errors": {
        "description": "Review text is required",
        "stars": "Stars must be an integer from 1 to 5"
      }
    }
    ```

- Error response: Couldn't find a review with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Review couldn't be found"
    }
    ```

- Error response: Review from the current user already exists for the restaurant

  - Status Code: 500
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "User already has a review for this restaurant"
    }
    ```

### Delete a Review

Delete an existing review.

- Require Authentication: true
- Require proper authorization: Review must belong to the current user
- Request

  - Method: DELETE
  - URL: /api/reviews/:reviewId
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Successfully deleted"
    }
    ```

- Error response: Couldn't find a Review with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Review couldn't be found"
    }
    ```

## Shopping Cart

## Get current/active shopping cart

Returns the current shopping cart by the current user

- Require Authentication: True
- Require Authorization: When a current user is logged in
- Request

  - METHOD: GET
  - URL: /api/users/current/cart
  - Body: none

- Response

  - Status Code: 200
  - Body:

  ```json
  {

      "cart": {
          "orderId": 1,
          "restaurant": "Burger King",
          "items": [
              {
                  "name": "Cheeseburger",
                  "price": 7.99,
                  "imageUrl": "fakeImage.png"
              }
              ,...
          ],
          "totalPrice": 20.99,
          "balance": 200.00
        // add checkout_date into the cart_table
      }
  }
  ```

## GET Past Orders

Returns the past orders by the current user

- Require Authentication: True
- Require Authorization: When a current user is logged in
- Request

  - METHOD: GET
  - URL: /api/users/current/past_orders
  - Body: none

- Response

  - Status Code: 200
  - Body:

  ```json
  {

      "orders": [
        {
          "orderId": 1,
          "restaurant": "Burger King",
          "items": [
              {
                  "name": "Cheeseburger",
                  "price": 7.99,
                  "imageUrl": "fakeImage.png"
              }
              ,...
          ],

          "totalPrice": 20.99,
          "checkedOut": "May 20, 2024"
      }
      ]
  }
  ```

## ADD Item to current Cart

Add an item to the current cart

// we can potentially do this in the front end. redux store

// only add final checkout items to the database. display selected choices with the store

- Require Authentication: True
- Require Authorization: When a current user is logged in
- Request

  - METHOD: POST
  - URL: /api/users/current/cart
  - Body:
    ```json
    {
      "user_id": 1,
      "menuItem_id": 5,
      "order_id": 3
    }
    ```

- Response

  - Status Code: 200
  - Body:

  ```json
  {
    "user_id": 1,
    "menuItem_id": 5,
    "order_id": 3
  }
  ```

  - Error response: Couldn't find a menu item with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Menu Item Id couldn't be found"
    }
    ```

## DELETE Item from current Cart

Delete an existing item from current cart.

- Require Authentication: true
- Require proper authorization: Cart must belong to the current user
- Request

  - Method: DELETE
  - URL: /api/cart/:cartId
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Successfully deleted"
    }
    ```

- Error response: Couldn't find a cart item with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Cart Item couldn't be found"
    }
    ```

## Clear the current Cart

Delete all items from current cart.

- Require Authentication: true
- Require proper authorization: Cart must belong to the current user
- Request

  - Method: DELETE
  - URL: /api/user/current/cart/clear
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Successfully deleted"
    }
    ```

## Checkout

Checkout all items from current cart.

- Require Authentication: true
- Require proper authorization: Cart must belong to the current user
- Request

  - Method: POST
  - URL: /api/user/current/cart/checkout
  - Body:

  ```json
  {
    "order_id": 1
  }
  ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Successfully checked out"
    }
    ```

- Error response: Couldn't find a cart with the specified order_id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Order couldn't be found"
    }
    ```

- Error response: User does not have enough money

  - Status Code: 403
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Insufficient Funds"
    }
    ```
