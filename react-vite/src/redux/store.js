import {
  legacy_createStore as createStore,
  applyMiddleware,
  compose,
  combineReducers,
} from "redux";
import thunk from "redux-thunk";
import sessionReducer from "./session";
import restaurantReducer from "./restaurantReducer";
import menuItemReducer from "./menuItemReducer";
import shoppingCartReducer from "./shoppingCartReducer";
import reviewReducer from "./reviewReducer";

const rootReducer = combineReducers({
  session: sessionReducer,
  restaurantState: restaurantReducer,
  menuItemState: menuItemReducer,
  orderState: shoppingCartReducer,
  reviewState: reviewReducer,
});

let enhancer;
if (import.meta.env.MODE === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = (await import("redux-logger")).default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
