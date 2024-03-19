import { useDispatch } from "react-redux";
import { deleteMenuItem } from "../../redux/menuItemReducer";
import { useNavigate } from "react-router-dom";

function DeleteMenuItemButton({ id }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const removeMenuItem = async (e) => {
    e.preventDefault();
    dispatch(deleteMenuItem(id)).then(navigate("/"));
  };
  return (
    <button
      onClick={(e) => {
        if (window.confirm("Are you sure you want to delete this menu item?")) {
          removeMenuItem(e);
        }
      }}
    >
      Delete
    </button>
  );
}

export default DeleteMenuItemButton;
