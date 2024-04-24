import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import CartButton from "./CartButton";
import "./Navigation.css";
import SearchBar from "../SearchBar";

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
      </div>

      <div className="delivery-pickup">
        <button className="button-delivery" onClick={handleFeature}>
          Delivery
        </button>
        <button className="button-pickup" onClick={handleFeature}>
          Pickup
        </button>
      </div>

      <div className="right-side-nav-bar">
        <SearchBar />
        <CartButton />
      </div>
    </ul>
  );
}

export default Navigation;
