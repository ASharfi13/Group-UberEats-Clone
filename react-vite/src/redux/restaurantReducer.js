//action type creator
const LOAD_RESTAURANT = "restaurant/loadRestaurant";
const LOAD_ALL_RESTAURANTS = "restaurant/loadAllRestaurants";
const LOAD_OWNER_RESTAURANTS = "restaurant/ownerRestaurants";
const ADD_RESTAURANT = "restaurant/addRestaurant";
const REMOVE_RESTAURANT = "restaurant/removeRestaurant";
const UPDATE_RESTAURANT = "restaurant/updateRestaurant";
const LOAD_RESTAURANT_TYPES = "restaurant/loadTypes";
const CLEAR_RESTAURANTS = "restaurant/clearRestaurants";

//action creator
export const loadRestaurantTypes = (restaurantTypes) => {
  return {
    type: LOAD_RESTAURANT_TYPES,
    restaurantTypes,
  };
};

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

export const clearRestaurants = () => {
  return {
    type: CLEAR_RESTAURANTS
  };
};

//thunk action creator
export const getRestaurantTypes = () => async (dispatch) => {
  const response = await fetch(`/api/restaurants/types`);
  const restaurantTypes = await response.json();
  dispatch(loadRestaurantTypes(restaurantTypes));
};

export const fetchRestaurant = (restaurantId) => async (dispatch) => {
  const response = await fetch(`/api/restaurants/${restaurantId}`);
  const restaurant = await response.json();
  dispatch(loadRestaurant(restaurant));
};

export const fetchAllRestaurants = () => async (dispatch) => {
  const response = await fetch("/api/restaurants/");
  const restaurants = await response.json();
  dispatch(loadAllRestaurants(restaurants));
};

export const fetchOwnerRestaurants = () => async (dispatch) => {
  const response = await fetch(`/api/restaurants/current`);
  const restaurants = await response.json();
  dispatch(loadOwnerRestaurants(restaurants));
};

export const writeRestaurant = (payload) => async (dispatch) => {
  const response = await fetch("/api/restaurants/", {
    method: "POST",
    body: payload,
  });
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
  const response = await fetch(`/api/restaurants/${restaurantId}`, {
    method: "DELETE",
  });
  if (response.ok) {
    const restaurant = await response.json();
    dispatch(removeRestaurant(restaurantId));
    return restaurant;
  }
};

export const editRestaurant = (restaurantId, payload) => async (dispatch) => {
  const response = await fetch(`/api/restaurants/${restaurantId}`, {
    method: "PUT",
    body: payload,
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
    case LOAD_RESTAURANT_TYPES:
      return { ...state, ["types"]: action.restaurantTypes };
    case LOAD_RESTAURANT:
      return { ...state, [action.restaurant.id]: action.restaurant };
    case LOAD_ALL_RESTAURANTS: {
      const restaurantState = { ...state };
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
      delete newState[action.restaurantId];
      return newState;
    }
    case UPDATE_RESTAURANT:
      return { ...state, [action.restaurant.id]: action.restaurant };
    case CLEAR_RESTAURANTS:
      return {};
    default:
      return state;
  }
};

export default restaurantReducer;
