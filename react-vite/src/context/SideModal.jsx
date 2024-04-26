import { useRef, useState, useContext, createContext } from 'react';
import ReactDOM from 'react-dom';
import './SideModal.css';

const ModalContext = createContext();

export function SideModalProvider({ children }) {
  const modalRef = useRef();
  const [modalContent, setModalContent] = useState(null);
  const [modalSide, setModalSide] = useState("left")
  // callback function that will be called when modal is closing
  const [onModalClose, setOnModalClose] = useState(null);

  const closeModal = () => {
    setModalContent(null); // clear the modal contents
    // If callback function is truthy, call the callback function and reset it
    // to null:
    if (typeof onModalClose === 'function') {
      setOnModalClose(null);
      onModalClose();
    }
  };

  const contextValue = {
    modalRef, // reference to modal div
    modalContent, // React component to render inside modal
    setModalContent, // function to set the React component to render inside modal
    setOnModalClose, // function to set the callback function called when modal is closing
    closeModal, // function to close the modal
    modalSide, // side of modal
    setModalSide // function to set modal side
  };

  return (
    <>
      <ModalContext.Provider value={contextValue}>
        {children}
      </ModalContext.Provider>
      <div ref={modalRef} />
    </>
  );
}

export function SideModal() {
  const { modalSide, modalRef, modalContent, closeModal } = useContext(ModalContext);
  // If there is no div referenced by the modalRef or modalContent is not a
  // truthy value, render nothing:
  if (!modalRef || !modalRef.current || !modalContent) return null;

  // Render the following component to the div referenced by the modalRef
  return ReactDOM.createPortal(
    <div id="side-modal">
      <div id="modal-background" onClick={closeModal} />
      <div id="side-modal-content" className={modalSide}>
        {modalContent}
      </div>
    </div>,
    modalRef.current
  );
}

export const useSideModal = () => useContext(ModalContext);
