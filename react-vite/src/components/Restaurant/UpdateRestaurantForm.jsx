import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from "react-router-dom"
import { fetchRestaurant, editRestaurant, getRestaurantTypes } from "../../redux/restaurantReducer"

function UpdateRestaurant() {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const { restaurantId } = useParams()
    const restaurant = useSelector((state) => state.restaurantState[restaurantId])
    const restaurantTypes = useSelector((state) => state.restaurantState.types)

    const [name, setName] = useState(restaurant?.name)
    const [location, setLocation] = useState(restaurant?.location)
    const [type, setType] = useState(restaurant?.type)
    const [image, setImage] = useState(restaurant?.imageUrl)
    const [errors, setErrors] = useState({})


    useEffect(() => {
        dispatch(fetchRestaurant(restaurantId)).then(dispatch(getRestaurantTypes()))
        setName(restaurant?.name)
        setLocation(restaurant?.location)
        setType(restaurant?.type)
        setImage(restaurant?.imageUrl)
    }, [dispatch, restaurantId, restaurant?.name, restaurant?.location, restaurant?.type, restaurant?.imageUrl])

    const onSubmit = async (e) => {
        e.preventDefault()

        const payload = {
            name,
            location,
            type,
            "imageUrl": image
        }

        const response = await dispatch(editRestaurant(payload));
        if (response.errors) setErrors(response.errors)
        else navigate(`/restaurants/${response.id}`)
    }

    return (
        <div>
            {restaurant && restaurantTypes && <div>
                <form onSubmit={onSubmit}>
                    <h1>Update Your Restaurant</h1>
                    <div>
                        <input
                            type="text"
                            placeholder="Enter A Name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        // required
                        >
                        </input>
                        <p className="errors">{errors.name ? errors.name : null}</p>
                    </div>

                    <div>
                        <input
                            type="text"
                            placeholder="Enter A Location"
                            value={location}
                            onChange={(e) => setLocation(e.target.value)}
                        // required
                        >
                        </input>
                        <p className="errors">{errors.location ? errors.location : null}</p>
                    </div>
                    <div>
                        <select
                            value={type}
                            onChange={(e) => setType(e.target.value)}
                        >
                            <option value={""} disabled selected>Select Type</option>
                            {restaurantTypes.map((restaurant, idx) => (
                                <option key={idx}>{restaurant}</option>
                            ))}
                        </select>
                        <p className="errors">{errors.type ? errors.type : null}</p>

                    </div>
                    <div>
                        <input
                            type="url"
                            placeholder="Enter New Image Url"
                            value={image}
                            onChange={(e) => setImage(e.target.value)}
                        >
                        </input>
                        <p className="errors">{errors.imageUrl ? errors.imageUrl : null}</p>

                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>}

        </div>
    )
}

export default UpdateRestaurant
