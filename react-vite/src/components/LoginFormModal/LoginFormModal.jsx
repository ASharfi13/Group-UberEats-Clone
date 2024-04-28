import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import * as sessionActions from "../../redux/session";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse.errors);
    } else {
      closeModal();
    }
  };

  const handleDemo = (e) => {
    e.preventDefault();
    setErrors({});
    const demoUser = {};
    demoUser.email = "jwhite@gmail.com";
    demoUser.password = "jwpassword12";
    return dispatch(sessionActions.thunkLogin(demoUser))
      .then(closeModal)
      .catch(async (res) => {
        const data = await res.json();
        if (data && data.errors) {
          setErrors(data.errors);
        }
      });
  };

  return (
    <div className="log-in-modal">
      <h1 className="log-in-logo">Log In</h1>
      <form className="log-in-form" onSubmit={handleSubmit}>
        <label className="email-area">
          Email:
          <input
            className="loginTextInput"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p className="login-errors">{errors.email}</p>}
        <label className="passtime">
          Password:
          <input
            className="loginTextInput"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p className="login-errors">{errors.password}</p>}
        <button className="modalButton" type="submit">Log In</button>
      </form>
      <button className="demo-user" onClick={handleDemo}>
        Demo User
      </button>
    </div>
  );
}

export default LoginFormModal;
