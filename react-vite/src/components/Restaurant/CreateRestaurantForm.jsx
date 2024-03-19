import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"


function RestaurantForm() {
    const [name, setName] = useState("")
    const [location, setLocation] = useState("")
    const [type, setType] = useState("")
    const [image, setImage] = useState("")
    const [errors, setErrors] = useState({})
    const [showErrors, setShowErrors] = useState(false)

    const restaurantTypes = ["American", "Chinese", "Indian", "Mexican", "Korean", "Thai", "Other"]

    const errObj = {}

    // useEffect(() => {
    //     const errObj = {}

    //     if (name.length < 3) {
    //         errObj["nameLength"] = "Name must be at least 3 Characters"
    //     }

    //     if (location.length == 0) {
    //         errObj["locationMissing"] = "Location is required"
    //     }

    //     if (image.length == 0) {
    //         errObj["imageMissing"] = "Image is required"
    //     }

    //     setErrors(errObj)
    // }, [name, location, image])

    const onSubmit = async (e) => {
        e.preventDefault()

        if(Object.values(errObj).length === 0) {
            alert("Successful")
        } else {
            setErrors("")
        }
    }

    return (
        <div>
            <form>
                <h1>Create A New Restaurant</h1>
                <div>
                    <input
                        type="text"
                        placeholder="Enter A Name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    >
                    </input>
                    <p className="errors">{errors.name ? errors.name: null}</p>
                </div>

                <div>
                    <input
                        type="text"
                        placeholder="Enter A Location"
                        value={location}
                        onChange={(e) => setLocation(e.target.value)}
                        required
                    >
                    </input>
                    <p className="errors">{errors.location ? errors.location: null}</p>
                </div>
                <div>
                    <select
                        value={type}
                        onChange={(e) => setType(e.target.value)}
                    >
                        <option value={""} disabled selected>Select Type</option>
                        {restaurantTypes.map((restaurant) => (
                            <option>{restaurant}</option>
                        ))}
                    </select>
                    <p className="errors">{errors.name ? errors.name: null}</p>

                </div>
                <div>
                    <input
                        type="url"
                        placeholder="Enter Image Url"
                        value={image}
                        onChange={(e) => setImage(e.target.value)}
                    >
                    </input>
                    <p className="errors">{errors.name ? errors.name: null}</p>

                </div>
            </form>
        </div>
    )
}

export default RestaurantForm
