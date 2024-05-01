import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';

export function FilterCarousel({restaurantTypes, filter, setSearchParams}) {
    // console.log(restaurantTypes)
    const responsive = {
        desktop: {
            breakpoint: { max: 3500, min: 1024 },
            items: 13,
            slidesToSlide: 12 // optional, default to 1.
        },
        tablet: {
            breakpoint: { max: 1024, min: 464 },
            items: 10,
            slidesToSlide: 9 // optional, default to 1.
        },
    }
    return (
        <Carousel responsive={responsive} containerClass='filter-carousel' itemClass='filter-item'>
            {restaurantTypes.map((type) => (
            <div key={type.id} className={`filterButton ${filter == type.name && "selected"}`} onClick={() => {
              if (filter == type.name) setSearchParams('')
              else setSearchParams(`type=${type.name}`)
            }}>
              <img src={type.imageUrl} alt={type.name} width="64px" height="64px" />
              <div>{type.name}</div>
            </div>
          ))}
        </Carousel>
      )
}