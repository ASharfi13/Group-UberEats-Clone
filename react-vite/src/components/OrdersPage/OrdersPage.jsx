import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getOrders } from "../../redux/shoppingCartReducer";
import { NavLink, Link, useNavigate, useParams } from "react-router-dom";

function OrdersPage() {
    const dispatch = useDispatch();
    const user = useSelector((state) => state.session.user)
    const orders = useSelector((state) => state.orderState)

    useEffect(() => {
        dispatch(getOrders(user.id));
    }, [dispatch, user.id]);

    return (
        <div>
            <h1>This is the Orders Page</h1>
            {Object.values(orders).map((order, idx) =>{
                return (
                    <div key={idx} className="orderCard">
                        <h3>{order.order_id} | <span>{order.createdAt} | </span><span>{order.restaurant}</span></h3>
                        {
                            order.items.map((item, index) => {
                                return (
                                    <div className="orderItemCard" key={String(index) + String(idx)}>
                                        <p>{item.name}</p>
                                        <p>{item.price}</p>
                                    </div>
                                )
                            })
                        }

                    </div>
                )
            } )}
        </div>
    )
}

export default OrdersPage
