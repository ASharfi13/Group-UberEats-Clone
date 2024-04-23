import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaShoppingCart, FaWallet } from 'react-icons/fa';
import { useShoppingCart } from "../../context/CartContext";
import { checkOutCart } from "../../redux/shoppingCartReducer";
import { decreaseFunds, increaseFunds, loadFunds } from "../../redux/walletReducer";
import { useNavigate } from "react-router-dom";
import { useModal } from "../../context/Modal";
import ErrorModal from "../ErrorModal/ErrorModal";
import LoginFormModal from "../LoginFormModal";
import OpenSideModalButton from "../OpenSideModalButton";
import CartModal from "../CartModal";

function CartButton() {
  const dispatch = useDispatch();
  const user = useSelector((store) => store.session.user);
  const wallets = useSelector((store) => store.walletState);
  const userWallet = wallets ? wallets[user?.id] : null;
  const restaurants = useSelector((store) => store.restaurantState)
  const { cartItems, setCartItems, cartRestaurant, setCartRestaurant } = useShoppingCart();
  const restaurantName = cartItems?.length > 0 ? JSON.parse(cartItems[0]).restaurant : ""

  useEffect(() => {
    dispatch(loadFunds(user?.id))
  }, [dispatch, user?.id])

  return (
    <div className="cart-button">
      <OpenSideModalButton
        buttonText={<><FaShoppingCart /><span>{cartItems?.length} items</span></>}
        modalComponent={<CartModal
          user={user}
          restaurantName={restaurantName}
          userWallet={userWallet}
          cartItems={cartItems}
          setCartItems={setCartItems}
          cartRestaurant={cartRestaurant}
          setCartRestaurant={setCartRestaurant}
          restaurants={restaurants} />}
        modalSide="right"
      />
      {/* {showMenu && (
        <ul className={"cart-dropdown"} ref={ulRef}>
          <div className="cart-header">
            <IoMdClose className="close-cart" onClick={closeMenu}/>
            <div className="wallet-info">
              <FaWallet />
              <li>${userWallet?.toFixed(2)}</li>
            </div>
          </div>
          <div className="cart-content">
            <h4>Cart For: {restaurantName}</h4>
            <div className="cart-items">
              Items:
              {cartItems?.map((item, index) => {
                item = JSON.parse(item)
                total += item.price
                return <li key={index} className="cart-item">
                  {item.name} | $ {item.price}
                </li>
              })}
            </div>
            {cartItems?.length > 0 ? (<li className="total-price">Total: $ {total.toFixed(2)}</li>) : null}
            <li>
              <button disabled={cartItems.length === 0} onClick={(e) => user ? checkOutLoggedIn(e) : checkOutLoggedOut(e)}>
                Check Out
              </button>
            </li>
            <li>
              <button onClick={() => {
                setCartItems([])
                setCartRestaurant(0)
              }}>
                Clear Cart
              </button>
            </li>
          </div>
        </ul>
      )} */}
    </div>
  );
}


export default CartButton;
