import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getOrders, clearOrders } from "../../redux/shoppingCartReducer";
import { useNavigate } from "react-router-dom";
import "./ReviewsOrdersStyling.css";
import { clearReviews, fetchOwnerReviews } from "../../redux/reviewReducer";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";

function OrdersPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);
  const orders = useSelector((state) => state.orderState);
  const restaurants = useSelector((state) => state.restaurantState);

  const restaurantsArr = Object.values(restaurants)

  useEffect(() => {
    dispatch(clearOrders());
    dispatch(getOrders(user?.id));
    dispatch(fetchOwnerReviews());
    dispatch(fetchAllRestaurants())
    return () => {
      dispatch(clearReviews())
    }
  }, [dispatch, user?.id]);

  const orderKeys = Object.keys(orders).map((item) => Number(item)).sort().reverse()

  return (
    <>
      {user ? (
        <div className="ordersContent">
          <h1>Past Orders</h1>
          {orderKeys?.map((orderNumber, idx) => {
            let total = 0;
            let restaurantId = null;
            let order = orders[orderNumber]
            let restaurantImg = "http://www.vintage-breitling.com/wp-content/uploads/2015/06/no-longer-available.jpg";
            let processedItems = Object.groupBy(order.items, ({id})=>id)
            restaurantsArr.forEach((res) => {
              if (res.name == order?.restaurant) restaurantImg = res.imageUrl
            })
            return (
              <div key={idx} className="orderCard">
                <img className="order-img" src={restaurantImg}></img>
                <div className="order-text">

                  <h2>{order.restaurant}</h2>

                  <h3>{order.createdAt}</h3>

                  {Object.values(processedItems).map((items, index) => {
                    let item = items[0]
                    let quantity = items.length;
                    total += item.price * quantity;
                    restaurantId = item.restaurant_id;
                    // restaurantsArr.forEach((res) => (
                    //   if(res.name == item.)
                    // ))
                    return (
                      <div
                        className="orderItemCard"
                        key={String(index) + String(idx)}
                      >
                        <span>
                          {item.name} | {quantity} | ${item.price * quantity}
                        </span>
                      </div>
                    );
                  })}
                  <p>Total Price: ${total.toFixed(2)}</p>
                </div>
                {order?.order_id == orderKeys[0] && (<button
                  className="order-button"
                  style={{}}
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
