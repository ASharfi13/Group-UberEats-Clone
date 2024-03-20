import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchRestaurant } from "../../redux/restaurantReducer";
import { NavLink, Link, useNavigate, useParams } from "react-router-dom";
import "./SingleRestaurant.css";
import DeleteRestaurantButton from "./DeleteRestaurantButton";
import DeleteMenuItemButton from "../MenuItems/DeleteMenuItemButton";
import { useShoppingCart } from "../../context/CartContext";
// import { loadAllMenuItems } from "../../redux/menuItemReducer";

function SingleRestaurant() {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const restaurant = useSelector((state) => state.restaurantState);
  // console.log("THIS IS THE RESTAURANT", restaurant)
  const restaurantArr = Object.values(restaurant);
  const { cartItems, setCartItems } = useShoppingCart();

  const reviewsArr = restaurant[restaurantId]?.Reviews;
  const menuItemsArr = restaurant[restaurantId]?.MenuItems;

  const user = useSelector((state) => state.session.user);

  // console.log(cartItems, "over here");

  //   console.log(restaurant[restaurantId]?.Reviews[0]?.description, "over here");
  // put this in the route!!!
  //   const avgRating = {};
  //   restaurantArr.forEach((restaurant) => {
  //     let sum = 0;
  //     restaurant.reviews
  //       ? restaurant.reviews.forEach((res) => {
  //           sum += res.stars;
  //         })
  //       : null;
  //     avgRating[restaurant.id] = sum / restaurant.reviews.length;
  //   });

  //   console.log(avgRating);

  //   console.log(restaurantArr);
  useEffect(() => {
    dispatch(fetchRestaurant(restaurantId));
  }, [dispatch, restaurantId]);

  function addToCart(e, menuItem) {
    setCartItems([...cartItems, JSON.stringify(menuItem)]);
  }

  return (
    <>
    {restaurant &&
    <div>
      <h1>What customers are saying </h1>
      <div className="restaurantDetails">
        <div className="reviews-Container">
          {reviewsArr?.map((review) => (
            <div
              className="review-Card"
              // style={{ border: "2px solid black" }}
              key={review.id}
            >
              <p className="name-review">{review.name}</p>
              <div className="rating">
                <p>{review.stars}</p>
                <img
                  className="star"
                  src="https://i.postimg.cc/QxSC3byV/stars-removebg-preview.png"
                  alt="star"
                />
              </div>
              <p className="description-review">{review.description}</p>
            </div>
          ))}
        </div>
        <h1>Featured Items</h1>
        <div className="menuItemsContainer">
          {menuItemsArr?.map((item) => (
            <div className="menuItemCard" key={item.id}>
              <p className="name-item">{item.name}</p>
              <p>${item.price}</p>
              <img className="itemImage" src={item.imageUrl} />
              <button
                className="add-to-cart"
                onClick={(e) => addToCart(e, item)}
              >
                Add to Cart
              </button>
              <div className="ManageMenuItem">
                {restaurant[restaurantId]?.owner_id === user.id && (
                  <DeleteMenuItemButton id={item.id} restaurantId={restaurantId} />
                )}
              </div>
            </div>
          ))}
        </div>
        <div className="ManageRestaurant">
          {restaurant[restaurantId]?.owner_id === user.id && (
            <DeleteRestaurantButton id={restaurantId} />
          )}
        </div>
      </div>
    </div>
}
    </>
  );
}

export default SingleRestaurant;
