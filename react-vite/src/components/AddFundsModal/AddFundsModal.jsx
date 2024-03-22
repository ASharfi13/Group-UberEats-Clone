import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { increaseFunds } from "../../redux/walletReducer";
import "./AddFundsModal.css"
function AddFundsModal() {
    const dispatch = useDispatch()
    const [funds, setFunds] = useState(0)
    const { closeModal } = useModal()
    const user = useSelector((store) => store.session.user)
    const wallets = useSelector((store) => store.walletState)
    const currentBalance = wallets ? wallets[user?.id] : null

    const handleSubmit = async (e) => {
        e.preventDefault();

        const addingFunds = await dispatch(increaseFunds(funds, user?.id))
        closeModal()
    }

    return (
        <div className="add-funds-modal">
            <h1 className="add-funds-logo">Add Funds</h1>
            <h2 className="current-funds">Balance: $ {currentBalance?.toFixed(2)}</h2>
            <form className="add-funds-form" onSubmit={handleSubmit}>
                <label className="funds-area">
                    Amount:
                    <input type="number" min={0} max={500} value={funds} onChange={(e) => setFunds(e.target.value)}/>
                </label>
                <button>Submit</button>
            </form>
        </div>
    )
}

export default AddFundsModal
