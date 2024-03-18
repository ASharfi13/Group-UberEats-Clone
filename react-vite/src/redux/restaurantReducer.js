//action type creator
const LOAD_RESTAURANT = "restaurant/loadRestaurant";
const LOAD_ALL_RESTAURANTS = "restaurant/loadAllRestaurants";
const LOAD_OWNER_RESTAURANTS = "restaurant/ownerRestaurants";
const ADD_RESTAURANT = "restaurant/addRestaurant";
const REMOVE_RESTAURANT = "restaurant/removeRestaurant";
const UPDATE_RESTAURANT = "restaurant/updateRestaurant";

//action creator
export const loadRestaurant = (restaurant) => {
  return {
    type: LOAD_RESTAURANT,
    restaurant,
  };
};

export const loadAllRestaurants = (restaurants) => {
  return {
    type: LOAD_ALL_RESTAURANTS,
    restaurants,
    //payload
  };
};

export const loadOwnerRestaurants = (restaurants) => {
  return {
    type: LOAD_OWNER_RESTAURANTS,
    restaurants,
  };
};

export const addRestaurant = (restaurant) => {
  return {
    type: ADD_RESTAURANT,
    restaurant,
  };
};

export const removeRestaurant = (restaurantId) => {
  return {
    type: REMOVE_RESTAURANT,
    restaurantId,
  };
};

export const updateRestaurant = (restaurant) => {
  return {
    type: UPDATE_RESTAURANT,
    restaurant,
  };
};

//thunk action creator
export const fetchRestaurant = (restaurantId) => async (dispatch) => {
  const response = await fetch(`/api/restaurants/${restaurantId}`);
  const restaurant = await response.json();
  dispatch(loadRestaurant(restaurant));
};

export const fetchAllRestaurants = () => async (dispatch) => {
  const response = await fetch("/api/restaurants");
  const restaurants = await response.json();
  dispatch(loadAllRestaurants(restaurants));
};

export const fetchOwnerRestaurants = () => async (dispatch) => {
  const response = await csrfFetch(`/api/restaurants/current`);
  const restaurants = await response.json();
  dispatch(loadOwnerRestaurants(restaurants));
};

export const writeRestaurant = (payload) => async (dispatch) => {
  const response = await csrfFetch("/api/restaurants", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  console.log(response);
  const restaurant = await response.json();
  if (response.status !== 201) {
    return restaurant;
  }
  if (response.ok) {
    dispatch(addRestaurant(restaurant));
    return restaurant;
  }
};

export const deleteRestaurant = (restaurantId) => async (dispatch) => {
  const response = await csrfFetch(`/api/restaurants/${restaurantId}`, {
    method: "DELETE",
  });
  if (response.ok) {
    const restaurant = await response.json();
    // console.log(spotId, "thunk");
    // console.log(spot, "here is another log");
    dispatch(removeRestaurant(restaurant.restaurantId));
    return restaurant;
  }
};

export const editRestaurant = (restaurantId, payload) => async (dispatch) => {
  const response = await csrfFetch(`/api/restaurant/${restaurantId}`, {
    method: "PUT",
    header: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const restaurant = await response.json();
    dispatch(updateRestaurant(payload));
    return restaurant;
  }
};

//selectors if needed

//reducer
const restaurantReducer = (state = {}, action) => {
  switch (action.type) {
    case LOAD_RESTAURANT:
      return { ...state, [action.restaurant.id]: action.restaurant };
    case LOAD_ALL_RESTAURANTS: {
      const restaurantState = {};
      action.restaurants.restaurants.forEach((restaurant) => {
        restaurantState[restaurant.id] = restaurant;
      });
      return restaurantState;
    }
    case LOAD_OWNER_RESTAURANTS: {
      const restaurantState = {};
      action.restaurants.restaurants.forEach((restaurant) => {
        restaurantState[restaurant.id] = restaurant;
      });
      return restaurantState;
    }
    case ADD_RESTAURANT:
      return { ...state, [action.restaurant.id]: action.restaurant };
    // case ADD_SPOTIMAGE:
    //   return { ...state, [action.image.id]: action.image };
    case REMOVE_RESTAURANT: {
      const newState = { ...state };
      delete newState[action.restaurant.id];
      return newState;
    }
    case UPDATE_RESTAURANT:
      return { ...state, [action.restaurant.id]: action.restaurant };
    default:
      return state;
  }
};

export default restaurantReducer;
