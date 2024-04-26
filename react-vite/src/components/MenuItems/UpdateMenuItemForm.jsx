import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import {
  fetchMenuItem,
  editMenuItem,
  getMenuItemTypes,
} from "../../redux/menuItemReducer";
import "./UpdateMenuItemForm.css";

export default function UpdateMenuItem() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { menuItemId } = useParams();
  const menuItem = useSelector((state) => state.menuItemState[menuItemId]);

  const [name, setName] = useState(menuItem?.name);
  const [price, setPrice] = useState(menuItem?.price);
  const [type, setType] = useState(menuItem?.type);
  const [image, setImage] = useState(null)
  const [imageURL, setImageURL] = useState(menuItem?.imageUrl);
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
    const payload = new FormData();
    payload.append("name", name);
    payload.append("price", price);
    payload.append("type", type);
    payload.append("image", image);

    const newItem = await dispatch(editMenuItem(menuItemId, payload));
    if (newItem.errors) setErrors(newItem.errors);
    else navigate(`/restaurants/${newItem.restaurant_id}`);
  };

  useEffect(() => {
    dispatch(fetchMenuItem(menuItemId)).then(dispatch(getMenuItemTypes()));
    setName(menuItem?.name);
    setPrice(menuItem?.price);
    setType(menuItem?.type);
    setImage(menuItem?.imageUrl);
  }, [
    dispatch,
    menuItemId,
    menuItem?.name,
    menuItem?.price,
    menuItem?.type,
    menuItem?.imageUrl,
  ]);
  return (
    <div>
      {menuItem && menuItemTypes && (
        <div className="update-menu-page">
          <form className="update-form" onSubmit={onSubmit} encType="multipart/form-data">
            <h1 className="update-menu-title">Update Your Menu Item</h1>
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
              <p>Image Url</p>
              <input
                className="input-area"
                type="file"
                accept="image/*"
                onChange={(e) => handleFile(e)}
              ></input>
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
            src={imageURL}
            alt="menu-logo"
          />
        </div>
      )}
    </div>
  );
}
