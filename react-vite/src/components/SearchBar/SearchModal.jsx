import { NavLink } from "react-router-dom"
import { useSearch } from "../../context/SearchContext"
import "./SearchModal.css"
export default function SearchModal({restaurantTypes}) {
    const { results, types, handleExit } = useSearch();
    const topTypes = ["American", "Asian", "Fast Food", "Comfort Food"]

    return (
        <div>
        {results?.length > 0 && <div className="restaurant-results">
            <h2>Restaurants</h2>
        {results?.map(restaurant => (
            <NavLink className="restaurant-result" key={restaurant.id+restaurant.name}onClick={handleExit} to={`/restaurants/${restaurant?.id}`}>
                <img src={restaurant.imageUrl} ></img>
                <div>{restaurant.name}</div>
            </NavLink>
                ))
        }
        </div>}
        {types?.length ?
            <div className="type-results">
                <h2>Categories</h2>
                {types?.map(type => (
                    <NavLink className="type-result" key={type.id+type.name}onClick={handleExit} to={`/?type=${type.name}`}>
                        <img src={type.imageUrl} width="40px" />
                        <div>{type.name}</div>
                    </NavLink>
                ))}
            </div> :
            <div className="type-results">
                <h2>Top Categories</h2>
                {topTypes?.map((type, idx) => (
                    <NavLink className="type-result" key={idx+type} onClick={handleExit} to={`/?type=${type}`}>
                        <img src={restaurantTypes.filter((x) => x.name==type)[0].imageUrl} width="40px" />
                        <div>{type}</div>
                    </NavLink>
            ))}
            </div>}
        </div>
    )
}
