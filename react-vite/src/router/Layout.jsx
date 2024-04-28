import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { ShoppingCartProvider } from "../context/CartContext"
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";
import Footer from "../components/Footer";
import { SideModal, SideModalProvider } from "../context/SideModal";
import { TopModal, TopModalProvider } from "../context/TopModal";
import { SearchProvider } from "../context/SearchContext";

export default function Layout() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <ModalProvider>
        <SideModalProvider>
          <TopModalProvider>
            <ShoppingCartProvider>
              <SearchProvider>
                <Navigation />
                <TopModal />
                <SideModal />
                {isLoaded && <Outlet />}
                <Modal />
                <Footer />
              </SearchProvider>
            </ShoppingCartProvider>
          </TopModalProvider>
        </SideModalProvider>
      </ModalProvider>
    </>
  );
}
