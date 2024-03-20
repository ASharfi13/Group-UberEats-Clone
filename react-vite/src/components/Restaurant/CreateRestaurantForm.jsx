import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { writeRestaurant } from "../../redux/restaurantReducer";
import { useNavigate } from "react-router-dom";
// import Layout from "../../router/Layout"

function RestaurantForm() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);
  const restaurants = useSelector((state) => state.restaurantState);

    // console.log(user)

  const [name, setName] = useState("");
  const [location, setLocation] = useState("");
  const [type, setType] = useState("");
  const [image, setImage] = useState("");
  const [errors, setErrors] = useState({});

  const restaurantTypes = [
    "American",
    "Chinese",
    "Indian",
    "Mexican",
    "Korean",
    "Thai",
    "Filipino",
    "Other",
  ];

  //   const errObj = {};

  useEffect(() => {
    const errObj = {};

    if (name.length < 3) {
      errObj["nameLength"] = "Name must be at least 3 Characters";
    }

    if (location.length == 0) {
      errObj["locationMissing"] = "Location is required";
    }

    if (image.length == 0) {
      errObj["imageMissing"] = "Image is required";
    }

    setErrors(errObj);
  }, [name, location, image]);

  const onSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      name,
      location,
      type,
      imageUrl: image,
    };

    if (Object.values(errors).length === 0) {
      dispatch(writeRestaurant(payload));
    } else {
      alert("Did not work");
    }

    // try{
    //     const newRestaurant = await dispatch(writeRestaurant(payload))
    // } catch(e) {
    //     const results = await e.json()
    //     setErrors(results.errors)
    // }
  };

  return (
    <div>
      <form onSubmit={onSubmit}>
        <h1>Create A New Restaurant</h1>
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
            placeholder="Enter A Location"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            // required
          ></input>
          <p className="errors">{errors.location ? errors.location : null}</p>
        </div>
        <div>
          <select value={type} onChange={(e) => setType(e.target.value)}>
            <option value={""} disabled selected>
              Select Type
            </option>
            {restaurantTypes.map((restaurant, idx) => (
              <option key={idx}>{restaurant}</option>
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
  );
}

export default RestaurantForm;
