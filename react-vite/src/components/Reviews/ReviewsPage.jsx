import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { createReview } from "../../redux/reviewReducer";
import { useNavigate, useParams } from "react-router-dom";
import { FaStar } from "react-icons/fa";

function ReviewsPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { restaurantId } = useParams();
  const user = useSelector((state) => state.session.user);
  const [description, setDescription] = useState("");
  const [stars, setStars] = useState(0);
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      stars,
      description,
    };
    const newReview = await dispatch(createReview(payload, restaurantId));
    if (newReview.errors) setErrors(newReview.errors);
    else navigate(`/restaurants/${restaurantId}`);
  };

  return (
    <>
      <h1>Reviews Page</h1>
      <form onSubmit={handleSubmit} className="restaurant-form">
        <textarea
          name="description"
          value={description}
          placeholder="Write your review"
          onChange={(e) => setDescription(e.target.value)}
        ></textarea>
        <p className="errors">{errors ? errors.description : null}</p>
        <label>
          Star Rating:
          <input
            onChange={(e) => setStars(e.target.value)}
            type="number"
            value={stars}
            name="stars"
            max={5}
            min={0}
          />
          <FaStar />
        </label>
        <p className="errors">{errors ? errors.stars : null}</p>
        <button className="order-button">Submit Review</button>
      </form>
    </>
  );
}

export default ReviewsPage;
