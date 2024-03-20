//action type creator
const LOAD_REVIEWS = "review/loadReviews";
const ADD_REVIEW = "review/addReview";
const DELETE_REVIEW = "review/deleteReview";
const LOAD_OWNER_REVIEWS = "review/loadOwnerReviews"
const CLEAR_REVIEWS = "review/clearReviews"

//action creator
export const loadReviews = (reviews) => {
  return {
    type: LOAD_REVIEWS,
    reviews,
  };
};

export const addReview = (review) => {
  return {
    type: ADD_REVIEW,
    review,
  };
};

export const deleteReview = (reviewId) => {
  return {
    type: DELETE_REVIEW,
    reviewId,
  };
};

export const loadOwnerReviews = (reviews) => {
  return {
    type: LOAD_OWNER_REVIEWS,
    reviews
  }
}

export const clearReviews = () => {
  return {
    type: CLEAR_REVIEWS
  }
}

//thunk action creators
export const fetchAllReviews = (restuarantId) => async (dispatch) => {
  const response = await fetch(`/api/restaurants/${restuarantId}/reviews`);
  const reviews = await response.json();
  // console.log(response, "review response");
  // console.log(reviews, "here is the reviews");
  dispatch(loadReviews(reviews));
};

export const createReview = (payload, restuarantId) => async (dispatch) => {
  const response = await fetch(`/api/restaurants/${restuarantId}/reviews`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  // console.log(response, "here is the response");
  const review = await response.json();
  if (response.status !== 201) {
    // console.log(review);
    return review;
  }
  if (response.ok) {
    dispatch(addReview(review));
    // console.log(review);
    return review;
  }
};

export const removeReview = (reviewId) => async (dispatch) => {
  const response = await fetch(
    `/api/reviews/${reviewId}`,
    {
      method: "DELETE",
    }
  );
  // console.log(response, "here is the response");
  if (response.ok) {
    const review = await response.json();
    // console.log(review, "here is the review");
    dispatch(deleteReview(reviewId));
    return review;
  }
};

export const fetchOwnerReviews = () => async (dispatch) => {
  const response = await fetch(
    "/api/reviews/current"
  )

  if (response.ok) {
    const reviews = await response.json();
    dispatch(loadOwnerReviews(reviews))
    return reviews;
  }
}

//reducer
const reviewReducer = (state = {}, action) => {
  switch (action.type) {
    case LOAD_REVIEWS: {
      const reviewState = { ...state };
      action.reviews.Reviews.forEach((review) => {
        reviewState[review.id] = review;
      });
      return reviewState;
    }
    case ADD_REVIEW: {
      return { ...state, [action.review.id]: action.review };
    }
    case DELETE_REVIEW: {
      const newState = { ...state };
      delete newState[action.reviewId];
      return newState;
    }
    case LOAD_OWNER_REVIEWS: {
      const reviewState = { ...state };
      action.reviews.forEach((review) => {
        reviewState[review.id] = review;
      });
      return reviewState;
    }
    case CLEAR_REVIEWS: {
      return {}
    }
    default:
      return state;
  }
};

export default reviewReducer;
