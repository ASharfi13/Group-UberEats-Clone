import { FaSearch } from "react-icons/fa";
import { useSelector, useDispatch } from "react-redux";
import { fetchAllRestaurants, getRestaurantTypes } from "../../redux/restaurantReducer";
import { useEffect, useState } from "react";
import "./SearchBar.css"
import { useSearch } from "../../context/SearchContext"
import { useTopModal } from "../../context/TopModal";
import SearchModal from "./SearchModal";

function SearchBar() {
    const dispatch = useDispatch();
    const { setModalContent } = useTopModal();
    const restaurants = useSelector((state) => state.restaurantState);
    const restaurantTypes = restaurants?.types
    const restaurantArr = Object.values(restaurants);
    const { input, setInput, results, setResults, types, setTypes, handleExit } = useSearch();



    const findResults = () => {
        if (input) {
            setResults([])
            const res = restaurantArr.filter(restaurant => restaurant?.name?.toLowerCase().startsWith(input?.toLowerCase()))
            setResults(res)
        }
    }

    const findTypes = () => {
        if (input) {
            setTypes([])
            const res = restaurantTypes.filter(type => type?.name?.toLowerCase().startsWith(input?.toLowerCase()))
            setTypes(res)
        }
    }

    useEffect(() => {
        setResults([])
        setTypes([])
        findResults()
        findTypes()
    }, [input])

    useEffect(() => {
        dispatch(fetchAllRestaurants());
        dispatch(getRestaurantTypes());
      }, [dispatch]);

    return (
        <div className="search-container">
            <div className="search-bar">
                <FaSearch />
                <input
                type="text"
                name="search-bar"
                value={input}
                onFocus={(e) => setModalContent(<SearchModal restaurantTypes={restaurantTypes}/>)}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Search for a restaurant"
                />
            </div>
        </div>
      )
}

export default SearchBar
