import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import CartButton from "./CartButton";
import "./Navigation.css";

function Navigation() {
  return (
    <ul>
      <div className="left-side-nav-bar">
        <NavLink to="/">
          <img
            className="landing-logo"
            src="https://i.postimg.cc/zBFrwRpH/logo-landing-page-removebg-preview.png"
            alt="logi"
          />
        </NavLink>
      </div>

      <div className="right-side-nav-bar">
        <ProfileButton />
        <CartButton />
      </div>
    </ul>
  );
}

export default Navigation;
