import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchRestaurant, getRestaurantTypes } from "../../redux/restaurantReducer";
import { useNavigate, useParams } from "react-router-dom";
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

  const removeFromCart = async (e, menuItem) => {
    const tempCartItems = [...cartItems]
    const targetItem = cartItems.findIndex((element) => element.includes(`{"id":${menuItem.id},`))
    tempCartItems.splice(targetItem, 1)
    setCartItems(tempCartItems)
  }

  return (
    <>
      {restaurant && (
        <div className="restaurant-details-container">
          <div className="restaurant-image-container">
            <img className="restaurant-image" src={restaurant[restaurantId]?.imageUrl}></img>
          </div>
          <div className="restaurant-details-header-container">
            <h1 className="restaurant-name">{restaurant[restaurantId]?.name} </h1>
            <h3 className="restaurantRating">
              {avgReviews.toFixed(1)} <FaStar /> ({reviewsArr?.length}) reviews
            </h3>
          </div>
          <div className="reviews-header-container">
            <h1>Top Reviews</h1>
            <h4>From customers who've ordered here</h4>

          </div>
          <div className="restaurantDetails">
            <div className="reviews-Container">
              {reviewsArr?.map((review) => (
                <div
                  className="review-Card"
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
                  <p className="description-review">"{review.description}"</p>
                </div>
              ))}
            </div>
            <h1>Featured Items</h1>

            <div className="menuItemsContainer">
              {menuItemsArr?.map((item, index) => (
                <div className="menuItemCard" key={index}>
                  <div className="menu-item-card-left">
                    <div className="menu-item-card-header">
                      <p className="name-item">{item.name}</p>
                      <p className="price-item">${item.price}</p>
                    </div>

                    <div className="menu-item-buttons-container">
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
                  </div>

                  <div className="menu-item-image-container">
                    <img className="itemImage" src={item.imageUrl} />
                  </div>

                </div>
              ))}
            </div>
            <div className="ManageRestaurant">
              {restaurant[restaurantId]?.owner_id === user?.id && (
                <>
                  <h1>Manage Restaurant</h1>
                  {/* <hr /> */}
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
