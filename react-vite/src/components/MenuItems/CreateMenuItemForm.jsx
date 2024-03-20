import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { writeMenuItem, getMenuItemTypes } from "../../redux/menuItemReducer";
import { useNavigate, useParams } from "react-router-dom";

export default function MenuItemForm() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);
  const menuItems = useSelector((state) => state.menuItemState);
  const { restaurantId } = useParams()

  const [name, setName] = useState("");
  const [type, setType] = useState("");
  const [price, setPrice] = useState(0);
  const [image, setImage] = useState("");
  const [errors, setErrors] = useState({});

  const menuItemTypes = useSelector((state) => state.menuItemState.types)

  useEffect(() => {
    dispatch(getMenuItemTypes())
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
    if (newItem.errors) setErrors(newItem.errors)
    else navigate(`/restaurants/${restaurantId}`)
  };

  return (
    <>
    {menuItemTypes &&
    <div>
      <form onSubmit={onSubmit}>
        <h1>Create A New Menu Item</h1>
        <div>
          <input
            type="text"
            placeholder="Enter the name of the item"
            value={name}
            onChange={(e) => setName(e.target.value)}
            // required
          ></input>
          <p className="errors">{errors.name ? errors.name : null}</p>
        </div>

        <div>
          <input
            type="number"
            placeholder="Enter the price of the item"
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
            placeholder="Enter Image Url"
            value={image}
            onChange={(e) => setImage(e.target.value)}
          ></input>
          <p className="errors">{errors.imageUrl ? errors.imageUrl : null}</p>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
    }
    </>
  );
}
