import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { NavLink, Link, useNavigate } from "react-router-dom";
import { loadAllMenuItems } from "../../redux/menuItemReducer";
import "./LandingPage.css";

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

  // console.log(avgRating);

  // console.log(restaurantArr);
  useEffect(() => {
    dispatch(fetchAllRestaurants());
  }, [dispatch]);

  if (!restaurants) return;
  if (!restaurantArr) return;

  return (
    <div>
      <h1 className="featured-on">Featured on Uber Eats</h1>
      <hr />
      <div className="restaurantDivs">
        {restaurantArr?.map((restaurant, idx) => (
          <div
            className="restaurantCard"
            key={restaurant.id}
            onClick={() => navigate(`restaurants/${restaurant.id}`)}
          >
            <p className="name">{restaurant.name}</p>

            <div className="rating">
              <p>{avgRating[restaurant.id]}</p>
              <img
                className="star"
                src="https://i.postimg.cc/QxSC3byV/stars-removebg-preview.png"
                alt="star"
              />
            </div>
            <img className="resCardImage" src={restaurant.imageUrl} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default LandingPage;
