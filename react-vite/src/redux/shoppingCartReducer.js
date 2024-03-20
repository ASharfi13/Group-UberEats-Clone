const LOAD_ORDERS = "shopping-cart/loadOrders"
const ADD_CART_ITEM = "shopping-cart/addCartItem";
const REMOVE_CART_ITEM = "shopping-cart/removeCartItem";
const ADD_ORDER = "shopping-cart/addOrder";


export const loadOrders = (orders) => {
    return {
        type: LOAD_ORDERS,
        orders
    }
}

export const addCartItem = (user_id, menu_item_id) => {
    return {
        type: ADD_CART_ITEM,
        user_id, menu_item_id
    }
}

export const removeCartItem = (user_id, menu_item_id) => {
    return {
        type: REMOVE_CART_ITEM,
        user_id, menu_item_id
    }
}

export const addOrder = (order) => {
    return {
        type: ADD_ORDER,
        order
    }
}

export const checkOutCart = (user_id, cart_items) => async (dispatch) => {
    const response = await fetch("/api/shopping-carts/check-out", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            "user_id": user_id,
            "cart_items": cart_items
        })
    })
    if (response.ok) {
        const newOrder = await response.json()
        dispatch(addOrder(newOrder))
        return newOrder
    }
}

export const getOrders = (user_id) => async (dispatch) => {
    const response = await fetch(`/api/shopping-carts/${user_id}`)
    if (response.ok) {
        const orders = await response.json()
        dispatch(loadOrders(orders))
        return orders;
    }
}

export const shoppingCartReducer = (state = {}, action) => {
    switch(action.type) {
        case LOAD_ORDERS:
            const ordersState = {};
            action.orders.orders.forEach((order) => {
                ordersState[order.order_id] = order;
            });
            return ordersState;
        case ADD_ORDER:
            return { ...state, [action.order.order_id]: action.order };
        default:
            return state;
    }
}
