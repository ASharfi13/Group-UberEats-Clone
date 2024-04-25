import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaShoppingCart } from 'react-icons/fa';
import { useShoppingCart } from "../../context/CartContext";
import { loadFunds } from "../../redux/walletReducer";
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
          restaurants={restaurants}
          userWallet={userWallet} />}
        modalSide="right"
      />
    </div>
  );
}


export default CartButton;
