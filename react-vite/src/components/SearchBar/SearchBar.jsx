import { FaSearch } from "react-icons/fa";
import { useSelector, useDispatch } from "react-redux";
import { fetchAllRestaurants } from "../../redux/restaurantReducer";
import { useEffect, useState } from "react";
import "./SearchBar.css"
import { NavLink } from "react-router-dom";

function SearchBar() {
    const dispatch = useDispatch();
    const restaurants = useSelector((state) => state.restaurantState);
    const restaurantArr = Object.values(restaurants);
    const [input, setInput] = useState("");
    const [results, setResults] = useState([]);

    const handleExit = () => {
        setInput("")
        setResults([])
    }

    const findResults = () => {
        if (input) {
            setResults([])
            const res = restaurantArr.filter(restaurant => restaurant?.name?.toLowerCase().startsWith(input?.toLowerCase()))
            setResults(res)
        }
    }

    useEffect(() => {
        setResults([])
        findResults()
    }, [input])

    useEffect(() => {
        dispatch(fetchAllRestaurants());
      }, [dispatch]);

    return (
        <div className="search-container">
        <div className="search-bar">
            <FaSearch />
            <input
            type="text"
            name="search-bar"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Search for a restaurant"
            />
        </div>
        {input && results?.length > 0 && <div className="search-results">
            {results?.map(restaurant => (
                <NavLink onClick={handleExit} to={`/restaurants/${restaurant?.id}`}>
                    <img src={restaurant.imageUrl} width="40px"></img>
                    <div>{restaurant.name}</div>
                </NavLink>
            ))}
        </div>}
        </div>
      )
}

export default SearchBar
