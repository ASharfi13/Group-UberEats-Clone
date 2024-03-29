import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { writeRestaurant } from "../../../redux/restaurantReducer";
import { useNavigate } from "react-router-dom";
import { getRestaurantTypes } from "../../../redux/restaurantReducer";
import "./CreateRestaurantForm.css";
// import Layout from "../../router/Layout"

function RestaurantForm() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const restaurantTypes = useSelector((state) => state.restaurantState.types);

  const [name, setName] = useState("");
  const [location, setLocation] = useState("");
  const [type, setType] = useState("");
  const [image, setImage] = useState("");
  const [errors, setErrors] = useState({});

  useEffect(() => {
    dispatch(getRestaurantTypes());
  }, [dispatch]);

  const onSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      name,
      location,
      type,
      imageUrl: image,
    };

    const newRestaurant = await dispatch(writeRestaurant(payload));
    if (newRestaurant.errors) setErrors(newRestaurant.errors);
    else navigate(`/restaurants/${newRestaurant.id}`);
  };

  return (
    <>
      <div>
        {restaurantTypes && (
          <div className="restaurant-page-create">
            <form className="restaurant-form" onSubmit={onSubmit}>
              <h1 className="restaurant-title-form">Create Your Restaurant</h1>
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
              src="https://i.postimg.cc/8cdCxDbc/restaurant-logo.jpg"
              alt="res-logo"
            />
          </div>
        )}
      </div>
    </>
  );
}

export default RestaurantForm;
