import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { NavLink, Link, useNavigate } from "react-router-dom";
import { loadAllMenuItems } from "../../redux/menuItemReducer";

function LandingPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const restaurants = useSelector((state) => state.restaurantState);
  const restaurantArr = Object.values(restaurants);

  const avgRating = {};

  restaurantArr?.forEach((restaurant) => {
    let sum = 0;
    if (restaurant.reviews) {
      restaurant?.reviews?.forEach((res) => {
        sum += res.stars;
        avgRating[restaurant.id] = sum / restaurant.reviews.length;
      });
    } else {
      return null;
    }
  });

  console.log(avgRating);

  console.log(restaurantArr);
  useEffect(() => {
    dispatch(fetchAllRestaurants());
  }, [dispatch]);

  if (!restaurants) return;
  if (!restaurantArr) return;

  return (
    <div>
      <h1>This is the Landing Page</h1>
      <div className="restaurantDivs">
        {restaurantArr?.map((restaurant) => (
          <div
            className="restaurantCard"
            style={{ border: "2px solid black" }}
            key={restaurant.id}
            onClick={() => navigate(`restaurants/${restaurant.id}`)}
          >
            <p>{restaurant.name}</p>
            <img className="resCardImage" src={restaurant.imageUrl} />
            <p>{avgRating[restaurant.id]}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default LandingPage;
