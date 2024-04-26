import { useEffect } from "react";
import { thunkLogout } from "../../redux/session";
import { useNavigate } from "react-router-dom";
import { FaRegUserCircle, FaReceipt, FaComment, FaWallet, FaUtensils } from "react-icons/fa";
import { useSideModal } from "../../context/SideModal";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import AddFundsModal from "../AddFundsModal";
import "./ProfileModal.css";
import { useDispatch } from "react-redux";
import { useShoppingCart } from "../../context/CartContext";

function ProfileModal({user}) {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { cartItems, setCartItems } = useShoppingCart();
  const { closeModal } = useSideModal();

  const logout = (e) => {
    e.preventDefault();
    dispatch(thunkLogout());
    closeModal();
    setCartItems([]);
    navigate("/");
  };

  const handleClick = (url) => {
    closeModal();
    navigate(url)
  }

  return (
      <ul className={"profile-modal"}>
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
                  <button className="style-hover" onClick={() => handleClick("/orders")}>My Orders</button>
                </li>
                <li className="profile-item">
                  <FaComment />
                  <button className="style-hover" onClick={() => handleClick("/orders/reviews")}>My Reviews</button>
                </li>
                <li className="profile-item">
                  <FaWallet />
                  <OpenModalMenuItem
                  itemText="Add Funds"
                  onItemClick={closeModal}
                  modalComponent={<AddFundsModal />} />
                </li>
                <li className="profile-item">
                  <FaUtensils />
                  <button className="style-hover" onClick={() => handleClick("/restaurants/new")}>Add Restaurant</button>
                </li>
                <li className="logout">
                  <button className="login-button" onClick={logout}>Sign Out</button>
                </li>
              </>
            ) : (
              <>
              <li className="login-button">
                <OpenModalMenuItem
                  itemText="Sign In"
                  onItemClick={closeModal}
                  modalComponent={<LoginFormModal />}
                />
              </li>
              <li className="login-button">
                <OpenModalMenuItem
                  itemText="Sign Up"
                  onItemClick={closeModal}
                  modalComponent={<SignupFormModal />}
                />
              </li>
              </>
            )}
          </ul>
  );
}

export default ProfileModal;
