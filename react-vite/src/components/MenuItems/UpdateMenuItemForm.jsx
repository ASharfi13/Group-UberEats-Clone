import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { fetchMenuItem, editMenuItem, getMenuItemTypes } from "../../redux/menuItemReducer";

export default function UpdateMenuItem() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { menuItemId } = useParams();
  const menuItem = useSelector((state) => state.menuItemState[menuItemId]);

  const [name, setName] = useState(menuItem?.name);
  const [price, setPrice] = useState(menuItem?.price);
  const [type, setType] = useState(menuItem?.type);
  const [image, setImage] = useState(menuItem?.imageUrl);
  const [errors, setErrors] = useState({});

  const menuItemTypes = useSelector((state) => state.menuItemState.types)

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

  const onSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      name,
      price,
      type,
      imageUrl: image,
    };

    const newItem = await dispatch(editMenuItem(menuItemId, payload));
    if (newItem.errors) setErrors(newItem.errors)
    else navigate(`/restaurants/${newItem.restaurant_id}`)
  };
  return (
    <div>
      {menuItem && menuItemTypes && (
        <div>
          <form onSubmit={onSubmit}>
            <h1>Update Your Menu Item</h1>
            <div>
              <input
                type="text"
                placeholder="Enter A Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                // required
              ></input>
              <p className="errors">{errors.name ? errors.name : null}</p>
            </div>

            <div>
              <input
                type="text"
                placeholder="Enter A Price"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
                // required
              ></input>
              <p className="errors">{errors.price ? errors.price : null}</p>
            </div>
            <div>
              <select value={type} onChange={(e) => setType(e.target.value)}>
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
                type="url"
                placeholder="Enter New Image Url"
                value={image}
                onChange={(e) => setImage(e.target.value)}
              ></input>
              <p className="errors">
                {errors.imageUrl ? errors.imageUrl : null}
              </p>
            </div>
            <button type="submit">Submit</button>
          </form>
        </div>
      )}
    </div>
  );
}
