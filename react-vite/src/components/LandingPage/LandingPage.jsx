import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { NavLink, Link, useNavigate } from "react-router-dom";
import { loadAllMenuItems } from "../../redux/menuItemReducer";
import "./LandingPage.css";
import { FaStar } from "react-icons/fa";

function LandingPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const restaurants = useSelector((state) => state.restaurantState);
  const restaurantArr = Object.values(restaurants);
  const user = useSelector((state) => state.session.user);

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
            // style={{ backgroundColor: `${user?.id == restaurant?.owner_id ? "#64B41C" : null}` }}
            key={idx}
            onClick={() => {
              navigate(`/restaurants/${restaurant.id}`);
            }}
          >
            <p className="name">{restaurant.name}</p>

            <div className="rating">
              <p>
                {avgRating[restaurant.id]?.toFixed(1)} <FaStar />
              </p>
            </div>
            <img className="resCardImage" src={restaurant?.imageUrl} />
            {user?.id == restaurant?.owner_id && (
              <button
                className="add-item edit-restaurant"
                onClick={(e) => {
                  e.stopPropagation();
                  navigate(`/restaurants/${restaurant?.id}/update`);
                }}
              >
                Edit Restaurant
              </button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default LandingPage;
