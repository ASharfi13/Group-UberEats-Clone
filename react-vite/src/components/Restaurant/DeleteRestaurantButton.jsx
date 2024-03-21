import { useDispatch } from "react-redux";
import { deleteRestaurant } from "../../redux/restaurantReducer";
import { useNavigate } from "react-router-dom";
import "./DeleteRestaurantButton.css";

function DeleteRestaurantButton({ id }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const removeRestaurant = async (e) => {
    e.preventDefault();
    dispatch(deleteRestaurant(id)).then(navigate("/"));
  };

  return (
    <button
      className="delete-restaurant-button"
      onClick={(e) => {
        if (
          window.confirm("Are you sure you want to delete this restaurant?")
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
