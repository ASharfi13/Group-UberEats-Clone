import { createBrowserRouter } from "react-router-dom";
import LoginFormPage from "../components/LoginFormPage";
import SignupFormPage from "../components/SignupFormPage";
import Layout from "./Layout";
import LandingPage from "../../src/components/LandingPage/LandingPage";
import SingleRestaurant from "../components/Restaurant/SingleRestaurant";
import CreateRestaurantForm from "../../src/components/Restaurant/CreateRestaurantForm"
import UpdateRestaurant from "../components/Restaurant/UpdateRestaurantForm";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "restaurants/:restaurantId",
        element: <SingleRestaurant />,
      },
      {
        path: "restaurants/new",
        element: <CreateRestaurantForm/>
      },
      {
        path: "restaurants/:restaurantId/update",
        element: <UpdateRestaurant/>
      }
    ],
  },
]);
