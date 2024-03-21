import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FiAlignJustify } from "react-icons/fi";
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { useNavigate } from "react-router-dom";
import { useShoppingCart } from "../../context/CartContext";
import "./ProfileButton.css";

function ProfileButton() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();
  const { cartItems, setCartItems } = useShoppingCart();

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const logout = (e) => {
    e.preventDefault();
    dispatch(thunkLogout());
    closeMenu();
    setCartItems([]);
    navigate("/");
  };

  return (
    <>
      <div className="burger-container">
        <button className="profilebutton" onClick={toggleMenu}>
          <FiAlignJustify className="three-lines" />
        </button>
        {showMenu && (
          <ul className={"profile-dropdown"} ref={ulRef}>
            {user ? (
              <>
                <ul>{user.name}</ul>
                <ul>{user.email}</ul>
                <ul>
                  <button onClick={() => navigate("/orders")}>My Orders</button>
                </ul>
                <ul>
                  <button onClick={logout}>Log Out</button>
                </ul>
                <ul>
                  <button onClick={() => navigate("/restaurants/new")}>
                    Add Restaurant
                  </button>
                </ul>
                <ul>
                  <button onClick={() => navigate("/orders/reviews")}>
                    My Reviews
                  </button>
                </ul>
              </>
            ) : (
              <div className="log-sign">
                <OpenModalMenuItem
                  itemText="Log In"
                  onItemClick={closeMenu}
                  modalComponent={<LoginFormModal />}
                />
                <OpenModalMenuItem
                  itemText="Sign Up"
                  onItemClick={closeMenu}
                  modalComponent={<SignupFormModal />}
                />
              </div>
            )}
          </ul>
        )}
      </div>
    </>
  );
}

export default ProfileButton;
