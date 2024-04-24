import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { NavLink, Link, useNavigate } from "react-router-dom";
import { loadAllMenuItems } from "../../redux/menuItemReducer";
import "./LandingPage.css";
import { FaStar } from "react-icons/fa";
import { SiMoneygram } from "react-icons/si";



function LandingPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const restaurants = useSelector((state) => state.restaurantState);
  const restaurantArr = Object.entries(restaurants).filter(([key, restaurant]) => key != "types");
  const user = useSelector((state) => state.session.user);
  const [delPriceCheck, setDelPriceCheck] = useState(false);

  const avgRating = {};

  restaurantArr?.forEach(([key, restaurant]) => {
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



  // useEffect(() => {
  //   dispatch(fetchAllRestaurants());
  // }, [dispatch]);

  if (!restaurants) return;
  if (!restaurantArr) return;

  // ONLY IMPLEMENT IF MODEL COLUMN DOESN'T WORK OUT
  // const generateRandomPrices = (n) => {
  //   const prices = [];
  //   const dollarAmount = [0, 1, 2, 3];
  //   const centAmount = ['49', '99'];

  //   for (let i = 0; i < n; i++) {
  //     const randomWholeNumber = dollarAmount[Math.floor(Math.random() * dollarAmount.length)];
  //     const randomDecimal = centAmount[Math.floor(Math.random() * centAmount.length)];
  //     const randomPrice = `${randomWholeNumber}.${randomDecimal}`;
  //     prices.push(parseFloat(randomPrice));
  //   }

  //   return prices;
  // }

  const generateRandomTime = (n) => {
    const result = [];
    const min = 10;
    const max = 40;
    const step = 5;

    for (let i = 0; i < n; i++) {
      const randomNumber = Math.floor(Math.random() * ((max - min) / step + 1)) * step + min;

      const randomAddition = [10, 15, 20][Math.floor(Math.random() * 3)];

      result.push([randomNumber, randomNumber + randomAddition]);
    }
    return result;
  }

  const timeArr = generateRandomTime(parseInt(restaurantArr?.length));
  if (!localStorage.getItem("delTimeArr")) localStorage.setItem("delTimeArr", JSON.stringify(timeArr))

  const delTimeArr = JSON.parse(localStorage.getItem("delTimeArr"));

  console.log(delTimeArr)

  return (
    <div className="landingContainer">
      <h1 className="featured-on">Featured on Uber Eats</h1>
      <hr />
      <div className="restaurantDivs">
        {restaurantArr?.map(([id, restaurant], idx) => (
          <div
            className="restaurantCard"
            // style={{ backgroundColor: `${user?.id == restaurant?.owner_id ? "#64B41C" : null}` }}
            key={idx}
            onClick={() => {
              navigate(`/restaurants/${restaurant?.id}`);
            }}
          >
            <img className="resCardImage" src={restaurant?.imageUrl} />
            <div className="info">
              <p className="name">{restaurant?.name}</p>
              <p className="review-info">
                {avgRating[restaurant?.id]?.toFixed(1) || "(New)"}
              </p>
            </div>
            <div className="restPriceTimeInfo">
              <p className="timeInfo">{delTimeArr[restaurant?.id - 1][0]}-{delTimeArr[restaurant?.id - 1][1]} min</p>
            </div>
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
