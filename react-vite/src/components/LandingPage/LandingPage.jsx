import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { useNavigate, useSearchParams } from "react-router-dom";
import "./LandingPage.css";
import { getRestaurantTypes } from "../../redux/restaurantReducer";
import { FilterCarousel } from "./FilterCarousel";
import { RestaurantCarousel } from "./RestaurantCarousel";
import RestaurantCard from "./RestaurantCard";

function LandingPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();

  const restaurants = useSelector((state) => state.restaurantState);
  const restaurantTypes = restaurants?.types
  const filter = searchParams.get("type");

  const restaurantArr = Object.entries(restaurants).filter(([key, restaurant]) => key != "types").filter(([key, restaurant]) => {
    if (filter) return restaurant?.types?.includes(filter)
    return restaurant
  });
  const user = useSelector((state) => state.session.user);


  const avgRating = {};

  // Calculate Average Rating
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
  const generateRandomPrices = (restaurantArr) => {
    const prices = {};
    const dollarAmount = [0, 1, 2, 3];
    const centAmount = ['49', '99'];

    restaurantArr.forEach(([id, restaurant]) => {
      const randomWholeNumber = dollarAmount[Math.floor(Math.random() * dollarAmount.length)];
      const randomDecimal = centAmount[Math.floor(Math.random() * centAmount.length)];
      const randomPrice = `${randomWholeNumber}.${randomDecimal}`;
      prices[id] = parseFloat(randomPrice);
    })

    return prices;
  }

  const generateRandomTime = (restaurantArr) => {
    const result = {};
    const min = 10;
    const max = 40;
    const step = 5;

    restaurantArr.forEach(([id, restaurant]) => {
      const randomNumber = Math.floor(Math.random() * ((max - min) / step + 1)) * step + min;

      const randomAddition = [10, 15, 20][Math.floor(Math.random() * 3)];

      result[id] = [randomNumber, randomNumber + randomAddition]
    })
    return result;
  }

  const timeArr = generateRandomTime(restaurantArr);
  const priceArr = generateRandomPrices(restaurantArr);

  // const delTimeArr = JSON.parse(localStorage.getItem("delTimeArr"));

  // console.log(delTimeArr)
  // console.log("sp", searchParams);
  // console.log(restaurantTypes)
  // console.log(avgRating)
  let lowDelFees
  let lowTimes
  if (!filter) {
    lowDelFees = Object.entries(priceArr)?.filter(([x, y]) => y < 2).map((x) => restaurantArr[Number(x[0]) - 1][1]);
    lowTimes = Object.entries(timeArr)?.filter(([x, y]) => y[1] <= 30).map((x) => restaurantArr[Number(x[0]) - 1][1]);
  }

  useEffect(() => {
    dispatch(getRestaurantTypes())
  }, [dispatch])

  document.title = "Order Food Online | Food Delivery"
  if (restaurantTypes) return (
    <div className="landingContainer">
      <FilterCarousel restaurantTypes={restaurantTypes} filter={filter} setSearchParams={setSearchParams} />
        {!filter && (
        <>
        <div className="under-2-delivery">
        <h1 className="featured-on">Under $2 Delivery Fee</h1>
        <RestaurantCarousel restaurants={lowDelFees} user={user} avgRating={avgRating} priceArr={priceArr} timeArr={timeArr} />
      </div>
      <div className="under-20-min">
        <h1 className="featured-on">Get it in 30 minutes</h1>
        <RestaurantCarousel restaurants={lowTimes} user={user} avgRating={avgRating} priceArr={priceArr} timeArr={timeArr} />
      </div>
      </>)}
      <h1 className="featured-on">
        {filter ? filter : "All"} Restaurants
      </h1>
      <div className="restaurantDivs">
        {restaurantArr?.map(([id, restaurant], idx) => (
          <RestaurantCard key={idx} restaurant={restaurant} idx={idx} user={user} avgRating={avgRating} priceArr={priceArr} timeArr={timeArr} />
          // <div
          //   className="restaurantCard"
          //   // style={{ backgroundColor: `${user?.id == restaurant?.owner_id ? "#64B41C" : null}` }}
          //   key={idx}
          //   onClick={() => {
          //     navigate(`/restaurants/${restaurant?.id}`);
          //   }}
          // >
          //   <img className="resCardImage" src={restaurant?.imageUrl} />
          //   <div className="info">
          //     <p className="name">{restaurant?.name}</p>
          //     <p className="review-info">
          //       {avgRating[restaurant?.id] ? avgRating[restaurant?.id].toFixed(1) : "(New)"}
          //     </p>
          //   </div>
          //   <div className="restPriceTimeInfo">
          //     <h4>${priceArr[idx + 1]} Delivery Fee • {timeArr[idx + 1][0]}-{timeArr[idx + 1][1]} min</h4>
          //   </div>
          //   {user?.id == restaurant?.owner_id && (
          //     <button
          //       className="add-item edit-restaurant"
          //       onClick={(e) => {
          //         e.stopPropagation();
          //         navigate(`/restaurants/${restaurant?.id}/update`);
          //       }}
          //     >
          //       Edit Restaurant
          //     </button>
          //   )}
          // </div>
        ))}
      </div>
    </div>
  );
}

export default LandingPage;
