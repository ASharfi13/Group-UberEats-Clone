import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchRestaurant, getRestaurantTypes } from "../../redux/restaurantReducer";
import { useNavigate, useParams } from "react-router-dom";
import "./SingleRestaurant.css";
import { useShoppingCart, removeItems } from "../../context/CartContext";
import { fetchOwnerMenuItems } from "../../redux/menuItemReducer";
import { FaStar } from "react-icons/fa";
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import ErrorModal from "../ErrorModal/ErrorModal";
import DeleteRestaurantModal from "./DeleteRestaurantModal";
import DeleteMenuItemModal from "../MenuItems/DeleteMenuItemModal";
import { useSideModal } from "../../context/SideModal";
import CartModal from "../CartModal";

function SingleRestaurant() {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const restaurant = useSelector((state) => state.restaurantState);
  const menu_items = useSelector((state) => state.menuItemState);
  const user = useSelector((state) => state.session.user);
  const wallets = useSelector((store) => store.walletState);
  const userWallet = wallets ? wallets[user?.id] : null;
  const { cartItems, setCartItems, cartRestaurant, setCartRestaurant, restaurantName, setRestaurantName } =
    useShoppingCart();
  const { setModalContent } = useModal();
  const setCartModal = useSideModal().setModalContent;
  const { setModalSide } = useSideModal();

  const reviewsArr = restaurant[restaurantId]?.reviews;
  const menuItemsArr = Object.values(menu_items);


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
      setRestaurantName(restaurant[restaurantId].name)
      setModalSide("right");
      setCartModal(<CartModal
        user={user}
        userWallet={userWallet}
        restaurants={restaurant} />)
    } else if (cartRestaurant !== menuItem.restaurant_id) {
        setModalContent(<ErrorModal message={"Menu Item from a different Restaurant cannot be added to Current Cart. Please Checkout or Clear Cart"}/>)
    } else {
      setCartItems([...cartItems, JSON.stringify(menuItem)]);
      setModalSide("right");
      setCartModal(<CartModal
        user={user}
        restaurantName={restaurant[restaurantId].name}
        userWallet={userWallet}
        restaurants={restaurant} />)
    }
  }

  let cartRestaurantId;

  cartItems?.length > 0
    ? (cartRestaurantId = cartItems[0].restaurant_id)
    : (cartRestaurantId = null);

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
                        (<button onClick={(e) => setCartItems(removeItems(cartItems, item.id))}>
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
                            <OpenModalButton
                              buttonText={"Delete"}
                              modalComponent={<DeleteMenuItemModal itemId={item.id} restaurantId={restaurantId} message={"Are you sure you want to delete this menu item? It will erase this Menu Item from Order History"}/>}
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
                  <OpenModalButton
                    buttonText={"Delete Restaurant"}
                    modalComponent={<DeleteRestaurantModal restaurantId={restaurantId} message={"Are you sure you want to delete this restaurant? It will erase this Restaurant from Order History."}/>}
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
