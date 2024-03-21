// action type creator
const ADD_FUNDS = "wallet/addFunds";
const GET_FUNDS = "wallet/getFunds";
const REMOVE_FUNDS = "wallet/removeFunds";
const CLEAR_FUNDS = "wallet/clearFunds";

//action creator
export const addFunds = (funds, userId) => {
  return {
    type: ADD_FUNDS,
    funds,
    userId
  };
};

export const getFunds = (funds, userId) => {
  return {
    type: GET_FUNDS,
    funds,
    userId
  };
};

export const removeFunds = (funds, userId) => {
  return {
    type: REMOVE_FUNDS,
    funds,
    userId
  };
};

export const clearFunds = () => {
  return {
    type: CLEAR_FUNDS
  }
}

//thunk action creator
export const increaseFunds = (funds, userId) => async (dispatch) => {
  const response = await fetch(`/api/users/${userId}/add-funds`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({funds: funds}),
  });
  if (response.ok) {
    const newFunds = await response.json()
    dispatch(addFunds(newFunds, userId));
    return newFunds
  }
}

export const decreaseFunds = (funds, userId) => async (dispatch) => {
  const response = await fetch(`/api/users/${userId}/add-funds`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({funds: funds}),
  });
  if (response.ok) {
    const newFunds = await response.json()
    dispatch(addFunds(newFunds, userId));
    return newFunds
  }
}

export const loadFunds = (userId) => async (dispatch) => {
  if (userId) {
    const response = await fetch(`/api/users/${userId}/get-funds`);
    if (response.ok) {
      const funds = await response.json()
      dispatch(getFunds(funds, userId));
      return funds
    }
  }
}

//reducer
const walletReducer = (state = {}, action) => {
  switch (action.type) {
    case ADD_FUNDS: {
      const walletState = { ...state, [action.userId]: action.funds} ;
      return walletState;
    }
    case GET_FUNDS:
      return { ...state, [action.userId]: action.funds };
    case REMOVE_FUNDS:
      return { ...state, [action.userId]: action.funds };
    case CLEAR_FUNDS:
      return {};
    default:
      return state;
  }
};

export default walletReducer;
