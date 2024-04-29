import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';
import RestaurantCard from './RestaurantCard';

export function RestaurantCarousel({restaurants, user, avgRating, priceArr, timeArr}) {
    // console.log(restaurants)
    const responsive = {
        desktop: {
            breakpoint: { max: 3500, min: 1024 },
            items: 4,
            slidesToSlide: 3 // optional, default to 1.
        },
        tablet: {
            breakpoint: { max: 1024, min: 464 },
            items: 4,
            slidesToSlide: 3 // optional, default to 1.
        },
    }
    return (
        <>
        <Carousel responsive={responsive} containerClass='restaurant-carousel' itemClass='restaurant-item'>
            {restaurants.map((restaurant, idx) => <RestaurantCard key={idx}restaurant={restaurant} idx={idx} user={user} avgRating={avgRating} priceArr={priceArr} timeArr={timeArr} />
            )}
        </Carousel>
        </>
      )
}
