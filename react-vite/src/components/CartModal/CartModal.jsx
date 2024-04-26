import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
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

function CartModal({restaurants}) {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const user = useSelector(state => state.session.user);
    const wallets = useSelector((store) => store.walletState);
    const userWallet = wallets ? wallets[user?.id] : null;
    const { closeModal } = useSideModal();
    const { setModalContent } = useModal();
    const { cartItems, cartRestaurant, restaurantName, clearCart } = useShoppingCart();
    const processedCart = processCart(cartItems);

    // console.log(cartItems)
    // console.log(processedCart)

    let total = 0

    const checkOutLoggedIn = async (e) => {
      e.preventDefault()
      if (userWallet >= total) {
        await dispatch(checkOutCart(user.id, cartItems))
        await dispatch(decreaseFunds(-total, user.id))
        await dispatch(increaseFunds(total * 0.95, restaurants[cartRestaurant].owner_id))
        clearCart()
        navigate("/orders")
      } else {
        setModalContent(<ErrorModal message={"Insufficient Funds, Please Add Funds in your profile"}/>)
      }
    }

    const checkOutLoggedOut = async (e) => {
      e.preventDefault()
      setModalContent(<LoginFormModal/>)
    }

    return (
        <ul className={"cart-modal"}>
          <div className="cart-header">
            <IoMdClose className="close-cart" onClick={closeModal}/>
            {user && <div className="wallet-info">
              <FaWallet />
              <li>${userWallet?.toFixed(2)}</li>
            </div>}
          </div>
          {cartItems?.length > 0 ? (
          <>
          <div className='cart-name'>
            <img src={restaurants[cartRestaurant]?.imageUrl} width="48px" height="48px"/>
            {restaurantName}
          </div>
          <div className="cart-content">
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
            {cartItems?.length > 0 && (<li className='add-items'>
              <button onClick={() => {
                navigate(`/restaurants/${cartRestaurant}`)
                closeModal()
              }}>Add Items</button>
            </li>)}
            <li>
              <button onClick={(e) => user ? checkOutLoggedIn(e).then(closeModal) : checkOutLoggedOut(e)}>
                Check Out
              </button>
            </li>
            <li>
              <button onClick={() => {
                clearCart()
                closeModal()
              }}>
                Clear Cart
              </button>
            </li>
          </div>
          </>):
          <div className='empty-cart'>
            <img src='https://d3i4yxtzktqr9n.cloudfront.net/web-eats-v2/a023a017672c2488.svg' />
            <h2>Add items to start a cart</h2>
            <p>Once you add items from a restaurant your cart will appear here.</p>
            <button onClick={() => {
              navigate("/");
              closeModal();
            }}>Start Shopping</button>
          </div>}

        </ul>
    )
}

export default CartModal;
