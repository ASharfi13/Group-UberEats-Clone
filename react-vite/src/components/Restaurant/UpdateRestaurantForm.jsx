import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import {
  fetchRestaurant,
  editRestaurant,
  getRestaurantTypes,
} from "../../redux/restaurantReducer";
import "./CreateRestaurantForm/CreateRestaurantForm.css";

function UpdateRestaurant() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { restaurantId } = useParams();
  const restaurant = useSelector(
    (state) => state.restaurantState[restaurantId]
  );
  const restaurantTypes = useSelector((state) => state.restaurantState.types);

  const [name, setName] = useState(restaurant?.name);
  const [location, setLocation] = useState(restaurant?.location);
  const [type, setType] = useState(restaurant?.type);
  const [image, setImage] = useState(restaurant?.imageUrl);
  const [errors, setErrors] = useState({});

  useEffect(() => {
    dispatch(fetchRestaurant(restaurantId)).then(
      dispatch(getRestaurantTypes())
    );
    setName(restaurant?.name);
    setLocation(restaurant?.location);
    setType(restaurant?.type);
    setImage(restaurant?.imageUrl);
  }, [
    dispatch,
    restaurantId,
    restaurant?.name,
    restaurant?.location,
    restaurant?.type,
    restaurant?.imageUrl,
  ]);

  const onSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      name,
      location,
      type,
      imageUrl: image,
    };

    const response = await dispatch(editRestaurant(restaurantId, payload));
    if (response.errors) setErrors(response.errors);
    else navigate(`/restaurants/${response.id}`);
  };

  return (
    <div>
      {restaurant && restaurantTypes && (
        <div className="restaurant-page-create">
          <form className="restaurant-form" onSubmit={onSubmit}>
            <h1 className="restaurant-title-form">Update Your Restaurant</h1>
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
              <p className="restaurant-errors">
                {errors.name ? errors.name : null}
              </p>
            </div>

            <div className="column-styles">
              <p>Location</p>
              <input
                className="input-area"
                type="text"
                placeholder="Enter A Location"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                // required
              ></input>
              <p className="restaurant-errors">
                {errors.location ? errors.location : null}
              </p>
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
                {restaurantTypes.map((restaurant, idx) => (
                  <option key={idx}>{restaurant}</option>
                ))}
              </select>
              <p className="restaurant-errors">
                {errors.type ? errors.type : null}
              </p>
            </div>
            <div className="column-styles">
              <p>Image Url</p>
              <input
                className="input-area"
                type="url"
                placeholder="Enter New Image Url"
                value={image}
                onChange={(e) => setImage(e.target.value)}
              ></input>
              <p className="restaurant-errors">
                {errors.imageUrl ? errors.imageUrl : null}
              </p>
            </div>
            <button className="restaurant-submit" type="submit">
              Submit
            </button>
          </form>
          <img
            className="res-logo"
            src={restaurant?.imageUrl}
            alt="res-logo"
          />
        </div>
      )}
    </div>
  );
}

export default UpdateRestaurant;
