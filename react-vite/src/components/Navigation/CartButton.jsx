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
  const {cartItems, setCartItems} = useShoppingCart();
//   console.log("THIS IS THE CART", cartItems)
  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  const checkOut = async (e) => {
    e.preventDefault()
    const newOrder = await dispatch(checkOutCart(user.id, cartItems))
    setCartItems([])
    navigate("/orders")
  }



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


  return (
    <>
      <button onClick={toggleMenu}>
        <FaShoppingCart />
      </button>
      {showMenu && (
        <ul className={"cart-dropdown profile-dropdown"} ref={ulRef}>
            <li>IN THE CART</li>

          {cartItems?.map((item, index) => {
            item = JSON.parse(item)
            return <li key={index}>
                {item.name}
            </li>
          })}
          <li>
            <button onClick={(e) => checkOut(e)}>
                Check Out
            </button>
          </li>
        </ul>
      )}
    </>
  );
}


export default CartButton;
