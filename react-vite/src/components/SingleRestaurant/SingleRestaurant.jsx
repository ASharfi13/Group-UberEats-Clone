import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchRestaurant } from "../../redux/restaurantReducer";
import { NavLink, Link, useNavigate, useParams } from "react-router-dom";
import { loadAllMenuItems } from "../../redux/menuItemReducer";

function SingleRestaurant() {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const restaurant = useSelector((state) => state.restaurantState);
  const restaurantArr = Object.values(restaurant);

  const reviewsArr = restaurant[restaurantId]?.Reviews;
  const menuItemsArr = restaurant[restaurantId]?.MenuItems;

  console.log(menuItemsArr, "over here");

  //   console.log(restaurant[restaurantId]?.Reviews[0]?.description, "over here");
  // put this in the route!!!
  //   const avgRating = {};
  //   restaurantArr.forEach((restaurant) => {
  //     let sum = 0;
  //     restaurant.reviews
  //       ? restaurant.reviews.forEach((res) => {
  //           sum += res.stars;
  //         })
  //       : null;
  //     avgRating[restaurant.id] = sum / restaurant.reviews.length;
  //   });

  //   console.log(avgRating);

  //   console.log(restaurantArr);
  useEffect(() => {
    dispatch(fetchRestaurant(restaurantId));
  }, [dispatch, restaurantId]);

  return (
    <div>
      <h1>This is the Single Restaurant Page</h1>
      <div className="restaurantDetails">
        <div clasName="reviewsContainer">
          {reviewsArr?.map((review) => (
            <div
              className="reviewCard"
              style={{ border: "2px solid black" }}
              key={review.id}
            >
              <p>{review.description}</p>
              <p>{review.stars}</p>
              <p>{review.name}</p>
            </div>
          ))}
        </div>
        <div className="menuItemsContainer">
          {menuItemsArr?.map((item) => (
            <div
              className="menuItemCard"
              style={{ border: "2px solid red" }}
              key={item.id}
            >
              <p>{item.name}</p>
              <p>{item.price}</p>
              <img className="itemImage" src={item.imageUrl} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default SingleRestaurant;
