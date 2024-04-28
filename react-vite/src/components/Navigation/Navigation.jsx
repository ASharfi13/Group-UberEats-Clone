import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import CartButton from "./CartButton";
import OpenModalButton from "../OpenModalButton";
import "./Navigation.css";
import SearchBar from "../SearchBar";
import { RiMapPin2Line } from "react-icons/ri";
import { FaChevronDown } from "react-icons/fa";
import { useSearch } from "../../context/SearchContext";

function Navigation() {
  const handleFeature = (e) => {
    alert("Feature Coming Soon");
  };
  const { handleExit } = useSearch();

  return (
    <ul className="nav-bar">
      <div className="left-side-nav-bar">
        <ProfileButton />
        <NavLink to="/" onClick={handleExit} className="main-logo">
          <img
            className="landing-logo"
            src="https://i.postimg.cc/zBFrwRpH/logo-landing-page-removebg-preview.png"
            alt="logo"
          />
        </NavLink>
        <div className="address-bar">
          <OpenModalButton buttonText={<><RiMapPin2Line /><p>Loc. Coming Soon</p><FaChevronDown/></>}/>
        </div>
      </div>

      {/* <div className="delivery-pickup">
        <button className="button-delivery" onClick={handleFeature}>
          Delivery
        </button>
        <button className="button-pickup" onClick={handleFeature}>
          Pickup
        </button>
      </div> */}


      <div className="right-side-nav-bar">
        <SearchBar />
        <CartButton />
      </div>
    </ul>
  );
}

export default Navigation;
