import {useMapsLibrary, APIProvider, Map} from '@vis.gl/react-google-maps';

export default function UserAddress() {
    const geocoderLibrary = useMapsLibrary('geocoding');

    console.log(geocoderLibrary)

    const request = geocoderLibrary?.Geocoder

    console.log(request)

    return (
        <APIProvider apiKey="AIzaSyBgx4z6ZvY6IYmCpMA-JxSgrLuY39y1PAk">
            <Map
                style={{width: '100vw', height: '100vh'}}
                defaultCenter={{
                    lat: 40.782555,
                    lng: -73.965583
                }}
                defaultZoom={13}
                gestureHandling={'greedy'}
                disableDefaultUI={true}
            />
        </APIProvider>
    )
}
