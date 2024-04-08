import { useDispatch } from "react-redux";
import { deleteRestaurant } from "../../redux/restaurantReducer";
import { useNavigate } from "react-router-dom";
import "./DeleteRestaurantButton.css";
import { useShoppingCart } from "../../context/CartContext";

function DeleteRestaurantButton({ id }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { cartItems, setCartItems, cartRestaurant, setCartRestaurant } =
    useShoppingCart();

  const removeRestaurant = async (e) => {
    e.preventDefault();
    dispatch(deleteRestaurant(id)).then(setCartItems([])).then(setCartRestaurant(0)).then(
      navigate("/")
    );
  };

  return (
    <button
      className="delete-restaurant-button"
      onClick={(e) => {
        if (
          window.confirm("Are you sure you want to delete this restaurant? It will erase this Restaurant from Order History.")
        ) {
          removeRestaurant(e);
        }
      }}
    >
      Delete Restuarant
    </button>
  );
}

export default DeleteRestaurantButton;
