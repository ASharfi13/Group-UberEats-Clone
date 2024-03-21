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
    userId,
  };
};

export const getFunds = (funds) => {
  return {
    type: GET_FUNDS,
    funds,
  };
};

export const removeFunds = (funds, userId) => {
  return {
    type: ADD_FUNDS,
    funds,
    userId,
  };
};

//thunk action creator

//reducer
const walletReducer = (state = {}, action) => {};

export default walletReducer;
