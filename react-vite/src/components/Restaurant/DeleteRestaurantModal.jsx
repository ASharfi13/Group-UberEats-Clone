import { useDispatch } from "react-redux";
import { deleteRestaurant } from "../../redux/restaurantReducer";
import { useNavigate } from "react-router-dom";
import { useModal } from "../../context/Modal";
import "../ErrorModal/ErrorModal.css"
import { useShoppingCart } from "../../context/CartContext";

function DeleteRestaurantModal({restaurantId, message}) {
    // const dispatch = useDispatch()
    const { closeModal } = useModal()
    const { clearCart, cartRestaurant } = useShoppingCart();
    const navigate = useNavigate()
    const dispatch = useDispatch()

    const handleSubmit = async (e) => {
        e.preventDefault();
        await dispatch(deleteRestaurant(restaurantId));
        if (cartRestaurant == restaurantId) clearCart();
        navigate("/")
        closeModal()
    }

    const handleCancel = async (e) => {
        e.preventDefault();
        closeModal();
    }
    return (
        <div className="error-modal-container">
            {/* <h1>ERROR</h1> */}
            <h2 className="error-modal-message">{message}</h2>
            <button className="exit-modal-button-yes" onClick={handleSubmit}>Yes</button>
            <button className="exit-modal-button-no" onClick={handleCancel}>No</button>
        </div>
    )
}

export default DeleteRestaurantModal
