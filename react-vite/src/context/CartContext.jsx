import { useContext, createContext, useState } from "react";

export const ShoppingCartContext = createContext();
export const useShoppingCart = () => useContext(ShoppingCartContext);

export const processCart = (cartItems) => {
    return Object.groupBy(cartItems, (item) => JSON.parse(item).id)
}

export function ShoppingCartProvider({ children }) {
    const [cartItems, setCartItems] = useState([]);
    const [cartRestaurant, setCartRestaurant] = useState(0)
    return (
        <ShoppingCartContext.Provider
            value={{ cartItems, setCartItems, cartRestaurant, setCartRestaurant }}
        >
            {children}
        </ShoppingCartContext.Provider>
    );
}
