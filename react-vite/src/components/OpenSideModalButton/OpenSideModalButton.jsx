import { useSideModal } from '../../context/SideModal';
import { useTopModal } from '../../context/TopModal';

function OpenModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed
  modalSide,
  className
}) {
  const { setModalContent, setOnModalClose, setModalSide } = useSideModal();
  const closeTopModal = useTopModal().closeModal

  const onClick = () => {
    closeTopModal();
    setModalSide(modalSide);
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (typeof onButtonClick === "function") onButtonClick();
  };

  return <button onClick={onClick} className={className}>{buttonText}</button>;
}

export default OpenModalButton;
