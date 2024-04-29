import { useNavigate } from "react-router-dom";
import "./RestaurantCarousel.css"
export default function RestaurantCard({restaurant, user, idx, avgRating, priceArr, timeArr}) {
    const navigate = useNavigate();
    return (<div
        className="restaurantCard"
        key={idx}
        onClick={() => {
          navigate(`/restaurants/${restaurant?.id}`);
        }}
      >
        <img className="resCardImage" src={restaurant?.imageUrl} />
        <div className="info">
          <p className="name">{restaurant?.name}</p>
          <p className="review-info">
            {avgRating[restaurant?.id] ? avgRating[restaurant?.id].toFixed(1) : "(New)"}
          </p>
        </div>
        <div className="restPriceTimeInfo">
          <h4>${priceArr[restaurant.id]} Delivery Fee • {timeArr[restaurant.id][0]}-{timeArr[restaurant.id][1]} min</h4>
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
      </div>)
}
