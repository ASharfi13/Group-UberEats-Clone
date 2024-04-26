import { useSelector } from "react-redux";
import { VscThreeBars } from "react-icons/vsc";
import OpenSideModalButton from "../OpenSideModalButton";
import "./ProfileButton.css";
import ProfileModal from "../ProfileModal";

function ProfileButton() {
  const user = useSelector((store) => store.session.user);

  return (
    <>
      <div className="burger-container">
        <OpenSideModalButton className="profilebutton" buttonText={<VscThreeBars viewBox="0 0 24 24" width="20" height="20" className="three-lines"/>} modalComponent={<ProfileModal user={user} />} modalSide={"left"}/>
      </div>
    </>
  );
}

export default ProfileButton;
