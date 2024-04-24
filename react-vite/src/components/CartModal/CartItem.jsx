import { useShoppingCart } from "../../context/CartContext";
export default function({item, quantity}) {
    const { cartItems, setCartItems, cartRestaurant, setCartRestaurant } = useShoppingCart();
    const addItem = () => {
        setCartItems([...cartItems, JSON.stringify(item)])
    }

    const removeItem = () => {
        const temp = [...cartItems]
        const targetItem = cartItems.findIndex(element => element.includes(`{"id":${item.id},`))
        temp.splice(targetItem, 1)
        setCartItems(temp)
    }

    return (
        <li className="cart-item">
            <div className="cart-item-name">
                <h3>{item.name}</h3>
                <p>$ {item.price}</p>
            </div>
            <div className="cart-item-quantity">
                <button onClick={removeItem}>-</button>
                {quantity}
                <button onClick={addItem}>+</button>
            <div className="cart-item-subtotal">
                $ {(item.price * quantity).toFixed(2)}
            </div>
            </div>
        </li>
    )
}
