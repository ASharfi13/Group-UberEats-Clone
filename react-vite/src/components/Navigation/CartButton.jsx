import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaShoppingCart } from 'react-icons/fa';
import { useShoppingCart } from "../../context/CartContext";
import { checkOutCart } from "../../redux/shoppingCartReducer";
import { useNavigate } from "react-router-dom";

function CartButton() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();
  const { cartItems, setCartItems, cartRestaurant, setCartRestaurant } = useShoppingCart();
  //   console.log("THIS IS THE CART", cartItems)
  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  const checkOutLoggedIn = async (e) => {
    e.preventDefault()
    const newOrder = await dispatch(checkOutCart(user.id, cartItems))
    setCartItems([])
    setCartRestaurant(0)
    navigate("/orders")
  }

  const checkOutLoggedOut = async (e) => {
    e.preventDefault()
    alert("Redirected to Login Page")
    navigate("/login")
  }

  const restaurantName = cartItems?.length > 0 ? JSON.parse(cartItems[0]).restaurant : ""

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    // document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu, cartItems.length]);

  const closeMenu = () => setShowMenu(false);

  let total = 0


  return (
    <>
      <button onClick={toggleMenu}>
        <FaShoppingCart />
      </button>
      {showMenu && (
        <ul className={"cart-dropdown profile-dropdown"} ref={ulRef}>
          <li>Cart For {restaurantName}</li>
          {cartItems?.map((item, index) => {
            item = JSON.parse(item)
            total += item.price
            return <li key={index}>
              {item.name} | {item.price}
            </li>
          })}
          {cartItems?.length > 0 ? (<li>Total Price : {total.toFixed(2)}</li>) : null}
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
        </ul>
      )}
    </>
  );
}


export default CartButton;
