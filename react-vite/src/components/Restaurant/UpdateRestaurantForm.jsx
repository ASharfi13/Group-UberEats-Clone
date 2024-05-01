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
  const initialTypes = {}
  if (restaurant?.types) restaurantTypes?.forEach((rType) => initialTypes[rType?.name] = restaurant?.types.includes(rType?.name) ? true : false)
  const [types, setTypes] = useState(initialTypes);
  const [image, setImage] = useState(null);
  const [imageURL, setImageURL] = useState(restaurant?.imageUrl)
  const [errors, setErrors] = useState({});

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

  const handleCheck = (typeName) => {
    const newTypes = {...types};
    newTypes[typeName] = !newTypes[typeName];
    setTypes(newTypes)
  }

  const onSubmit = async (e) => {
    e.preventDefault();
    const finalTypes = Object.entries(types).filter(([name, selected]) => selected).map(([name, selected]) => name)
    const formData = new FormData();
    formData.append("name", name);
    formData.append("location", location);
    formData.append("types", JSON.stringify(finalTypes));
    formData.append("image", image);

    const response = await dispatch(editRestaurant(restaurantId, formData));
    if (response.errors) setErrors(response.errors);
    else navigate(`/restaurants/${response.id}`);
  };

  useEffect(() => {
    dispatch(fetchRestaurant(restaurantId)).then(
      dispatch(getRestaurantTypes())
    );
    setName(restaurant?.name);
    setLocation(restaurant?.location);
    setImage(restaurant?.imageUrl);
    setTypes(initialTypes);
  }, [
    dispatch,
    restaurantId,
    restaurant?.name,
    restaurant?.location,
    restaurant?.imageUrl,
    restaurant?.types?.length,
    initialTypes.length
  ]);

  return (
    <div>
      {restaurant && restaurantTypes && (
        <div className="restaurant-page-create">
          <form className="restaurant-form" onSubmit={onSubmit} encType="multipart/form-data">
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
              <p>Categories: </p>
              <div className="type-selector">
                {restaurantTypes?.map((rType) => (
                  <label key={rType.id}>
                    {rType?.name}
                    <input
                      type="checkbox"
                      id={rType.id}
                      name={rType.name}
                      value={rType.value}
                      checked={types[rType.name]}
                      onChange={() => handleCheck(rType.name)} />
                  </label>
                ))}
              </div>
              {/* <select
                className="input-area"
                value={type}
                onChange={(e) => setType(e.target.value)}
              >
                <option value={""} disabled defaultValue={""}>
                  Select Type
                </option>
                {restaurantTypes.map((restaurant, idx) => (
                  <option key={idx}>{restaurant.name}</option>
                ))}
              </select> */}
              <p className="restaurant-errors">
                {errors.type ? errors.type : null}
              </p>
            </div>
            <div className="column-styles">
              <p>Image Url</p>
              <input
                className="input-area"
                type="file"
                accept="image/*"
                onChange={(e) => handleFile(e)}
              />
              <p className="restaurant-errors">
                {errors.image ? errors.image : null}
              </p>
            </div>
            <button className="restaurant-submit" type="submit">
              Submit
            </button>
          </form>
          <img
            className="res-logo"
            src={imageURL}
            alt="res-logo"
          />
        </div>
      )}
    </div>
  );
}

export default UpdateRestaurant;
