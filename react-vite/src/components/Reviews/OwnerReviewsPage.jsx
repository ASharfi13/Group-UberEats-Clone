import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchOwnerReviews, removeReview, clearReviews } from "../../redux/reviewReducer";
import { fetchAllRestaurants, clearRestaurants } from "../../redux/restaurantReducer";
import { FaStar } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import "../OrdersPage/ReviewsOrdersStyling.css"

function OwnerReviews() {
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const reviews = useSelector((state) => state.reviewState)
    const restaurants = useSelector((state) => state.restaurantState)

    const reviewsArr = Object.values(reviews)

    useEffect(() => {
        dispatch(clearRestaurants())
        dispatch(clearReviews())
        dispatch(fetchOwnerReviews())
        dispatch(fetchAllRestaurants())
    }, [dispatch])


    return (
        <div className="orderBody">
            <h1>My Reviews</h1>
            {reviewsArr.map((review) => {
                return (
                    <div className="reviewCard" key={review?.id}>
                        <img className="review-img" src={restaurants[review.restaurant_id]?.imageUrl}></img>
                        <div className="reviewContent">
                            <p>{review?.description}</p>
                            <span> <span style={{fontWeight: "bold"}}>Rating: </span>{review?.stars} <FaStar /></span>
                            <span>{restaurants[review?.restaurant_id]?.name}</span>
                            <span>{review?.createdAt}</span>
                        </div>
                        <button
                        className="order-button"
                        onClick={() => {
                            dispatch(removeReview(review?.id)).then(
                                navigate(`/restaurants/${review?.restaurant_id}`)
                            )
                        }}>
                            Delete Review
                        </button>

                    </div>
                )
            })}
        </div>
    )
}


export default OwnerReviews
