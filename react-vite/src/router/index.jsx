import { createBrowserRouter } from "react-router-dom";
import Layout from "./Layout";
import LandingPage from "../../src/components/LandingPage";
import SingleRestaurant from "../components/Restaurant/SingleRestaurant";
import CreateRestaurantForm from "../../src/components/Restaurant/CreateRestaurantForm";
import UpdateRestaurant from "../components/Restaurant/UpdateRestaurantForm";
import OrdersPage from "../components/OrdersPage";
import MenuItemForm from "../components/MenuItems/CreateMenuItemForm";
import UpdateMenuItem from "../components/MenuItems/UpdateMenuItemForm";
import ReviewsPage from "../components/Reviews/ReviewsPage";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },
      {
        path: "restaurants/:restaurantId",
        element: <SingleRestaurant />,
      },
      {
        path: "restaurants/new",
        element: <CreateRestaurantForm />,
      },
      {
        path: "restaurants/:restaurantId/update",
        element: <UpdateRestaurant />,
      },
      {
        path: "restaurants/:restaurantId/add-item",
        element: <MenuItemForm />,
      },
      {
        path: "menu-items/:menuItemId/update",
        element: <UpdateMenuItem />,
      },
      {
        path: "orders",
        element: <OrdersPage />,
      },
      {
        path: "/restaurants/:restaurantId/add-review",
        element: <ReviewsPage />,
      },
    ],
  },
]);
