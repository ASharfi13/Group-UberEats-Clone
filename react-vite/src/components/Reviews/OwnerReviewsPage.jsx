import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchOwnerReviews, removeReview } from "../../redux/reviewReducer";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { FaStar } from "react-icons/fa";
import { useNavigate } from "react-router-dom";

function OwnerReviews() {
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const reviews = useSelector((state) => state.reviewState)
    const restaurants = useSelector((state) => state.restaurantState)

    const reviewsArr = Object.values(reviews)

    console.log(restaurants)

    console.log(reviewsArr)


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
                    <div className="orderCard" key={review?.id}>
                        <span>{review?.description}</span>
                        <span>{review?.stars}</span>
                        <span>{restaurants[review?.id]?.name}</span>
                        <span>{review?.createdAt}</span>
                        <button onClick={() => {
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
