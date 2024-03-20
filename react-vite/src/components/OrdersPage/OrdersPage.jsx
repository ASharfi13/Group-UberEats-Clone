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
    }, [dispatch]);

    return (
        <div>
            <h1>This is the Orders Page</h1>
            {Object.values(orders).map((order) => <p>hello</p> )}
        </div>
    )
}

export default OrdersPage
