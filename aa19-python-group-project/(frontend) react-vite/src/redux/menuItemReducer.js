import { csrfFetch } from "./csrf";

//action type creator
const LOAD_MENU_ITEM = "menu-item/loadMenuItem";

//action creator
export const loadMenuItem = (menu_item) => {
  return {
    type: LOAD_MENU_ITEM,
    menu_item,
  };
};

//thunk action creator
export const fetchMenuItem = (menu_itemId) => async (dispatch) => {
  const response = await fetch(`/api/menu-item/${menu_itemId}`);
  const menu_item = await response.json();
  dispatch(loadMenuItem(menu_item));
};

//selectors if needed

//reducer
const menuItemReducer = (state = {}, action) => {
  switch (action.type) {
    case LOAD_MENU_ITEM:
      return { ...state, [action.menu_item.id]: action.menu_item };
    // case LOAD_ALLSPOTS: {
    //   const spotsState = {};
    //   action.spots.Spots.forEach((spot) => {
    //     spotsState[spot.id] = spot;
    //   });
    //   return spotsState;
    // }
    // case LOAD_OWNERSPOTS: {
    //   const spotState = {};
    //   action.spots.Spots.forEach((spot) => {
    //     spotState[spot.id] = spot;
    //   });
    //   return spotState;
    // }
    // case ADD_SPOT:
    //   return { ...state, [action.spot.id]: action.spot };
    // case ADD_SPOTIMAGE:
    //   return { ...state, [action.image.id]: action.image };
    // case REMOVE_SPOT: {
    //   const newState = { ...state };
    //   delete newState[action.spotId];
    //   return newState;
    // }
    // case UPDATE_SPOT:
    //   return { ...state, [action.spot.id]: action.spot };

    default:
      return state;
  }
};

export default menuItemReducer;
