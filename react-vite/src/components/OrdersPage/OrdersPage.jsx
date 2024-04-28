import { useEffect, useState } from "react";
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

  // console.log(orders[0]);

  return (
    <div className="orderBody">
      {user ? (
        <div className="ordersContent">
          <h1>Past Orders</h1>
          {orderKeys?.map((orderNumber, idx) => {
            let total = 0;
            let restaurantId = null;
            let order = orders[orderNumber]
            let restaurantImg = "http://www.vintage-breitling.com/wp-content/uploads/2015/06/no-longer-available.jpg";
            let processedItems = Object.groupBy(order.items, ({ id }) => id)
            restaurantsArr.forEach((res) => {
              if (res.name == order?.restaurant) restaurantImg = res.imageUrl
            })

            order?.items.forEach((item) => {
              total += item?.price
            })

            return (
              <div key={idx} className="orderCard">
                <div className="order-info">

                  <img className="order-img" src={restaurantImg}></img>
                  <div className="order-text">

                    <div className="order-details">
                      <h2>{order.restaurant}</h2>
                      <h5> {order?.items.length} {order?.items.length > 1 ? "items" : "item"} for {total.toFixed(2)} • {order?.createdAt}</h5>

                      {Object.values(processedItems).map((items, index) => {
                        let item = items[0]
                        let quantity = items.length;
                        // total += item.price * quantity;
                        restaurantId = item.restaurant_id;
                        // restaurantsArr.forEach((res) => (
                        //   if(res.name == item.)
                        // ))
                        return (
                          <div
                            className="orderItemCard"
                            key={String(index) + String(idx)}
                          >
                            <h4>
                              <span className="orderQuantityBox">{quantity}</span> {item.name}
                            </h4>
                          </div>
                        );
                      })}
                    </div>

                    {/* <p>Total Price: ${total.toFixed(2)}</p> */}
                    {order.order_id == orderKeys[0] && (
                      <h3 className="leaveReviewText" onClick={() =>
                        navigate(`/restaurants/${restaurantId}/add-review`)
                      }>Add A Review</h3>
                    )}
                  </div>
                </div>

                {(<div
                  className="order-button"
                  onClick={() => { navigate(`/restaurants/${restaurantId}`) }}
                >

                  View store
                </div>)}
              </div>
            );
          })}
        </div>
      ) : (
        <h1>Not Logged In</h1>
      )}
    </div>
  );
}

export default OrdersPage;
