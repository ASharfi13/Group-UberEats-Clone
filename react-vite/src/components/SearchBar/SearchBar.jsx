import { FaSearch } from "react-icons/fa";
import { useSelector, useDispatch } from "react-redux";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { useEffect, useState } from "react";
import "./SearchBar.css"

function SearchBar() {
    const dispatch = useDispatch();
    const restaurants = useSelector((state) => state.restaurantState);
    const restaurantArr = Object.values(restaurants);
    const [input, setInput] = useState("");

    useEffect(() => {
        dispatch(fetchAllRestaurants());
      }, [dispatch]);

    return (
        <div className="search-bar" onClick={(e) => handleFeature(e)}>
            <FaSearch />
            <input
            type="text"
            name="search-bar"
            placeholder="Search for a restaurant"
            />
        </div>
      )
}

export default SearchBar
