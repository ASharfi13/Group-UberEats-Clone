import { useDispatch } from "react-redux";
import { deleteMenuItem } from "../../redux/menuItemReducer";
import { useNavigate } from "react-router-dom";
import "./DeleteMenuItemButton.css";
import { useShoppingCart } from "../../context/CartContext";


function DeleteMenuItemButton({ id, restaurantId }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { cartItems, setCartItems, cartRestaurant, setCartRestaurant } =
    useShoppingCart();

  const removeMenuItem = async (e) => {
    e.preventDefault();
    dispatch(deleteMenuItem(id)).then(setCartItems([])).then(setCartRestaurant(0)).then(navigate(`/restaurants/${restaurantId}`));
  };
  return (
    <button
      className="delete-menu-button"
      onClick={(e) => {
        if (window.confirm("Are you sure you want to delete this menu item? It will erase this Menu Item from Order History")) {
          removeMenuItem(e);
        }
      }}
    >
      Delete
    </button>
  );
}

export default DeleteMenuItemButton;
