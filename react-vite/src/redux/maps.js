const LOAD_API_KEY = 'maps/loadAPIKey';

const loadAPIKey = (key) => ({
    type: LOAD_API_KEY,
    payload: key
});

export const getKey = () => async (dispatch) => {
    const res = await fetch("/api/maps/key", {
        method: "POST"
    });
    const data = await res.json();
    dispatch(loadAPIKey(data.key));
}

const initialState = { key: null };

const mapsReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_API_KEY:
            return { key: action.payload }
        default:
            return state
    }
};

export default mapsReducer
