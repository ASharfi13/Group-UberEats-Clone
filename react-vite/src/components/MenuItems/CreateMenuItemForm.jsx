import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { writeMenuItem, getMenuItemTypes } from "../../redux/menuItemReducer";
import { useNavigate, useParams } from "react-router-dom";
import "./UpdateMenuItemForm.css";

export default function MenuItemForm() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);
  const menuItems = useSelector((state) => state.menuItemState);
  const { restaurantId } = useParams();

  const [name, setName] = useState("");
  const [type, setType] = useState("");
  const [price, setPrice] = useState(0);
  const [image, setImage] = useState("");
  const [errors, setErrors] = useState({});

  const menuItemTypes = useSelector((state) => state.menuItemState.types);

  useEffect(() => {
    dispatch(getMenuItemTypes());
  }, [dispatch]);

  const onSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      name,
      type,
      price,
      imageUrl: image,
    };

    const newItem = await dispatch(writeMenuItem(restaurantId, payload));
    if (newItem.errors) setErrors(newItem.errors);
    else navigate(`/restaurants/${restaurantId}`);
  };

  return (
    <>
      {menuItemTypes && (
        <div className="update-menu-page">
          <form className="update-form" onSubmit={onSubmit}>
            <h1 className="update-menu-title">Create A New Menu Item</h1>
            <div>
              <input
                className="input-area"
                type="text"
                placeholder="Enter item name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                // required
              ></input>
              <p className="errors">{errors.name ? errors.name : null}</p>
            </div>

            <div>
              <input
                className="input-area"
                type="number"
                placeholder="Enter the price"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
                // required
              ></input>
              <p className="errors">{errors.price ? errors.price : null}</p>
            </div>
            <div>
              <select
                className="input-area"
                value={type}
                onChange={(e) => setType(e.target.value)}
              >
                <option value={""} disabled selected>
                  Select Type
                </option>
                {menuItemTypes.map((menuItem, idx) => (
                  <option key={idx}>{menuItem}</option>
                ))}
              </select>
              <p className="errors">{errors.type ? errors.type : null}</p>
            </div>
            <div>
              <input
                className="input-area"
                type="url"
                placeholder="Enter Image Url"
                value={image}
                onChange={(e) => setImage(e.target.value)}
              ></input>
              <p className="errors">
                {errors.imageUrl ? errors.imageUrl : null}
              </p>
            </div>
            <button className="menu-submit" type="submit">
              Submit
            </button>
          </form>
          <img
            className="res-logo"
            src="https://i.postimg.cc/0yLWjssc/menu-logo.avif"
            alt="menu-logo"
          />
        </div>
      )}
    </>
  );
}
