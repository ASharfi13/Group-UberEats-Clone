import React from 'react';
import { GoogleMap, useJsApiLoader } from '@react-google-maps/api';

const containerStyle = {
    width: '800px',
    height: '400px',
};

const center = {
    lat: 40.782555,
    lng: -73.965583
};

function Maps({ apiKey }) {
    const { isLoaded } = useJsApiLoader({
        id: 'google-map-script',
        googleMapsApiKey: apiKey,
    });

    return (
        <>
        {isLoaded && (
            <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={10}
            />
        )}
        </>
        );
    };

export default React.memo(Maps);
