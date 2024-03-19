import { useDispatch } from "react-redux"
import { deleteRestaurant } from "../../redux/restaurantReducer"
import { useNavigate } from "react-router-dom"



function DeleteRestaurantButton({id}) {
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const removeRestaurant = async (e) => {
        e.preventDefault()
        dispatch(deleteRestaurant(id)).then(navigate("/"))
    }
    return (
        <button onClick={(e) => {
            if (window.confirm("Are you sure you want to delete this restaurant?")) {
                removeRestaurant(e);
            }
            }}>
           Delete
        </button>
    )
}

export default DeleteRestaurantButton
