import { useShoppingCart } from "../../context/CartContext";
export default function({item, quantity}) {
    const { cartItems, setCartItems, clearCart } = useShoppingCart();
    const addItem = () => {
        setCartItems([...cartItems, JSON.stringify(item)])
    }

    const removeItem = () => {
        const temp = [...cartItems]
        const targetItem = cartItems.findIndex(element => element.includes(`{"id":${item.id},`))
        temp.splice(targetItem, 1)
        setCartItems(temp);
        if (temp.length == 0) clearCart();
    }

    if (item) return (
        <li className="cart-item">
            <img src={item.imageUrl} width="72px" height="72px" alt={item.name}/>
            <div className="cart-item-name">
                <h3>{item.name}</h3>
                <p>$ {(item.price * quantity).toFixed(2)}</p>
            </div>
            <div className="cart-item-quantity">
                <button onClick={removeItem}>{"-"}</button>
                {quantity}
                <button onClick={addItem}>+</button>
            </div>
        </li>
    )
}
