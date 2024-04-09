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
  const [image, setImage] = useState(null);
  const [imageURL, setImageURL] = useState(null);
  const [imageLoading, setImageLoading] = useState(false)
  const [errors, setErrors] = useState({});

  const menuItemTypes = useSelector((state) => state.menuItemState.types);

  const handleFile = (e) => {
    e.stopPropagation();
    const tempFile = e.target.files[0]
    if (tempFile.size > 5000000) {
      setErrors({...errors, "image": "Selected Image exceeds maximum file size of 5mb"})
      return
    }
    const newImageURL = URL.createObjectURL(tempFile);
    setImageURL(newImageURL);
    setImage(tempFile);
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("name", name);
    formData.append("type", type);
    formData.append("price", price);
    formData.append("image", image);
    setImageLoading(true);

    const newItem = await dispatch(writeMenuItem(restaurantId, formData));
    if (newItem.errors) setErrors(newItem.errors);
    else navigate(`/restaurants/${restaurantId}`);
  };

  useEffect(() => {
    dispatch(getMenuItemTypes());
  }, [dispatch]);

  return (
    <>
      {menuItemTypes && (
        <div className="update-menu-page">
          <form className="update-form" onSubmit={onSubmit} encType="multipart/form-data">
            <h1 className="update-menu-title">Create A New Menu Item</h1>
            <div className="column-styles">
              <p>Name</p>
              <input
                className="input-area"
                type="text"
                placeholder="Enter A Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                // required
              ></input>
              <p className="errors">{errors.name ? errors.name : null}</p>
            </div>

            <div className="column-styles">
              <p>Price</p>
              <input
                className="input-area"
                type="text"
                placeholder="Enter A Price"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
                // required
              ></input>
              <p className="errors">{errors.price ? errors.price : null}</p>
            </div>
            <div className="column-styles">
              <p>Type</p>
              <select
                className="input-area"
                value={type}
                onChange={(e) => setType(e.target.value)}
              >
                <option value={""} disabled defaultValue={""}>
                  Select Type
                </option>
                {menuItemTypes.map((menuItem, idx) => (
                  <option key={idx}>{menuItem}</option>
                ))}
              </select>
              <p className="errors">{errors.type ? errors.type : null}</p>
            </div>
            <div className="column-styles">
              <p>Image</p>
              <input
                className="input-area"
                type="file"
                accept="image/*"
                onChange={(e) => handleFile(e)}
              />
              {(imageLoading)&& <p>Loading...</p>}
              <p className="errors">
                {errors.image ? errors.image : null}
              </p>
            </div>
            <button className="menu-submit" type="submit">
              Submit
            </button>
          </form>
          <img
            className="res-logo"
            src={imageURL ? imageURL : "https://i.postimg.cc/8cdCxDbc/restaurant-logo.jpg"}
            alt="menu-logo"
          />
        </div>
      )}
    </>
  );
}
