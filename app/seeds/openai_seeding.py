from openai import OpenAI
client = OpenAI()

restaurants = [{
        "name": "Saffron Lounge",
        "location": "100 Spice Blvd",
        "owner_id": 1,
        "imageUrl": "http://aa-uber-eats-project.s3.amazonaws.com/f3aeb9c5c7994471b99366b44ea6034a.png"
    },
    {
        "name": "Bamboo Garden",
        "location": "25 Panda Way",
        "owner_id": 2,
        "imageUrl": 'http://aa-uber-eats-project.s3.amazonaws.com/359cfbdcb106441ab687a0d4c946bf6d.png'
    },
    {
        "name": "The Burger Joint",
        "location": "88 Greasy Spoon St",
        "owner_id": 3,
        "imageUrl": "https://example.com/burgerjoint.jpg"
    },
    {
        "name": "Taco Oasis",
        "location": "55 Fiesta Rd",
        "owner_id": 4,
        "imageUrl": "https://example.com/tacooasis.jpg"
    },
    {
        "name": "Curry Corner",
        "location": "15 Masala Ln",
        "owner_id": 5,
        "imageUrl": "https://example.com/currycorner.jpg"
    },
    {
        "name": "Noodle Nest",
        "location": "3 Chopstick Cir",
        "owner_id": 6,
        "imageUrl": "https://example.com/noodlenest.jpg"
    },
    {
        "name": "Steakhouse Supreme",
        "location": "77 Tender Cut Ave",
        "owner_id": 7,
        "imageUrl": "https://example.com/steakhousesupreme.jpg"
    },
    {
        "name": "Oceanic Delights",
        "location": "22 Coral Reef Rd",
        "owner_id": 8,
        "imageUrl": "https://example.com/oceanicdelights.jpg"
    },
    {
        "name": "Le Petit Chef",
        "location": "5 French Cuisine Blvd",
        "owner_id": 9,
        "imageUrl": "https://example.com/lepetitchef.jpg"
    },
    {
        "name": "Pizza Palace",
        "location": "88 Pie Ln",
        "owner_id": 10,
        "imageUrl": "https://example.com/pizzapalace.jpg"
    },
    {
        "name": "Dumpling Den",
        "location": "2 Dumpling Dr",
        "owner_id": 11,
        "imageUrl": "https://example.com/dumplingden.jpg"
    },
    {
        "name": "BBQ Barn",
        "location": "55 Smoky Trail",
        "owner_id": 12,
        "imageUrl": "https://example.com/bbqbarn.jpg"
    },
    {
        "name": "Gelato Galore",
        "location": "14 Sweet St",
        "owner_id": 13,
        "imageUrl": "https://example.com/gelatogalore.jpg"
    },
    {
        "name": "The Vegan Bistro",
        "location": "25 Green Garden Rd",
        "owner_id": 14,
        "imageUrl": "https://example.com/veganbistro.jpg"
    },
    {
        "name": "Sushi Spot",
        "location": "18 Sashimi Blvd",
        "owner_id": 15,
        "imageUrl": "https://example.com/sushispot.jpg"
    },
    {
        "name": "Pastry Paradise",
        "location": "30 Confectioner's Row",
        "owner_id": 16,
        "imageUrl": "https://example.com/pastryparadise.jpg"
    },
    {
        "name": "Kebab Kingdom",
        "location": "90 Skewer St",
        "owner_id": 17,
        "imageUrl": "https://example.com/kebabkingdom.jpg"
    },
    {
        "name": "Bistro Bella",
        "location": "1 Lovely Ln",
        "owner_id": 18,
        "imageUrl": "https://example.com/bistrobella.jpg"
    },
    {
        "name": "Momo Mountain",
        "location": "44 Himalaya Hts",
        "owner_id": 19,
        "imageUrl": "https://example.com/momomountain.jpg"
    },
    {
        "name": "Pasta Pavilion",
        "location": "66 Noodle Blvd",
        "owner_id": 20,
        "imageUrl": "https://example.com/pastapavilion.jpg"
    },
    {
        "name": "The Breakfast Club",
        "location": "33 Morning Ave",
        "owner_id": 21,
        "imageUrl": "https://example.com/breakfastclub.jpg"
    },
    {
        "name": "Salad Sanctuary",
        "location": "40 Health Hwy",
        "owner_id": 22,
        "imageUrl": "https://example.com/saladsanctuary.jpg"
    },
    {
        "name": "Empanada Empire",
        "location": "12 Dough Dr",
        "owner_id": 23,
        "imageUrl": "https://example.com/empanadaempire.jpg"
    },
    {
        "name": "Coffee Cottage",
        "location": "28 Bean Blvd",
        "owner_id": 24,
        "imageUrl": "https://example.com/coffeecottage.jpg"
    },
    {
        "name": "Ramen Retreat",
        "location": "72 Broth Ln",
        "owner_id": 25,
        "imageUrl": "https://example.com/ramenretreat.jpg"
    },
    {
        "name": "Tiramisu Tower",
        "location": "60 Dessert Dr",
        "owner_id": 26,
        "imageUrl": "https://example.com/tiramisutower.jpg"
    },
    {
        "name": "Cheese Chalet",
        "location": "34 Fondue Fwy",
        "owner_id": 27,
        "imageUrl": "https://example.com/cheesechalet.jpg"
    },
    {
        "name": "Falafel Fortress",
        "location": "11 Pita Pl",
        "owner_id": 28,
        "imageUrl": "https://example.com/falafelfortress.jpg"
    },
    {
        "name": "Gumbo Grove",
        "location": "53 Bayou Blvd",
        "owner_id": 29,
        "imageUrl": "https://example.com/gumbogrove.jpg"
    },
    {
        "name": "Pie Palace",
        "location": "21 Baker St",
        "owner_id": 30,
        "imageUrl": "https://example.com/piepalace.jpg"
    }]

menu_items = [{"name": "Chicken Tikka Masala", "type": "Chicken", "price": 12.99, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Chicken-Tikka-Masala.jpg"},
            {"name": "Saag Paneer", "type": "Vegetarian", "price": 10.99, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Saag-Paneer.jpg"},
            {"name": "Lamb Vindaloo", "type": "Lamb", "price": 14.99, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Lamb-Vindaloo.jpg"},
            {"name": "Butter Chicken", "type": "Chicken", "price": 13.99, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Butter-Chicken.jpg"},
            {"name": "Chana Masala", "type": "Vegetarian", "price": 9.99, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Chana-Masala.jpg"},
            {"name": "Naan Bread", "type": "Bread", "price": 2.99, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Naan-Bread.jpg"},
            {"name": "Palak Paneer", "type": "Vegetarian", "price": 10.49, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Palak-Paneer.jpg"},
            {"name": "Tandoori Chicken", "type": "Chicken", "price": 11.99, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Tandoori-Chicken.jpg"},
            {"name": "Biryani", "type": "Rice", "price": 11.49, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Biryani.jpg"},
            {"name": "Gulab Jamun", "type": "Dessert", "price": 4.99, "restaurant_id": 19, "imageUrl": "https://i.postimg.cc/Gulab-Jamun.jpg"},
            {"name": "Kung Pao Chicken", "type": "Chicken", "price": 8.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Kung-Pao-Chicken.jpg"},
            {"name": "Beef and Broccoli", "type": "Beef", "price": 9.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Beef-and-Broccoli.jpg"},
            {"name": "Sweet and Sour Pork", "type": "Pork", "price": 8.49, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Sweet-and-Sour-Pork.jpg"},
            {"name": "Spring Rolls", "type": "Appetizer", "price": 5.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Spring-Rolls.jpg"},
            {"name": "Egg Fried Rice", "type": "Rice", "price": 7.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Egg-Fried-Rice.jpg"},
            {"name": "Mapo Tofu", "type": "Vegetarian", "price": 10.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Mapo-Tofu.jpg"},
            {"name": "Peking Duck", "type": "Duck", "price": 25.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Peking-Duck.jpg"},
            {"name": "Hot Pot", "type": "Mixed", "price": 15.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Hot-Pot.jpg"},
            {"name": "Dim Sum", "type": "Dumplings", "price": 12.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Dim-Sum.jpg"},
            {"name": "Mango Pudding", "type": "Dessert", "price": 6.99, "restaurant_id": 20, "imageUrl": "https://i.postimg.cc/Mango-Pudding.jpg"},
            {"name": "Classic Cheeseburger", "type": "Burger", "price": 7.99, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/Classic-Cheeseburger.jpg"},
            {"name": "Bacon Burger", "type": "Burger", "price": 8.99, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/Bacon-Burger.jpg"},
            {"name": "Veggie Burger", "type": "Vegetarian", "price": 6.99, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/Veggie-Burger.jpg"},
            {"name": "Smokehouse BBQ Burger", "type": "Burger", "price": 9.99, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/Smokehouse-BBQ-Burger.jpg"},
            {"name": "Mushroom Swiss Burger", "type": "Burger", "price": 8.49, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/Mushroom-Swiss-Burger.jpg"},
            {"name": "Jalapeno Popper Burger", "type": "Burger", "price": 8.99, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/Jalapeno-Popper-Burger.jpg"},
            {"name": "Turkey Burger", "type": "Turkey", "price": 8.49, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/Turkey-Burger.jpg"},
            {"name": "Black Bean Burger", "type": "Vegetarian", "price": 7.49, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/Black-Bean-Burger.jpg"},
            {"name": "The Double Stacker", "type": "Burger", "price": 10.99, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/The-Double-Stacker.jpg"},
            {"name": "The All-American", "type": "Burger", "price": 7.99, "restaurant_id": 21, "imageUrl": "https://i.postimg.cc/The-All-American.jpg"},
            {"name": "Carne Asada Tacos", "type": "Beef", "price": 3.99, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Carne-Asada-Tacos.jpg"},
            {"name": "Chicken Fajitas", "type": "Chicken", "price": 8.99, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Chicken-Fajitas.jpg"},
            {"name": "Shrimp Tacos", "type": "Seafood", "price": 4.49, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Shrimp-Tacos.jpg"},
            {"name": "Chorizo Quesadilla", "type": "Pork", "price": 7.49, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Chorizo-Quesadilla.jpg"},
            {"name": "Vegetarian Burrito", "type": "Vegetarian", "price": 6.99, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Vegetarian-Burrito.jpg"},
            {"name": "Fish Tacos", "type": "Fish", "price": 4.99, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Fish-Tacos.jpg"},
            {"name": "Al Pastor Tacos", "type": "Pork", "price": 3.49, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Al-Pastor-Tacos.jpg"},
            {"name": "Carnitas Tacos", "type": "Pork", "price": 3.99, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Carnitas-Tacos.jpg"},
            {"name": "Barbacoa Tacos", "type": "Beef", "price": 4.49, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Barbacoa-Tacos.jpg"},
            {"name": "Guacamole & Chips", "type": "Appetizer", "price": 5.99, "restaurant_id": 22, "imageUrl": "https://i.postimg.cc/Guacamole-Chips.jpg"},
            {"name": "Lamb Rogan Josh", "type": "Lamb", "price": 15.99, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Lamb-Rogan-Josh.jpg"},
            {"name": "Paneer Tikka", "type": "Vegetarian", "price": 12.99, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Paneer-Tikka.jpg"},
            {"name": "Chicken Korma", "type": "Chicken", "price": 13.99, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Chicken-Korma.jpg"},
            {"name": "Dal Tadka", "type": "Vegetarian", "price": 9.99, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Dal-Tadka.jpg"},
            {"name": "Aloo Gobi", "type": "Vegetarian", "price": 10.49, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Aloo-Gobi.jpg"},
            {"name": "Prawn Masala", "type": "Seafood", "price": 14.99, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Prawn-Masala.jpg"},
            {"name": "Mutter Paneer", "type": "Vegetarian", "price": 11.49, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Mutter-Paneer.jpg"},
            {"name": "Lamb Biryani", "type": "Lamb", "price": 16.99, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Lamb-Biryani.jpg"},
            {"name": "Samosas", "type": "Appetizer", "price": 5.49, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Samosas.jpg"},
            {"name": "Mango Lassi", "type": "Beverage", "price": 4.99, "restaurant_id": 23, "imageUrl": "https://i.postimg.cc/Mango-Lassi.jpg"},
            {"name": "Pho Bo", "type": "Beef", "price": 12.99, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Pho-Bo.jpg"},
            {"name": "Pad Thai", "type": "Noodles", "price": 11.99, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Pad-Thai.jpg"},
            {"name": "Dan Dan Noodles", "type": "Noodles", "price": 10.49, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Dan-Dan-Noodles.jpg"},
            {"name": "Laksa", "type": "Seafood", "price": 13.99, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Laksa.jpg"},
            {"name": "Udon", "type": "Noodles", "price": 9.99, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Udon.jpg"},
            {"name": "Singapore Noodles", "type": "Noodles", "price": 11.49, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Singapore-Noodles.jpg"},
            {"name": "Ramen", "type": "Noodles", "price": 12.99, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Ramen.jpg"},
            {"name": "Bibim Guksu", "type": "Noodles", "price": 10.99, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Bibim-Guksu.jpg"},
            {"name": "Char Kway Teow", "type": "Noodles", "price": 11.49, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Char-Kway-Teow.jpg"},
            {"name": "Soba", "type": "Noodles", "price": 10.99, "restaurant_id": 24, "imageUrl": "https://i.postimg.cc/Soba.jpg"},
            {"name": "Ribeye Steak", "type": "Beef", "price": 25.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/Ribeye-Steak.jpg"},
            {"name": "Filet Mignon", "type": "Beef", "price": 29.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/Filet-Mignon.jpg"},
            {"name": "New York Strip", "type": "Beef", "price": 27.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/New-York-Strip.jpg"},
            {"name": "Porterhouse Steak", "type": "Beef", "price": 30.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/Porterhouse-Steak.jpg"},
            {"name": "T-Bone Steak", "type": "Beef", "price": 26.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/T-Bone-Steak.jpg"},
            {"name": "Surf and Turf", "type": "Mixed", "price": 34.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/Surf-and-Turf.jpg"},
            {"name": "Grilled Salmon", "type": "Fish", "price": 19.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/Grilled-Salmon.jpg"},
            {"name": "Caesar Salad", "type": "Salad", "price": 9.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/Caesar-Salad.jpg"},
            {"name": "Lobster Bisque", "type": "Soup", "price": 12.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/Lobster-Bisque.jpg"},
            {"name": "Garlic Bread", "type": "Appetizer", "price": 5.99, "restaurant_id": 25, "imageUrl": "https://i.postimg.cc/Garlic-Bread.jpg"},
            {"name": "Lobster Roll", "type": "Seafood", "price": 17.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Lobster-Roll.jpg"},
            {"name": "Grilled Sea Bass", "type": "Fish", "price": 22.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Grilled-Sea-Bass.jpg"},
            {"name": "Crab Cakes", "type": "Seafood", "price": 15.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Crab-Cakes.jpg"},
            {"name": "Oysters Rockefeller", "type": "Seafood", "price": 14.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Oysters-Rockefeller.jpg"},
            {"name": "Shrimp Cocktail", "type": "Seafood", "price": 12.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Shrimp-Cocktail.jpg"},
            {"name": "Seared Scallops", "type": "Seafood", "price": 19.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Seared-Scallops.jpg"},
            {"name": "Clam Chowder", "type": "Soup", "price": 10.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Clam-Chowder.jpg"},
            {"name": "Fried Calamari", "type": "Seafood", "price": 13.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Fried-Calamari.jpg"},
            {"name": "Seafood Paella", "type": "Mixed", "price": 24.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Seafood-Paella.jpg"},
            {"name": "Fish Tacos", "type": "Fish", "price": 14.99, "restaurant_id": 26, "imageUrl": "https://i.postimg.cc/Fish-Tacos.jpg"},
            {"name": "Coq au Vin", "type": "Chicken", "price": 19.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Coq-au-Vin.jpg"},
            {"name": "Bouillabaisse", "type": "Seafood", "price": 25.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Bouillabaisse.jpg"},
            {"name": "Ratatouille", "type": "Vegetarian", "price": 16.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Ratatouille.jpg"},
            {"name": "Duck Confit", "type": "Duck", "price": 22.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Duck-Confit.jpg"},
            {"name": "Beef Bourguignon", "type": "Beef", "price": 23.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Beef-Bourguignon.jpg"},
            {"name": "Quiche Lorraine", "type": "Egg", "price": 12.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Quiche-Lorraine.jpg"},
            {"name": "Tarte Tatin", "type": "Dessert", "price": 10.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Tarte-Tatin.jpg"},
            {"name": "Escargot", "type": "Appetizer", "price": 13.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Escargot.jpg"},
            {"name": "Croque Monsieur", "type": "Sandwich", "price": 14.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Croque-Monsieur.jpg"},
            {"name": "Nicoise Salad", "type": "Salad", "price": 15.99, "restaurant_id": 27, "imageUrl": "https://i.postimg.cc/Nicoise-Salad.jpg"},
            {"name": "Margherita Pizza", "type": "Pizza", "price": 12.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/Margherita-Pizza.jpg"},
            {"name": "Pepperoni Pizza", "type": "Pizza", "price": 13.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/Pepperoni-Pizza.jpg"},
            {"name": "BBQ Chicken Pizza", "type": "Pizza", "price": 14.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/BBQ-Chicken-Pizza.jpg"},
            {"name": "Hawaiian Pizza", "type": "Pizza", "price": 13.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/Hawaiian-Pizza.jpg"},
            {"name": "Meat Lover's Pizza", "type": "Pizza", "price": 15.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/Meat-Lover-Pizza.jpg"},
            {"name": "Vegetarian Pizza", "type": "Pizza", "price": 12.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/Vegetarian-Pizza.jpg"},
            {"name": "Buffalo Chicken Pizza", "type": "Pizza", "price": 14.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/Buffalo-Chicken-Pizza.jpg"},
            {"name": "White Pizza", "type": "Pizza", "price": 13.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/White-Pizza.jpg"},
            {"name": "Pesto Pizza", "type": "Pizza", "price": 14.49, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/Pesto-Pizza.jpg"},
            {"name": "Four Cheese Pizza", "type": "Pizza", "price": 14.99, "restaurant_id": 28, "imageUrl": "https://i.postimg.cc/Four-Cheese-Pizza.jpg"},
            {"name": "Pork Dumplings", "type": "Pork", "price": 8.99, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Pork-Dumplings.jpg"},
            {"name": "Chicken Dumplings", "type": "Chicken", "price": 8.99, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Chicken-Dumplings.jpg"},
            {"name": "Vegetable Dumplings", "type": "Vegetarian", "price": 8.49, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Vegetable-Dumplings.jpg"},
            {"name": "Shrimp Dumplings", "type": "Seafood", "price": 9.99, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Shrimp-Dumplings.jpg"},
            {"name": "Beef Dumplings", "type": "Beef", "price": 9.49, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Beef-Dumplings.jpg"},
            {"name": "Kimchi Dumplings", "type": "Spicy", "price": 8.99, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Kimchi-Dumplings.jpg"},
            {"name": "Steamed Buns", "type": "Appetizer", "price": 7.99, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Steamed-Buns.jpg"},
            {"name": "Potstickers", "type": "Appetizer", "price": 8.99, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Potstickers.jpg"},
            {"name": "Xiao Long Bao", "type": "Pork", "price": 10.99, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Xiao-Long-Bao.jpg"},
            {"name": "Szechuan Dumplings", "type": "Spicy", "price": 9.99, "restaurant_id": 29, "imageUrl": "https://i.postimg.cc/Szechuan-Dumplings.jpg"},
            {"name": "Smoked Brisket", "type": "Beef", "price": 16.99, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/Smoked-Brisket.jpg"},
            {"name": "Pulled Pork Sandwich", "type": "Pork", "price": 12.99, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/Pulled-Pork-Sandwich.jpg"},
            {"name": "BBQ Ribs", "type": "Pork", "price": 15.99, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/BBQ-Ribs.jpg"},
            {"name": "Grilled Chicken", "type": "Chicken", "price": 14.49, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/Grilled-Chicken.jpg"},
            {"name": "Beef Ribs", "type": "Beef", "price": 18.99, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/Beef-Ribs.jpg"},
            {"name": "Smoked Turkey", "type": "Turkey", "price": 13.99, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/Smoked-Turkey.jpg"},
            {"name": "Cole Slaw", "type": "Side", "price": 3.99, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/Cole-Slaw.jpg"},
            {"name": "Mac & Cheese", "type": "Side", "price": 4.99, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/Mac-Cheese.jpg"},
            {"name": "Cornbread", "type": "Side", "price": 2.99, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/Cornbread.jpg"},
            {"name": "BBQ Beans", "type": "Side", "price": 3.49, "restaurant_id": 30, "imageUrl": "https://i.postimg.cc/BBQ-Beans.jpg"},
            {"name": "Stracciatella Gelato", "type": "Dessert", "price": 6.99, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Stracciatella-Gelato.jpg"},
            {"name": "Pistachio Gelato", "type": "Dessert", "price": 7.49, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Pistachio-Gelato.jpg"},
            {"name": "Lemon Sorbet", "type": "Dessert", "price": 6.49, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Lemon-Sorbet.jpg"},
            {"name": "Mango Gelato", "type": "Dessert", "price": 6.99, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Mango-Gelato.jpg"},
            {"name": "Coffee Gelato", "type": "Dessert", "price": 7.99, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Coffee-Gelato.jpg"},
            {"name": "Chocolate Gelato", "type": "Dessert", "price": 7.49, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Chocolate-Gelato.jpg"},
            {"name": "Raspberry Sorbet", "type": "Dessert", "price": 6.99, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Raspberry-Sorbet.jpg"},
            {"name": "Tiramisu Gelato", "type": "Dessert", "price": 8.49, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Tiramisu-Gelato.jpg"},
            {"name": "Hazelnut Gelato", "type": "Dessert", "price": 7.99, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Hazelnut-Gelato.jpg"},
            {"name": "Vanilla Bean Gelato", "type": "Dessert", "price": 6.99, "restaurant_id": 31, "imageUrl": "https://i.postimg.cc/Vanilla-Bean-Gelato.jpg"},
            {"name": "Vegan Burger", "type": "Vegetarian", "price": 9.99, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Vegan-Burger.jpg"},
            {"name": "Tofu Scramble", "type": "Vegetarian", "price": 8.99, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Tofu-Scramble.jpg"},
            {"name": "Seitan Steak", "type": "Vegetarian", "price": 11.99, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Seitan-Steak.jpg"},
            {"name": "Vegan Caesar Salad", "type": "Salad", "price": 10.49, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Vegan-Caesar-Salad.jpg"},
            {"name": "Vegan Lasagna", "type": "Vegetarian", "price": 12.99, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Vegan-Lasagna.jpg"},
            {"name": "Vegan Pizza", "type": "Pizza", "price": 13.49, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Vegan-Pizza.jpg"},
            {"name": "Vegan Sushi", "type": "Vegetarian", "price": 9.99, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Vegan-Sushi.jpg"},
            {"name": "Chickpea Curry", "type": "Vegetarian", "price": 8.49, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Chickpea-Curry.jpg"},
            {"name": "Vegetable Stir Fry", "type": "Vegetarian", "price": 10.99, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Vegetable-Stir-Fry.jpg"},
            {"name": "Vegan Chocolate Cake", "type": "Dessert", "price": 7.99, "restaurant_id": 32, "imageUrl": "https://i.postimg.cc/Vegan-Chocolate-Cake.jpg"},
            {"name": "California Roll", "type": "Sushi", "price": 6.99, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/California-Roll.jpg"},
            {"name": "Salmon Nigiri", "type": "Sushi", "price": 7.49, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Salmon-Nigiri.jpg"},
            {"name": "Tuna Sashimi", "type": "Sushi", "price": 8.99, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Tuna-Sashimi.jpg"},
            {"name": "Dragon Roll", "type": "Sushi", "price": 12.99, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Dragon-Roll.jpg"},
            {"name": "Rainbow Roll", "type": "Sushi", "price": 13.49, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Rainbow-Roll.jpg"},
            {"name": "Spicy Tuna Roll", "type": "Sushi", "price": 7.99, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Spicy-Tuna-Roll.jpg"},
            {"name": "Eel Avocado Roll", "type": "Sushi", "price": 9.49, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Eel-Avocado-Roll.jpg"},
            {"name": "Miso Soup", "type": "Soup", "price": 2.99, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Miso-Soup.jpg"},
            {"name": "Tempura Shrimp", "type": "Appetizer", "price": 9.99, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Tempura-Shrimp.jpg"},
            {"name": "Edamame", "type": "Appetizer", "price": 4.99, "restaurant_id": 33, "imageUrl": "https://i.postimg.cc/Edamame.jpg"},
            {"name": "Croissant", "type": "Pastry", "price": 2.99, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Croissant.jpg"},
            {"name": "Cinnamon Roll", "type": "Pastry", "price": 3.49, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Cinnamon-Roll.jpg"},
            {"name": "Macarons", "type": "Pastry", "price": 4.99, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Macarons.jpg"},
            {"name": "Apple Pie", "type": "Dessert", "price": 5.49, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Apple-Pie.jpg"},
            {"name": "Chocolate Eclair", "type": "Pastry", "price": 4.49, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Chocolate-Eclair.jpg"},
            {"name": "Tiramisu", "type": "Dessert", "price": 6.99, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Tiramisu.jpg"},
            {"name": "Cheesecake", "type": "Dessert", "price": 6.49, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Cheesecake.jpg"},
            {"name": "Fruit Tart", "type": "Dessert", "price": 5.99, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Fruit-Tart.jpg"},
            {"name": "Pain au Chocolat", "type": "Pastry", "price": 3.99, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Pain-au-Chocolat.jpg"},
            {"name": "Danish Pastry", "type": "Pastry", "price": 4.49, "restaurant_id": 34, "imageUrl": "https://i.postimg.cc/Danish-Pastry.jpg"},
            {"name": "Doner Kebab", "type": "Kebab", "price": 7.99, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Doner-Kebab.jpg"},
            {"name": "Chicken Shish Kebab", "type": "Kebab", "price": 8.49, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Chicken-Shish-Kebab.jpg"},
            {"name": "Lamb Shish Kebab", "type": "Kebab", "price": 9.99, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Lamb-Shish-Kebab.jpg"},
            {"name": "Mixed Grill Platter", "type": "Mixed", "price": 15.99, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Mixed-Grill-Platter.jpg"},
            {"name": "Falafel Wrap", "type": "Vegetarian", "price": 6.99, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Falafel-Wrap.jpg"},
            {"name": "Tabbouleh", "type": "Salad", "price": 5.49, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Tabbouleh.jpg"},
            {"name": "Baba Ganoush", "type": "Appetizer", "price": 5.99, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Baba-Ganoush.jpg"},
            {"name": "Hummus Plate", "type": "Appetizer", "price": 5.99, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Hummus-Plate.jpg"},
            {"name": "Beef Kofta", "type": "Kebab", "price": 8.99, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Beef-Kofta.jpg"},
            {"name": "Yogurt Kebab", "type": "Kebab", "price": 8.99, "restaurant_id": 35, "imageUrl": "https://i.postimg.cc/Yogurt-Kebab.jpg"},
            {"name": "Beef Carpaccio", "type": "Beef", "price": 14.99, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Beef-Carpaccio.jpg"},
            {"name": "Mushroom Risotto", "type": "Risotto", "price": 12.99, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Mushroom-Risotto.jpg"},
            {"name": "Caprese Salad", "type": "Salad", "price": 10.99, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Caprese-Salad.jpg"},
            {"name": "Bruschetta", "type": "Appetizer", "price": 8.49, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Bruschetta.jpg"},
            {"name": "Seafood Linguine", "type": "Pasta", "price": 15.99, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Seafood-Linguine.jpg"},
            {"name": "Chicken Piccata", "type": "Chicken", "price": 13.99, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Chicken-Piccata.jpg"},
            {"name": "Osso Bucco", "type": "Veal", "price": 22.99, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Osso-Bucco.jpg"},
            {"name": "Fettuccine Alfredo", "type": "Pasta", "price": 11.99, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Fettuccine-Alfredo.jpg"},
            {"name": "Tiramisu", "type": "Dessert", "price": 9.49, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Tiramisu.jpg"},
            {"name": "Limoncello Gelato", "type": "Dessert", "price": 6.99, "restaurant_id": 36, "imageUrl": "https://i.postimg.cc/Limoncello-Gelato.jpg"},
            {"name": "Chicken Momo", "type": "Dumplings", "price": 8.99, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Chicken-Momo.jpg"},
            {"name": "Beef Momo", "type": "Dumplings", "price": 9.49, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Beef-Momo.jpg"},
            {"name": "Vegetable Momo", "type": "Dumplings", "price": 8.49, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Vegetable-Momo.jpg"},
            {"name": "Buff Momo", "type": "Dumplings", "price": 9.99, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Buff-Momo.jpg"},
            {"name": "Paneer Momo", "type": "Dumplings", "price": 8.99, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Paneer-Momo.jpg"},
            {"name": "Momo Soup", "type": "Soup", "price": 7.99, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Momo-Soup.jpg"},
            {"name": "Fried Momo", "type": "Dumplings", "price": 8.99, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Fried-Momo.jpg"},
            {"name": "Jhol Momo", "type": "Dumplings", "price": 9.49, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Jhol-Momo.jpg"},
            {"name": "Chilli Momo", "type": "Spicy", "price": 10.49, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Chilli-Momo.jpg"},
            {"name": "Steamed Momo", "type": "Dumplings", "price": 8.49, "restaurant_id": 37, "imageUrl": "https://i.postimg.cc/Steamed-Momo.jpg"},
            {"name": "Spaghetti Carbonara", "type": "Pasta", "price": 12.99, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Spaghetti-Carbonara.jpg"},
            {"name": "Lasagna", "type": "Pasta", "price": 14.99, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Lasagna.jpg"},
            {"name": "Penne Arrabbiata", "type": "Pasta", "price": 11.99, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Penne-Arrabbiata.jpg"},
            {"name": "Fettuccine Alfredo", "type": "Pasta", "price": 12.49, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Fettuccine-Alfredo.jpg"},
            {"name": "Ravioli di Portobello", "type": "Pasta", "price": 13.99, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Ravioli-di-Portobello.jpg"},
            {"name": "Pesto Genovese", "type": "Pasta", "price": 12.99, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Pesto-Genovese.jpg"},
            {"name": "Gnocchi Pomodoro", "type": "Pasta", "price": 11.99, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Gnocchi-Pomodoro.jpg"},
            {"name": "Tagliatelle Bolognese", "type": "Pasta", "price": 14.49, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Tagliatelle-Bolognese.jpg"},
            {"name": "Seafood Linguine", "type": "Pasta", "price": 16.99, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Seafood-Linguine.jpg"},
            {"name": "Tortellini in Brodo", "type": "Pasta", "price": 13.49, "restaurant_id": 38, "imageUrl": "https://i.postimg.cc/Tortellini-in-Brodo.jpg"},
            {"name": "Pancakes with Maple Syrup", "type": "Breakfast", "price": 7.99, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Pancakes-with-Maple-Syrup.jpg"},
            {"name": "Eggs Benedict", "type": "Breakfast", "price": 9.99, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Eggs-Benedict.jpg"},
            {"name": "French Toast", "type": "Breakfast", "price": 8.49, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/French-Toast.jpg"},
            {"name": "Omelette with Mushrooms", "type": "Breakfast", "price": 8.99, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Omelette-with-Mushrooms.jpg"},
            {"name": "Avocado Toast", "type": "Breakfast", "price": 7.49, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Avocado-Toast.jpg"},
            {"name": "Breakfast Burrito", "type": "Breakfast", "price": 9.99, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Breakfast-Burrito.jpg"},
            {"name": "Bagel with Cream Cheese", "type": "Breakfast", "price": 3.99, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Bagel-with-Cream-Cheese.jpg"},
            {"name": "Granola with Yogurt", "type": "Breakfast", "price": 6.99, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Granola-with-Yogurt.jpg"},
            {"name": "Waffles with Berries", "type": "Breakfast", "price": 8.99, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Waffles-with-Berries.jpg"},
            {"name": "Sausage and Eggs", "type": "Breakfast", "price": 8.49, "restaurant_id": 39, "imageUrl": "https://i.postimg.cc/Sausage-and-Eggs.jpg"},
            {"name": "Caesar Salad", "type": "Salad", "price": 8.99, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Caesar-Salad.jpg"},
            {"name": "Greek Salad", "type": "Salad", "price": 7.99, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Greek-Salad.jpg"},
            {"name": "Cobb Salad", "type": "Salad", "price": 9.49, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Cobb-Salad.jpg"},
            {"name": "Quinoa Salad", "type": "Salad", "price": 9.99, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Quinoa-Salad.jpg"},
            {"name": "Kale and Avocado Salad", "type": "Salad", "price": 9.99, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Kale-and-Avocado-Salad.jpg"},
            {"name": "Caprese Salad", "type": "Salad", "price": 8.49, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Caprese-Salad.jpg"},
            {"name": "Spinach and Goat Cheese Salad", "type": "Salad", "price": 8.99, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Spinach-and-Goat-Cheese-Salad.jpg"},
            {"name": "Chicken Caesar Salad", "type": "Salad", "price": 10.99, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Chicken-Caesar-Salad.jpg"},
            {"name": "Beetroot and Feta Salad", "type": "Salad", "price": 8.99, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Beetroot-and-Feta-Salad.jpg"},
            {"name": "Arugula and Pear Salad", "type": "Salad", "price": 9.49, "restaurant_id": 40, "imageUrl": "https://i.postimg.cc/Arugula-and-Pear-Salad.jpg"},
            {"name": "Beef Empanadas", "type": "Empanada", "price": 4.99, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Beef-Empanadas.jpg"},
            {"name": "Chicken Empanadas", "type": "Empanada", "price": 4.49, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Chicken-Empanadas.jpg"},
            {"name": "Cheese and Onion Empanadas", "type": "Empanada", "price": 4.29, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Cheese-Onion-Empanadas.jpg"},
            {"name": "Spinach and Cheese Empanadas", "type": "Empanada", "price": 4.79, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Spinach-Cheese-Empanadas.jpg"},
            {"name": "Corn Empanadas", "type": "Empanada", "price": 4.49, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Corn-Empanadas.jpg"},
            {"name": "Pork Empanadas", "type": "Empanada", "price": 4.99, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Pork-Empanadas.jpg"},
            {"name": "Mushroom and Thyme Empanadas", "type": "Empanada", "price": 4.99, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Mushroom-Thyme-Empanadas.jpg"},
            {"name": "Shrimp Empanadas", "type": "Empanada", "price": 5.49, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Shrimp-Empanadas.jpg"},
            {"name": "Chorizo Empanadas", "type": "Empanada", "price": 4.99, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Chorizo-Empanadas.jpg"},
            {"name": "Guava and Cheese Empanadas", "type": "Dessert", "price": 4.79, "restaurant_id": 41, "imageUrl": "https://i.postimg.cc/Guava-Cheese-Empanadas.jpg"},
            {"name": "Espresso", "type": "Coffee", "price": 2.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Espresso.jpg"},
            {"name": "Cappuccino", "type": "Coffee", "price": 3.49, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Cappuccino.jpg"},
            {"name": "Latte", "type": "Coffee", "price": 3.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Latte.jpg"},
            {"name": "Americano", "type": "Coffee", "price": 2.49, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Americano.jpg"},
            {"name": "Mocha", "type": "Coffee", "price": 4.29, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Mocha.jpg"},
            {"name": "Flat White", "type": "Coffee", "price": 3.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Flat-White.jpg"},
            {"name": "Iced Coffee", "type": "Coffee", "price": 3.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Iced-Coffee.jpg"},
            {"name": "Scones", "type": "Pastry", "price": 2.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Scones.jpg"},
            {"name": "Banana Bread", "type": "Pastry", "price": 3.49, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Banana-Bread.jpg"},
            {"name": "Croissant", "type": "Pastry", "price": 2.79, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Banana-Bread.jpg"},
            {"name": "Tonkotsu Ramen", "type": "Ramen", "price": 12.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Tonkotsu-Ramen.jpg"},
            {"name": "Shoyu Ramen", "type": "Ramen", "price": 11.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Shoyu-Ramen.jpg"},
            {"name": "Miso Ramen", "type": "Ramen", "price": 12.49, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Miso-Ramen.jpg"},
            {"name": "Spicy Ramen", "type": "Ramen", "price": 13.49, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Spicy-Ramen.jpg"},
            {"name": "Vegetable Ramen", "type": "Vegetarian", "price": 10.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Vegetable-Ramen.jpg"},
            {"name": "Chicken Ramen", "type": "Chicken", "price": 11.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Chicken-Ramen.jpg"},
            {"name": "Beef Ramen", "type": "Beef", "price": 12.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Beef-Ramen.jpg"},
            {"name": "Seafood Ramen", "type": "Seafood", "price": 14.49, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Seafood-Ramen.jpg"},
            {"name": "Kimchi Ramen", "type": "Spicy", "price": 12.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Kimchi-Ramen.jpg"},
            {"name": "Cold Soba Noodles", "type": "Noodles", "price": 10.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Cold-Soba-Noodles.jpg"},
            {"name": "Classic Tiramisu", "type": "Dessert", "price": 7.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Classic-Tiramisu.jpg"},
            {"name": "Chocolate Tiramisu", "type": "Dessert", "price": 8.49, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Chocolate-Tiramisu.jpg"},
            {"name": "Strawberry Tiramisu", "type": "Dessert", "price": 8.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Strawberry-Tiramisu.jpg"},
            {"name": "Lemon Tiramisu", "type": "Dessert", "price": 8.49, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Lemon-Tiramisu.jpg"},
            {"name": "Matcha Tiramisu", "type": "Dessert", "price": 9.49, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Matcha-Tiramisu.jpg"},
            {"name": "Espresso Tiramisu", "type": "Dessert", "price": 8.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Espresso-Tiramisu.jpg"},
            {"name": "Pistachio Tiramisu", "type": "Dessert", "price": 9.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Pistachio-Tiramisu.jpg"},
            {"name": "Mango Tiramisu", "type": "Dessert", "price": 9.49, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Mango-Tiramisu.jpg"},
            {"name": "Hazelnut Tiramisu", "type": "Dessert", "price": 9.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Hazelnut-Tiramisu.jpg"},
            {"name": "Berry Tiramisu", "type": "Dessert", "price": 8.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Berry-Tiramisu.jpg"},
            {"name": "Classic Fondue", "type": "Fondue", "price": 18.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Classic-Fondue.jpg"},
            {"name": "Raclette", "type": "Cheese", "price": 20.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Raclette.jpg"},
            {"name": "Gruyere Grilled Cheese", "type": "Sandwich", "price": 9.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Gruyere-Grilled-Cheese.jpg"},
            {"name": "Blue Cheese and Pear Salad", "type": "Salad", "price": 10.49, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Blue-Cheese-Pear-Salad.jpg"},
            {"name": "Cheese Board", "type": "Appetizer", "price": 15.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Cheese-Board.jpg"},
            {"name": "Camembert Baked", "type": "Cheese", "price": 12.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Camembert-Baked.jpg"},
            {"name": "Mozzarella Sticks", "type": "Appetizer", "price": 8.49, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Mozzarella-Sticks.jpg"},
            {"name": "Brie and Fig Crostini", "type": "Appetizer", "price": 10.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Brie-Fig-Crostini.jpg"},
            {"name": "Parmesan Crisps", "type": "Appetizer", "price": 6.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Parmesan-Crisps.jpg"},
            {"name": "Stuffed Jalapenos with Cheddar", "type": "Appetizer", "price": 8.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Stuffed-Jalapenos-Cheddar.jpg"},
            {"name": "Falafel Wrap", "type": "Wrap", "price": 6.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Falafel-Wrap.jpg"},
            {"name": "Hummus Plate", "type": "Appetizer", "price": 5.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Hummus-Plate.jpg"},
            {"name": "Baba Ganoush", "type": "Appetizer", "price": 6.49, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Baba-Ganoush.jpg"},
            {"name": "Tabbouleh", "type": "Salad", "price": 5.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Tabbouleh.jpg"},
            {"name": "Stuffed Grape Leaves", "type": "Appetizer", "price": 6.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Stuffed-Grape-Leaves.jpg"},
            {"name": "Pita Bread Basket", "type": "Bread", "price": 3.49, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Pita-Bread-Basket.jpg"},
            {"name": "Lentil Soup", "type": "Soup", "price": 4.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Lentil-Soup.jpg"},
            {"name": "Shakshuka", "type": "Egg", "price": 8.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Shakshuka.jpg"},
            {"name": "Middle Eastern Sampler Plate", "type": "Appetizer", "price": 12.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Middle-Eastern-Sampler-Plate.jpg"},
            {"name": "Vegetarian Kebab", "type": "Vegetarian", "price": 7.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Vegetarian-Kebab.jpg"},
            {"name": "Apple Pie", "type": "Dessert", "price": 5.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Apple-Pie.jpg"},
            {"name": "Cherry Pie", "type": "Dessert", "price": 5.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Cherry-Pie.jpg"},
            {"name": "Pecan Pie", "type": "Dessert", "price": 6.49, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Pecan-Pie.jpg"},
            {"name": "Pumpkin Pie", "type": "Dessert", "price": 5.49, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Pumpkin-Pie.jpg"},
            {"name": "Key Lime Pie", "type": "Dessert", "price": 6.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Key-Lime-Pie.jpg"},
            {"name": "Banoffee Pie", "type": "Dessert", "price": 7.49, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Banoffee-Pie.jpg"},
            {"name": "Blueberry Pie", "type": "Dessert", "price": 5.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Blueberry-Pie.jpg"},
            {"name": "Chocolate Cream Pie", "type": "Dessert", "price": 6.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Chocolate-Cream-Pie.jpg"},
            {"name": "Lemon Meringue Pie", "type": "Dessert", "price": 6.49, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Lemon-Meringue-Pie.jpg"},
            {"name": "Sweet Potato Pie", "type": "Dessert", "price": 5.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Sweet-Potato-Pie.jpg"}]
from random import randint
import requests
import time
import json
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from app.utils.aws import get_unique_filename, upload_local_file
# test = restaurants[0]
# # response = client.images.generate(
# #     model="dall-e-3",
# #     prompt=f"a cover image for a restaurant called {test['name']} with no text",
# #     size="1024x1024",
# #     quality="standard",
# # )
# # print(response.data[0].url)
# url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-cNilt6LvlUXfb3FmQU0NDJE5/user-vC1Qt4sYOSfdNnH9W304Rs0t/img-SZiM4MzD0mrFFSpxtjNOKdd3.png?st=2024-04-26T17%3A20%3A37Z&se=2024-04-26T19%3A20%3A37Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-04-26T15%3A52%3A51Z&ske=2024-04-27T15%3A52%3A51Z&sks=b&skv=2021-08-06&sig=59wt/X%2BIHyjzOYgN/gv8VrdMEjN0qQKOgglJfYapDqo%3D"
# img_data = requests.get(url).content
# with open(f"./images/{test['name'].lower().replace(' ', '_')}.png", 'wb') as handler:
#     handler.write(img_data)
# img_loc = "./app/seeds/images/saffron_lounge.png"
# filename = get_unique_filename("saffron_lounge.png")
# upload = upload_local_file(img_loc, filename)
# print(upload)
# print(upload["url"])
# with open("./app/seeds/ai_restaurants.json", "w") as handler:
#     handler.write(json.dumps(restaurants))

# final_restaurants = []
# for restaurant in restaurants[2:]:
#     restaurant["owner_id"] = randint(1, 20)
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=f"a cover image for a restaurant called {restaurant['name']} with no text",
#         size="1024x1024",
#         quality="standard",
#     )
#     url = response.data[0].url
#     img_data = requests.get(url).content
#     filename = f"{restaurant['name'].lower().replace(' ', '_')}.png"
#     with open(f"./app/seeds/images/{filename}", 'wb') as handler:
#         handler.write(img_data)
#     unique_filename = get_unique_filename(filename)
#     img_loc = f"./app/seeds/images/{filename}"
#     upload = upload_local_file(img_loc, unique_filename)
#     print(upload)
#     restaurant["imageUrl"] = upload["url"]
#     final_restaurants.append(restaurant)
#     time.sleep(12)

# with open("./app/seeds/ai_restaurants.json", "w") as handler:
#     handler.write(json.dumps(final_restaurants))

errored_items = [{"name": "Latte", "type": "Coffee", "price": 3.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Latte.jpg"},
            {"name": "Americano", "type": "Coffee", "price": 2.49, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Americano.jpg"},
            {"name": "Mocha", "type": "Coffee", "price": 4.29, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Mocha.jpg"},
            {"name": "Flat White", "type": "Coffee", "price": 3.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Flat-White.jpg"},
            {"name": "Iced Coffee", "type": "Coffee", "price": 3.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Iced-Coffee.jpg"},
            {"name": "Scones", "type": "Pastry", "price": 2.99, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Scones.jpg"},
            {"name": "Banana Bread", "type": "Pastry", "price": 3.49, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Banana-Bread.jpg"},
            {"name": "Croissant", "type": "Pastry", "price": 2.79, "restaurant_id": 42, "imageUrl": "https://i.postimg.cc/Banana-Bread.jpg"},
            {"name": "Tonkotsu Ramen", "type": "Ramen", "price": 12.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Tonkotsu-Ramen.jpg"},
            {"name": "Shoyu Ramen", "type": "Ramen", "price": 11.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Shoyu-Ramen.jpg"},
            {"name": "Miso Ramen", "type": "Ramen", "price": 12.49, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Miso-Ramen.jpg"},
            {"name": "Spicy Ramen", "type": "Ramen", "price": 13.49, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Spicy-Ramen.jpg"},
            {"name": "Vegetable Ramen", "type": "Vegetarian", "price": 10.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Vegetable-Ramen.jpg"},
            {"name": "Chicken Ramen", "type": "Chicken", "price": 11.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Chicken-Ramen.jpg"},
            {"name": "Beef Ramen", "type": "Beef", "price": 12.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Beef-Ramen.jpg"},
            {"name": "Seafood Ramen", "type": "Seafood", "price": 14.49, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Seafood-Ramen.jpg"},
            {"name": "Kimchi Ramen", "type": "Spicy", "price": 12.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Kimchi-Ramen.jpg"},
            {"name": "Cold Soba Noodles", "type": "Noodles", "price": 10.99, "restaurant_id": 43, "imageUrl": "https://i.postimg.cc/Cold-Soba-Noodles.jpg"},
            {"name": "Classic Tiramisu", "type": "Dessert", "price": 7.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Classic-Tiramisu.jpg"},
            {"name": "Chocolate Tiramisu", "type": "Dessert", "price": 8.49, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Chocolate-Tiramisu.jpg"},
            {"name": "Strawberry Tiramisu", "type": "Dessert", "price": 8.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Strawberry-Tiramisu.jpg"},
            {"name": "Lemon Tiramisu", "type": "Dessert", "price": 8.49, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Lemon-Tiramisu.jpg"},
            {"name": "Matcha Tiramisu", "type": "Dessert", "price": 9.49, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Matcha-Tiramisu.jpg"},
            {"name": "Espresso Tiramisu", "type": "Dessert", "price": 8.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Espresso-Tiramisu.jpg"},
            {"name": "Pistachio Tiramisu", "type": "Dessert", "price": 9.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Pistachio-Tiramisu.jpg"},
            {"name": "Mango Tiramisu", "type": "Dessert", "price": 9.49, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Mango-Tiramisu.jpg"},
            {"name": "Hazelnut Tiramisu", "type": "Dessert", "price": 9.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Hazelnut-Tiramisu.jpg"},
            {"name": "Berry Tiramisu", "type": "Dessert", "price": 8.99, "restaurant_id": 44, "imageUrl": "https://i.postimg.cc/Berry-Tiramisu.jpg"},
            {"name": "Classic Fondue", "type": "Fondue", "price": 18.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Classic-Fondue.jpg"},
            {"name": "Raclette", "type": "Cheese", "price": 20.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Raclette.jpg"},
            {"name": "Gruyere Grilled Cheese", "type": "Sandwich", "price": 9.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Gruyere-Grilled-Cheese.jpg"},
            {"name": "Blue Cheese and Pear Salad", "type": "Salad", "price": 10.49, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Blue-Cheese-Pear-Salad.jpg"},
            {"name": "Cheese Board", "type": "Appetizer", "price": 15.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Cheese-Board.jpg"},
            {"name": "Camembert Baked", "type": "Cheese", "price": 12.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Camembert-Baked.jpg"},
            {"name": "Mozzarella Sticks", "type": "Appetizer", "price": 8.49, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Mozzarella-Sticks.jpg"},
            {"name": "Brie and Fig Crostini", "type": "Appetizer", "price": 10.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Brie-Fig-Crostini.jpg"},
            {"name": "Parmesan Crisps", "type": "Appetizer", "price": 6.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Parmesan-Crisps.jpg"},
            {"name": "Stuffed Jalapenos with Cheddar", "type": "Appetizer", "price": 8.99, "restaurant_id": 45, "imageUrl": "https://i.postimg.cc/Stuffed-Jalapenos-Cheddar.jpg"},
            {"name": "Falafel Wrap", "type": "Wrap", "price": 6.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Falafel-Wrap.jpg"},
            {"name": "Hummus Plate", "type": "Appetizer", "price": 5.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Hummus-Plate.jpg"},
            {"name": "Baba Ganoush", "type": "Appetizer", "price": 6.49, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Baba-Ganoush.jpg"},
            {"name": "Tabbouleh", "type": "Salad", "price": 5.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Tabbouleh.jpg"},
            {"name": "Stuffed Grape Leaves", "type": "Appetizer", "price": 6.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Stuffed-Grape-Leaves.jpg"},
            {"name": "Pita Bread Basket", "type": "Bread", "price": 3.49, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Pita-Bread-Basket.jpg"},
            {"name": "Lentil Soup", "type": "Soup", "price": 4.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Lentil-Soup.jpg"},
            {"name": "Shakshuka", "type": "Egg", "price": 8.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Shakshuka.jpg"},
            {"name": "Middle Eastern Sampler Plate", "type": "Appetizer", "price": 12.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Middle-Eastern-Sampler-Plate.jpg"},
            {"name": "Vegetarian Kebab", "type": "Vegetarian", "price": 7.99, "restaurant_id": 46, "imageUrl": "https://i.postimg.cc/Vegetarian-Kebab.jpg"},
            {"name": "Apple Pie", "type": "Dessert", "price": 5.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Apple-Pie.jpg"},
            {"name": "Cherry Pie", "type": "Dessert", "price": 5.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Cherry-Pie.jpg"},
            {"name": "Pecan Pie", "type": "Dessert", "price": 6.49, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Pecan-Pie.jpg"},
            {"name": "Pumpkin Pie", "type": "Dessert", "price": 5.49, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Pumpkin-Pie.jpg"},
            {"name": "Key Lime Pie", "type": "Dessert", "price": 6.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Key-Lime-Pie.jpg"},
            {"name": "Banoffee Pie", "type": "Dessert", "price": 7.49, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Banoffee-Pie.jpg"},
            {"name": "Blueberry Pie", "type": "Dessert", "price": 5.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Blueberry-Pie.jpg"},
            {"name": "Chocolate Cream Pie", "type": "Dessert", "price": 6.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Chocolate-Cream-Pie.jpg"},
            {"name": "Lemon Meringue Pie", "type": "Dessert", "price": 6.49, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Lemon-Meringue-Pie.jpg"},
            {"name": "Sweet Potato Pie", "type": "Dessert", "price": 5.99, "restaurant_id": 48, "imageUrl": "https://i.postimg.cc/Sweet-Potato-Pie.jpg"}]
final_menu_items = []
for item in errored_items:
    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=f"a photograph of {item['name']}",
            size="256x256",
            quality="standard",
        )
        url = response.data[0].url
        img_data = requests.get(url).content
        filename = f"{item['name'].lower().replace(' ', '_')}.png"
        with open(f"./app/seeds/images/{filename}", 'wb') as handler:
            handler.write(img_data)
        unique_filename = get_unique_filename(filename)
        img_loc = f"./app/seeds/images/{filename}"
        upload = upload_local_file(img_loc, unique_filename)
        print(upload)
        item["imageUrl"] = upload["url"]
        final_menu_items.append(item)
        time.sleep(12)
    except Exception as e:
        print(str(e))
        continue

with open("./app/seeds/ai_extra_menu_items.json", "w") as handler:
    handler.write(json.dumps(final_menu_items))
