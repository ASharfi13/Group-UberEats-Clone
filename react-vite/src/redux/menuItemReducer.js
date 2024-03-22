//action type creator
const LOAD_MENU_ITEM = "menu-item/loadMenuItem";
const LOAD_ALLMENU_ITEMS = "menu-item/loadAllMenuItems";
const LOAD_OWNER_MENU_ITEMS = "menu-item/ownerMenuItems";
const ADD_MENU_ITEM = "menu-item/addMenuItem";
const REMOVE_MENU_ITEM = "menu-item/removeMenuItem";
const UPDATE_MENU_ITEM = "menu-item/updateMenuItem";
const LOAD_MENU_ITEM_TYPES = "menu-item/loadTypes"

//action creator
export const loadMenuItemTypes = (types) => {
  return {
    type: LOAD_MENU_ITEM_TYPES,
    types
  };
};

export const loadMenuItem = (menu_item) => {
  return {
    type: LOAD_MENU_ITEM,
    menu_item,
  };
};

export const loadAllMenuItems = (menu_items) => {
  return {
    type: LOAD_ALLMENU_ITEMS,
    menu_items,
    //payload
  };
};

export const loadOwnerMenuItems = (menu_items) => {
  return {
    type: LOAD_OWNER_MENU_ITEMS,
    menu_items,
  };
};

export const addMenuItem = (menu_item) => {
  return {
    type: ADD_MENU_ITEM,
    menu_item,
  };
};

export const removeMenuItem = (menu_itemId) => {
  return {
    type: REMOVE_MENU_ITEM,
    menu_itemId,
  };
};

export const updateMenuItem = (menu_item) => {
  return {
    type: UPDATE_MENU_ITEM,
    menu_item,
  };
};

//thunk action creator
export const getMenuItemTypes = () => async (dispatch) => {
  const response = await fetch(`/api/menu-items/types`);
  const types = await response.json();
  dispatch(loadMenuItemTypes(types))
};
export const fetchMenuItem = (menu_itemId) => async (dispatch) => {
  const response = await fetch(`/api/menu-items/${menu_itemId}`);
  const menu_item = await response.json();
  dispatch(loadMenuItem(menu_item));
};

export const fetchAllMenuItems = () => async (dispatch) => {
  const response = await fetch("/api/menu-items");
  const menu_items = await response.json();
  dispatch(loadAllMenuItems(menu_items));
};

export const fetchOwnerMenuItems = (restaurantId) => async (dispatch) => {
  const response = await fetch(`/api/restaurants/${restaurantId}/menu-items`);
  const menu_items = await response.json();
  dispatch(loadOwnerMenuItems(menu_items));
};

export const writeMenuItem = (restaurantId, payload) => async (dispatch) => {
  const response = await fetch(`/api/restaurants/${restaurantId}/menu-items`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const menu_item = await response.json();
  if (response.status !== 201) {
    return menu_item;
  }
  if (response.ok) {
    dispatch(addMenuItem(menu_item));
    return menu_item;
  }
};

export const deleteMenuItem = (menu_itemId) => async (dispatch) => {
  const response = await fetch(`/api/menu-items/${menu_itemId}`, {
    method: "DELETE",
  });
  if (response.ok) {
    const menu_item = await response.json();
    dispatch(removeMenuItem(menu_itemId));
    return menu_item;
  }
};

export const editMenuItem = (menu_itemId, payload) => async (dispatch) => {
  const response = await fetch(`/api/menu-items/${menu_itemId}`, {
    method: "PUT",
    header: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const menu_item = await response.json();
    dispatch(updateMenuItem(payload));
    return menu_item;
  }
};

//selectors if needed

//reducer
const menuItemReducer = (state = {}, action) => {
  switch (action.type) {
    case LOAD_MENU_ITEM_TYPES:
      return { ...state, ["types"]: action.types};
    case LOAD_MENU_ITEM:
      return { ...state, [action.menu_item.id]: action.menu_item };
    case LOAD_ALLMENU_ITEMS: {
      const menuItemState = {};
      action.menu_item.Menu_Item.forEach((menu_item) => {
        menuItemState[menu_item.id] = menu_item;
      });
      return menuItemState;
    }
    case LOAD_OWNER_MENU_ITEMS: {
      const menuItemState = {};
      action.menu_items.items.forEach((menu_item) => {
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

export default menuItemReducer;
