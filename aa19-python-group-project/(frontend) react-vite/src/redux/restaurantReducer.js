import { csrfFetch } from "./csrf";

//action type creator
const LOAD_RESTAURANT = "spot/loadRestaurant";
const LOAD_ALL_RESTAURANTS = "spot/loadAllRestaurants";
const LOAD_OWNER_RESTAURANTS = "spot/ownerRestaurants";
const ADD_RESTAURANT = "spot/addRestaurant";
const REMOVE_RESTAURANT = "spot/removeRestaurant";
const UPDATE_RESTAURANT = "spot/updateRestaurant";

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
    case LOAD_MENU_ITEM:
      return { ...state, [action.menu_item.id]: action.menu_item };
    case LOAD_ALLMENU_ITEMS: {
      const menuItemState = {};
      action.menu_item.Menu_Item.forEach((menu_item) => {
        menuItemState[menu_item.id] = menu_item;
      });
      return menuItemState;
    }
    case LOAD_OWNWER_MENU_ITEMS: {
      const menuItemState = {};
      action.menu_item.Menu_Item.forEach((menu_item) => {
        menuItemState[menu_item.id] = menu_item;
      });
      return menuItemState;
    }
    case ADD_MENU_ITEM:
      return { ...state, [action.menu_item.id]: action.menu_item };
    // case ADD_SPOTIMAGE:
    //   return { ...state, [action.image.id]: action.image };
    case REMOVE_MENU_ITEM: {
      const newState = { ...state };
      delete newState[action.menu_itemId];
      return newState;
    }
    case UPDATE_MENU_ITEM:
      return { ...state, [action.menu_item.id]: action.menu_item };

    default:
      return state;
  }
};

export default restaurantReducer;
