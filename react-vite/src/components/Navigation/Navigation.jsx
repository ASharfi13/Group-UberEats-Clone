import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import CartButton from "./CartButton";
import { FaSearch } from "react-icons/fa";
import "./Navigation.css";

function Navigation() {
  const handleFeature = (e) => {
    alert("Feature Coming Soon");
  };

  return (
    <ul className="nav-bar">
      <div className="left-side-nav-bar">
        <ProfileButton />
        <NavLink to="/" className="main-logo">
          <img
            className="landing-logo"
            src="https://i.postimg.cc/zBFrwRpH/logo-landing-page-removebg-preview.png"
            alt="logo"
          />
        </NavLink>
        <div className="delivery-pickup">
          <button className="button-delivery" onClick={handleFeature}>
            Delivery
          </button>
          <button className="button-pickup" onClick={handleFeature}>
            Pickup
          </button>
        </div>
      </div>

      <div className="right-side-nav-bar">
        <div className="search-bar" onClick={(e) => handleFeature(e)}>
          <FaSearch />
          <input
            type="text"
            name="search-bar"
            placeholder="Search for a restaurant"
          />
        </div>
        <CartButton />
      </div>
    </ul>
  );
}

export default Navigation;
