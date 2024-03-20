import { useContext, createContext, useState } from "react";

export const ShoppingCartContext = createContext();
export const useShoppingCart = () => useContext(ShoppingCartContext);


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
