import { useContext, createContext, useState } from "react";

export const ShoppingCartContext = createContext();
export const useShoppingCart = () => useContext(ShoppingCartContext);

export const processCart = (cartItems) => {
    return Object.groupBy(cartItems, (item) => JSON.parse(item).id)
}

export const removeItems = (cartItems, itemId) => {
    const parsed = cartItems.filter((item) => {
        item = JSON.parse(item);
        return item.id !== itemId
    })
    return parsed
}
export function ShoppingCartProvider({ children }) {
    const [cartItems, setCartItems] = useState([]);
    const [cartRestaurant, setCartRestaurant] = useState(0);
    const [restaurantName, setRestaurantName] = useState("");
    const clearCart = () => {
        setCartItems([]);
        setCartRestaurant(0)
        setRestaurantName("")
    }
    return (
        <ShoppingCartContext.Provider
            value={{ cartItems, setCartItems, cartRestaurant, setCartRestaurant, restaurantName, setRestaurantName, clearCart }}
        >
            {children}
        </ShoppingCartContext.Provider>
    );
}
