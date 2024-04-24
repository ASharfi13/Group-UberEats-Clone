import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { FaWallet } from 'react-icons/fa';
import { IoMdClose } from 'react-icons/io';
import { useSideModal } from '../../context/SideModal';
import { useModal } from '../../context/Modal';
import { checkOutCart } from "../../redux/shoppingCartReducer";
import { useShoppingCart } from "../../context/CartContext";
import { decreaseFunds, increaseFunds } from "../../redux/walletReducer";
import ErrorModal from "../ErrorModal/ErrorModal";
import LoginFormModal from "../LoginFormModal";
import { processCart } from '../../context/CartContext';
import CartItem from './CartItem';
import "./CartModal.css"

function CartModal({user, restaurantName, userWallet, restaurants}) {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { closeModal } = useSideModal();
    const { setModalContent } = useModal();
    const { cartItems, setCartItems, cartRestaurant, setCartRestaurant } = useShoppingCart();
    const processedCart = processCart(cartItems);

    console.log(cartItems)
    console.log(processedCart)

    let total = 0

    const checkOutLoggedIn = async (e) => {
      e.preventDefault()
      if (userWallet >= total) {
        const newOrder = await dispatch(checkOutCart(user.id, cartItems))
        const newUserBalance = await dispatch(decreaseFunds(-total, user.id))
        const newRestaurantBalance = await dispatch(increaseFunds(total * 0.95, restaurants[cartRestaurant].owner_id))
        setCartItems([])
        setCartRestaurant(0)
        navigate("/orders")
      } else {

        setModalContent(<ErrorModal message={"Insufficient Funds, Please Add Funds in your profile"}/>)
        // alert("Insufficient Funds, Please Add Funds in your profile")
      }
    }

    const checkOutLoggedOut = async (e) => {
      e.preventDefault()
      // alert("Redirecting to Login Page")
      setModalContent(<LoginFormModal/>)
      // navigate("/")
    }
    return (
        <ul className={"cart-modal"}>
          <div className="cart-header">
            <IoMdClose className="close-cart" onClick={closeModal}/>
            <div className="wallet-info">
              <FaWallet />
              <li>${userWallet?.toFixed(2)}</li>
            </div>
          </div>
          <div className="cart-content">
            <h4>Cart For: {restaurantName}</h4>
            <div className="cart-items">
              Items:
              {Object.values(processedCart)?.map((items, index) => {
                let quantity = items.length
                let item = items[0]
                item = JSON.parse(item)
                total += item.price * quantity
                return <CartItem key={index} item={item} quantity={quantity} />
              })}
            </div>
            {cartItems?.length > 0 ? (<li className="total-price">Total: $ {total.toFixed(2)}</li>) : null}
            <li>
              <button disabled={cartItems.length === 0} onClick={(e) => user ? checkOutLoggedIn(e).then(closeModal) : checkOutLoggedOut(e)}>
                Check Out
              </button>
            </li>
            <li>
              <button onClick={() => {
                setCartItems([])
                setCartRestaurant(0)
                closeModal()
              }}>
                Clear Cart
              </button>
            </li>
          </div>
        </ul>
    )
}

export default CartModal;
