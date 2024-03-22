import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchOwnerReviews, removeReview } from "../../redux/reviewReducer";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { FaStar } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import "../OrdersPage/ReviewsOrdersStyling.css"

function OwnerReviews() {
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const reviews = useSelector((state) => state.reviewState)
    const restaurants = useSelector((state) => state.restaurantState)

    const reviewsArr = Object.values(reviews)

    console.log(restaurants)

    console.log(reviewsArr)

    console.log(reviewsArr[0])


    useEffect(() => {
        dispatch(fetchOwnerReviews())
        dispatch(fetchAllRestaurants())
    }, [dispatch])


    return (
        <>
            <h1>This Is My Reviews</h1>
            {reviewsArr.map((review) => {
                console.log(typeof review?.id)
                return (
                    <div className="reviewCard" key={review?.id}>
                        <img className="review-img" src={restaurants[review.restaurant_id]?.imageUrl}></img>
                        <div className="reviewContent">
                            <p>{review?.description}</p>
                            <span> <span style={{fontWeight: "bold"}}>Rating: </span>{review?.stars} <FaStar /></span>
                            <span>{restaurants[review?.id]?.name}</span>
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
        </>
    )
}


export default OwnerReviews
