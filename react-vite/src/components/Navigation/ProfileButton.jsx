import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FiAlignJustify } from "react-icons/fi";
import { FaRegUserCircle, FaReceipt, FaComment, FaWallet, FaUtensils } from "react-icons/fa";
import { CiLogin, CiLogout } from "react-icons/ci";
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import AddFundsModal from "../AddFundsModal";
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
                <div className="user-info-container">
                  <FaRegUserCircle />
                  <div className="user-info">
                    <li>{user.name}</li>
                    <li>{user.email}</li>
                  </div>
                </div>
                <li className="profile-item">
                  <FaReceipt />
                  <button className="style-hover" onClick={() => navigate("/orders")}>My Orders</button>
                </li>
                <li className="profile-item">
                  <FaComment />
                  <button className="style-hover" onClick={() => navigate("/orders/reviews")}>My Reviews</button>
                </li>
                <li className="profile-item">
                  <FaWallet />
                  <OpenModalMenuItem
                  itemText="Add Funds"
                  onItemClick={closeMenu}
                  modalComponent={<AddFundsModal />} />
                </li>
                <li className="profile-item">
                  <FaUtensils />
                  <button className="style-hover" onClick={() => navigate("/restaurants/new")}>Add Restaurant</button>
                </li>
                <li className="logout">
                  <button className="style-hover" onClick={logout}>Sign Out</button>
                </li>
              </>
            ) : (
              <>
              <li className="profile-item">
                <CiLogin />
                <OpenModalMenuItem
                  itemText="Log In"
                  onItemClick={closeMenu}
                  modalComponent={<LoginFormModal />}
                />
              </li>
              <li className="profile-item ending">
                <CiLogout />
                <OpenModalMenuItem
                  itemText="Sign Up"
                  onItemClick={closeMenu}
                  modalComponent={<SignupFormModal />}
                />
              </li>
              </>
            )}
          </ul>
        )}
      </div>
    </>
  );
}

export default ProfileButton;
