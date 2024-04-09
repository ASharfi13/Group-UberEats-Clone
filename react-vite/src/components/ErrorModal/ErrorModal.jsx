// import { useEffect, useState } from "react";
// import { useSelector, useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./ErrorModal.css"

function ErrorModal({message, cbFunction}) {
    // const dispatch = useDispatch()
    const { closeModal } = useModal()

    const handleSubmit = async (e) => {
        e.preventDefault();
        cbFunction();
        closeModal()
    }

    return (
        <div className="error-modal-container">
            {/* <h1>ERROR</h1> */}
            <h2 className="error-modal-message">{message}</h2>
            <button className="exit-modal-button" onClick={handleSubmit}>Ok</button>
        </div>
    )
}

export default ErrorModal
