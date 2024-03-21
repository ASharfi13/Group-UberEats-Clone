import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  clearRestaurant,
  fetchRestaurant,
  getRestaurantTypes,
} from "../../redux/restaurantReducer";
import { NavLink, Link, useNavigate, useParams } from "react-router-dom";
import "./SingleRestaurant.css";
import DeleteRestaurantButton from "./DeleteRestaurantButton";
import DeleteMenuItemButton from "../MenuItems/DeleteMenuItemButton";
import { useShoppingCart } from "../../context/CartContext";
import { fetchOwnerMenuItems } from "../../redux/menuItemReducer";
import { FaStar } from "react-icons/fa";

function SingleRestaurant() {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const restaurant = useSelector((state) => state.restaurantState);
  const menu_items = useSelector((state) => state.menuItemState);
  const { cartItems, setCartItems, cartRestaurant, setCartRestaurant } =
    useShoppingCart();

  const reviewsArr = restaurant[restaurantId]?.Reviews;
  const menuItemsArr = Object.values(menu_items);

  const user = useSelector((state) => state.session.user);

  const avgReviews =
    reviewsArr?.length > 0
      ? reviewsArr?.reduce((acc, item) => acc + item.stars, 0) /
      reviewsArr?.length
      : 0;

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
    dispatch(fetchRestaurant(restaurantId))
      .then(dispatch(getRestaurantTypes()))
      .then(dispatch(fetchOwnerMenuItems(restaurantId)));
  }, [dispatch, restaurantId]);

  function addToCart(e, menuItem) {
    if (cartRestaurant == 0) {
      setCartItems([...cartItems, JSON.stringify(menuItem)]);
      setCartRestaurant(menuItem.restaurant_id);
      window.alert(`${menuItem.name} added to Cart!`)
    } else if (cartRestaurant !== menuItem.restaurant_id) {
      window.alert(
        "Menu Item from a different Restaurant cannot be added to Current Cart. Please Checkout or Clear Cart"
      );
    } else {
      setCartItems([...cartItems, JSON.stringify(menuItem)]);
      window.alert(`${menuItem.name} added to Cart!`)
    }
  }

  let cartRestaurantId;

  cartItems?.length > 0
    ? (cartRestaurantId = cartItems[0].restaurant_id)
    : (cartRestaurantId = null);

  console.log(cartItems)
  console.log(JSON.stringify(menuItemsArr[0]))

  console.log(cartItems.includes(JSON.stringify(menuItemsArr[0])))

  const removeFromCart = async (e, menuItem) => {
    const tempCartItems = [...cartItems]
    const targetItem = cartItems.findIndex((element) => element.includes(`{"id":${menuItem.id},`))
    tempCartItems.splice(targetItem, 1)
    setCartItems(tempCartItems)
  }

  return (
    <>
      {restaurant && (
        <div>
          <div>
            <img src={restaurant[restaurantId]?.imageUrl}></img>
          </div>
          <h1 className="restaurant-name">{restaurant[restaurantId]?.name} </h1>
          <h3 className="restaurantRating">
            {" "}
            {avgReviews.toFixed(1)} <FaStar /> ({reviewsArr?.length})
          </h3>
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
            <hr />
            <div className="menuItemsContainer">
              {menuItemsArr?.map((item) => (
                <div className="menuItemCard" key={item.id}>
                  <p className="name-item">{item.name}</p>
                  <p>${item.price}</p>
                  <img className="itemImage" src={item.imageUrl} />

                  <button
                    className="add-to-cart"
                    onClick={(e) =>
                      addToCart(e, {
                        ...item,
                        restaurant: restaurant[restaurantId].name,
                      })
                    }
                  >
                    Add to Cart
                  </button>


                  {
                    cartItems.findIndex((element) => element.includes(`{"id":${item.id},`)) !== -1 &&
                    (<button onClick={(e) => removeFromCart(e, item)}>
                      Remove Item From Cart
                    </button>)
                  }


                  <div className="ManageMenuItem">
                    {restaurant[restaurantId]?.owner_id === user?.id && (
                      <>
                        <button
                          className="edit-button"
                          onClick={() =>
                            navigate(`/menu-items/${item.id}/update`)
                          }
                        >
                          Edit
                        </button>
                        <DeleteMenuItemButton
                          id={item.id}
                          restaurantId={restaurantId}
                        />
                      </>
                    )}
                  </div>
                </div>
              ))}
            </div>
            <div className="ManageRestaurant">
              {restaurant[restaurantId]?.owner_id === user?.id && (
                <>
                  <button className="add-item" onClick={() =>
                    navigate(`/restaurants/${restaurantId}/update`)
                  }>
                    Edit Restaurant
                  </button>
                  <DeleteRestaurantButton
                    className="delete-button"
                    id={restaurantId}
                  />
                  <button
                    className="add-item"
                    onClick={() =>
                      navigate(`/restaurants/${restaurantId}/add-item`)
                    }
                  >
                    Add Menu Item
                  </button>
                </>
              )}
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default SingleRestaurant;
