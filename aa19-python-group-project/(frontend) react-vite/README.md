# React/Vite Authenticate Me

This is the frontend for the Flask/React project. Note that it has no styling
applied. You can copy the __.css__ files from your Authenticate Me project into
the corresponding locations in the __react-vite__ folder to give your project a
unique look.

To run it:

1. `cd` into the __react-vite__ folder.
2. Run `npm install` to install dependencies.
3. Launch it with `npm run dev`.
4. In your browser, navigate to [`localhost:5173`].

Don't forget to run `npm run build` before merging your work to your production
branch!

[`localhost:5173`]: http://localhost:5173/

# User-facing routes

## `/login`

### Log in page

This page displays a log in form

* `GET /login`
* `POST /login`

## `/signup`

This page displays a signup form.

### Sign up page

* `GET /signup`
* `POST /signup`

## `/`

This page displays restaurants, as well as a nav bar with the login/signup buttons or profile dropdown menu. Restaurants should be grouped by types. There will be a search bar with a filter dropdown.

* `GET /`
* `GET /restaurants/:restaurntId`
* `GET /cart`
* `GET /profile`

## `/restaurants/:restaurntId`

This page displays restaurant details, as well as all menu items with buttons to add to cart

* `GET /restaurants/:restaurntId`
* `PUT /restaurants/:restaurntId`
* `GET /restaurants/:restaurntId/menu_items`
* `POST /cart`
* `DELETE /cart/:cartId`

## `/restaurants/:restaurntId/menu_items`

This page displays menu item details

* `GET /restaurants/:restaurntId/menu_items`

if user is owner of restaurant

* `POST /restaurants/:restaurntId/menu_items`
* `PUT /restaurants/:restaurntId/menu_items`
* `DELETE /restaurants/:restaurntId/menu_items`

## `/cart`

This modal displays current cart with all menu items in cart with add and subtract buttons and total price. There will be a checkout button and a clear cart button

* `GET /cart`
* `POST /cart`
* `DELETE /cart/:cartId`
* `POST /cart/clear`
* `POST /checkout`

## `/profile`

This page/modal will show balance and past orders and owned restaurants

* `GET /past_orders`
* `GET /current/restaurants`
* `POST /restaurants/:restaurntId`
* `PUT /restaurants/:restaurntId`
* `DELETE /restaurants/:restaurntId`

## `/past_orders`

This page will show past orders and buttons to post reviews and re-order

* `GET /restaurants/:restaurntId`
* `GET /review`
* `POST /cart`

## `/review`

This popup will have the post review form

* `POST /restaurants/:restaurntId/reviews`
