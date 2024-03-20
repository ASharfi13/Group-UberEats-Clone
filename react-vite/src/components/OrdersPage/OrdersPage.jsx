import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getOrders } from "../../redux/shoppingCartReducer";
import { NavLink, Link, useNavigate, useParams } from "react-router-dom";
import "./OrdersPage.css";
import { clearReviews, fetchOwnerReviews, removeReview } from "../../redux/reviewReducer";

function OrdersPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);
  const orders = useSelector((state) => state.orderState);
  const reviews = useSelector((state) => state.reviewState);

  const ordersArr = Object.values(orders)

  const reviewsArr = (Object.values(reviews))

  useEffect(() => {
    dispatch(getOrders(user?.id));
    dispatch(fetchOwnerReviews());
    return () => {
      dispatch(clearReviews())
    }
  }, [dispatch, user?.id]);

  const reviewedRestaurants = reviewsArr?.map((review) => review.restaurant_id)

  const orderKeys = Object.keys(orders).map((item) => Number(item)).sort().reverse()

  return (
    <>
      {user ? (
        <div className="ordersContent">
          <h1>This is the Orders Page</h1>
          {orderKeys?.map((orderNumber, idx) => {
            let total = 0;
            let restaurantId = null;
            let order = orders[orderNumber]
            return (
              <div key={idx} className="orderCard">
                <h3>
                  {order.order_id} | <span>{order.createdAt} | </span>
                  <span>{order.restaurant}</span>
                </h3>

                {order.items.map((item, index) => {
                  total += item.price;
                  restaurantId = item.restaurant_id;
                  return (
                    <div
                      className="orderItemCard"
                      key={String(index) + String(idx)}
                    >
                      <span>
                        {item.name} | ${item.price}
                      </span>
                    </div>
                  );
                })}
                <p>Total Price: ${total.toFixed(2)}</p>
                {order?.order_id == orderKeys[0] && (<button
                  onClick={() =>
                    navigate(`/restaurants/${restaurantId}/add-review`)
                  }
                >
                  Add Review
                </button>)}
              </div>
            );
          })}
        </div>
      ) : (
        <h1>Not Logged In</h1>
      )}
    </>
  );
}

export default OrdersPage;
