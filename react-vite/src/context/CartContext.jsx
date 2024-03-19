import { useContext, createContext, useState} from "react";

export const ShoppingCartContext = createContext();
export const useShoppingCart = () => useContext(ShoppingCartContext);


export function ShoppingCartProvider({ children }) {
    const [cartItems, setCartItems] = useState([]);
    return (
         <ShoppingCartContext.Provider
            value={{cartItems, setCartItems}}
         >
            {children}
        </ShoppingCartContext.Provider>
    );
}
