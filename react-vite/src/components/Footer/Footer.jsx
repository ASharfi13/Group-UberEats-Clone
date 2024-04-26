import { FaGithub, FaLinkedin } from "react-icons/fa"
import "./Footer.css"
import { Link } from "react-router-dom"

function Footer() {
    return (
        <div className="footer">
            <div>Ahmed<Link to="https://github.com/ASharfi13" target="_blank" ><FaGithub /></Link><Link to="https://www.linkedin.com/in/ahmedsharfi/" target="_blank"><FaLinkedin /></Link></div>
            <div>Joel<Link to="https://github.com/Jabitzen" target="_blank" ><FaGithub /></Link><Link to="" target="_blank"><FaLinkedin /></Link></div>
            <div>Khobe<Link to="https://github.com/khobearzadon24" target="_blank" ><FaGithub /></Link><Link to="https://www.linkedin.com/in/khobe-arzadon-4b985a202/" target="_blank"><FaLinkedin /></Link></div>
            <div>Royce<Link to="https://github.com/jiangroyce" target="_blank" ><FaGithub /></Link><Link to="https://www.linkedin.com/in/jiangroyce/" target="_blank"><FaLinkedin /></Link></div>
        </div>
    )
}

export default Footer
