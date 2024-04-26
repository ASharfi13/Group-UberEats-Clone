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
# final_menu_items = []
# for item in errored_items:
#     try:
#         response = client.images.generate(
#             model="dall-e-2",
#             prompt=f"a photograph of {item['name']}",
#             size="256x256",
#             quality="standard",
#         )
#         url = response.data[0].url
#         img_data = requests.get(url).content
#         filename = f"{item['name'].lower().replace(' ', '_')}.png"
#         with open(f"./app/seeds/images/{filename}", 'wb') as handler:
#             handler.write(img_data)
#         unique_filename = get_unique_filename(filename)
#         img_loc = f"./app/seeds/images/{filename}"
#         upload = upload_local_file(img_loc, unique_filename)
#         print(upload)
#         item["imageUrl"] = upload["url"]
#         final_menu_items.append(item)
#         time.sleep(12)
#     except Exception as e:
#         print(str(e))
#         continue

# with open("./app/seeds/ai_extra_menu_items.json", "w") as handler:
#     handler.write(json.dumps(final_menu_items))
new_reviews = [
    {"stars": 5, "description": "Absolutely loved the Chicken Tikka Masala! Best I've had in town.", "restaurant_id": 19, "user_id": 101},
    {"stars": 4, "description": "The ambiance is perfect for dining out. The Lamb Vindaloo was a bit spicy but delicious.", "restaurant_id": 19, "user_id": 102},
    {"stars": 3, "description": "Service was a bit slow, but the food was worth the wait. Enjoyed the Naan Bread.", "restaurant_id": 19, "user_id": 103},
    {"stars": 4, "description": "Kung Pao Chicken was fantastic! Will definitely return!", "restaurant_id": 20, "user_id": 104},
    {"stars": 5, "description": "Great service and the Beef and Broccoli was cooked to perfection.", "restaurant_id": 20, "user_id": 105},
    {"stars": 3, "description": "Decent food but the Sweet and Sour Pork was too sweet for my taste.", "restaurant_id": 20, "user_id": 106},
    {"stars": 4, "description": "Loved the Classic Cheeseburger, juicy and flavorful!", "restaurant_id": 21, "user_id": 107},
    {"stars": 4, "description": "Great atmosphere and delicious Bacon Burger. A must-try!", "restaurant_id": 21, "user_id": 108},
    {"stars": 5, "description": "Veggie Burger was the best I've had! Great options for vegetarians.", "restaurant_id": 21, "user_id": 109},
    {"stars": 5, "description": "Shrimp Tacos are amazing! Fresh ingredients and packed with flavor.", "restaurant_id": 22, "user_id": 110},
    {"stars": 4, "description": "A lively place with an authentic Mexican vibe. Loved the Chorizo Quesadilla.", "restaurant_id": 22, "user_id": 111},
    {"stars": 3, "description": "The food is good, but the service could be faster. Fish Tacos were worth the wait though.", "restaurant_id": 22, "user_id": 112},
    {"stars": 5, "description": "The Chicken Korma is out of this world! Highly recommended.", "restaurant_id": 23, "user_id": 113},
    {"stars": 4, "description": "Cozy atmosphere and the Lamb Rogan Josh is a must-try dish here.", "restaurant_id": 23, "user_id": 114},
    {"stars": 4, "description": "I love their vegetarian options. Dal Tadka was delightful.", "restaurant_id": 23, "user_id": 115},
    {"stars": 5, "description": "The Pho Bo was absolutely delicious, full of flavor!", "restaurant_id": 24, "user_id": 116},
    {"stars": 4, "description": "Loved the variety of noodles they offer. Dan Dan Noodles were spicy and tasty.", "restaurant_id": 24, "user_id": 117},
    {"stars": 4, "description": "Udon was cooked perfectly. A great find for noodle lovers.", "restaurant_id": 24, "user_id": 118},
    {"stars": 5, "description": "The Ribeye Steak was cooked to perfection. Highly recommend this place!", "restaurant_id": 25, "user_id": 119},
    {"stars": 4, "description": "Great ambiance and top-notch service. The Porterhouse Steak is a must-try.", "restaurant_id": 25, "user_id": 120},
    {"stars": 3, "description": "Decent steaks but a bit pricey. The Caesar Salad was fresh though.", "restaurant_id": 25, "user_id": 121},
    {"stars": 5, "description": "The Lobster Roll is the best I've had! Fresh and full of flavor.", "restaurant_id": 26, "user_id": 122},
    {"stars": 4, "description": "Loved the Seafood Linguine, and the service was excellent.", "restaurant_id": 26, "user_id": 123},
    {"stars": 4, "description": "The Grilled Sea Bass was a delight. Will come back to try more dishes.", "restaurant_id": 26, "user_id": 124},
    {"stars": 5, "description": "Every dish is a piece of art here, especially the Duck Confit. Simply sublime!", "restaurant_id": 27, "user_id": 125},
    {"stars": 4, "description": "Had a wonderful dinner. The Coq au Vin was memorable.", "restaurant_id": 27, "user_id": 126},
    {"stars": 3, "description": "Nice French cuisine, but the service was slower than expected. Ratatouille was good though.", "restaurant_id": 27, "user_id": 127},
    {"stars": 5, "description": "Best pizza in town! The Meat Lover's Pizza is incredible.", "restaurant_id": 28, "user_id": 128},
    {"stars": 4, "description": "Really enjoyed the Margherita Pizza. Fresh ingredients and a perfect crust.", "restaurant_id": 28, "user_id": 129},
    {"stars": 3, "description": "Decent pizza but I expected more from the BBQ Chicken Pizza. Good service, though.", "restaurant_id": 28, "user_id": 130},
    {"stars": 5, "description": "The Pork Dumplings are a must-try! So juicy and flavorful.", "restaurant_id": 29, "user_id": 131},
    {"stars": 4, "description": "Loved the variety of dumplings, especially the Shrimp Dumplings. Great taste and nice atmosphere.", "restaurant_id": 29, "user_id": 132},
    {"stars": 4, "description": "Really good vegetarian options like the Vegetable Dumplings. Fresh and delicious.", "restaurant_id": 29, "user_id": 133},
    {"stars": 5, "description": "The Smoked Brisket melts in your mouth! Fantastic BBQ place.", "restaurant_id": 30, "user_id": 134},
    {"stars": 4, "description": "Great BBQ Ribs and the side of Mac & Cheese was perfect. Definitely coming back.", "restaurant_id": 30, "user_id": 135},
    {"stars": 3, "description": "Good food but service could be improved. The Pulled Pork Sandwich was tasty though.", "restaurant_id": 30, "user_id": 136},
    {"stars": 5, "description": "The Pistachio Gelato is out of this world! So creamy and full of flavor.", "restaurant_id": 31, "user_id": 137},
    {"stars": 4, "description": "Love the selection of gelato. Lemon Sorbet was refreshing and perfectly tart.", "restaurant_id": 31, "user_id": 138},
    {"stars": 4, "description": "Really nice place to get authentic Italian gelato. Tiramisu flavor was a treat!", "restaurant_id": 31, "user_id": 139},
    {"stars": 5, "description": "The Vegan Burger is the best I've had! Can't believe it's not meat.", "restaurant_id": 32, "user_id": 140},
    {"stars": 4, "description": "Delicious and healthy! The Chickpea Curry had just the right amount of spice.", "restaurant_id": 32, "user_id": 141},
    {"stars": 4, "description": "Great vegan options, and the Vegan Chocolate Cake is a must-try.", "restaurant_id": 32, "user_id": 142},
    {"stars": 5, "description": "The Sushi Spot never disappoints. The Salmon Nigiri is my favorite.", "restaurant_id": 33, "user_id": 143},
    {"stars": 4, "description": "Good variety and quality sushi. The Dragon Roll was fantastic!", "restaurant_id": 33, "user_id": 144},
    {"stars": 4, "description": "Nice ambiance and quality food. Spicy Tuna Roll was delicious and had a great kick!", "restaurant_id": 33, "user_id": 145},
    {"stars": 5, "description": "The croissants here are heavenly! Perfectly flaky and buttery.", "restaurant_id": 34, "user_id": 146},
    {"stars": 2, "description": "Was excited to try the macarons but they were too sweet and a bit stale.", "restaurant_id": 34, "user_id": 147},
    {"stars": 3, "description": "The apple pie had a good flavor, but the crust was not as crispy as I like.", "restaurant_id": 34, "user_id": 148},
    {"stars": 4, "description": "The Doner Kebab is full of flavor and very satisfying.", "restaurant_id": 35, "user_id": 149},
    {"stars": 1, "description": "The Lamb Shish Kebab was undercooked and chewy. Very disappointing.", "restaurant_id": 35, "user_id": 150},
    {"stars": 5, "description": "Loved the Mixed Grill Platter. A great selection of meats and all cooked to perfection.", "restaurant_id": 35, "user_id": 151},
    {"stars": 5, "description": "The Beef Carpaccio is a must-try! Delicious and well-prepared.", "restaurant_id": 36, "user_id": 152},
    {"stars": 2, "description": "The service was slow, and the Mushroom Risotto was overly salty.", "restaurant_id": 36, "user_id": 153},
    {"stars": 3, "description": "The ambiance is nice, but the Seafood Linguine was lackluster in flavor.", "restaurant_id": 36, "user_id": 154},
    {"stars": 5, "description": "The Chicken Momo is incredible here! Full of spices and perfectly steamed.", "restaurant_id": 37, "user_id": 155},
    {"stars": 1, "description": "Had high hopes for the Beef Momo but they were greasy and the meat was tough.", "restaurant_id": 37, "user_id": 156},
    {"stars": 4, "description": "The Paneer Momo is a delightful vegetarian option, well-seasoned and fresh.", "restaurant_id": 37, "user_id": 157},
    {"stars": 4, "description": "Spaghetti Carbonara had a rich and creamy sauce, just how I like it.", "restaurant_id": 38, "user_id": 158},
    {"stars": 2, "description": "Penne Arrabbiata was overly spicy and unbalanced. Not what I expected.", "restaurant_id": 38, "user_id": 159},
    {"stars": 3, "description": "Lasagna was okay, but lacked the depth of flavor I was hoping for.", "restaurant_id": 38, "user_id": 160},
    {"stars": 5, "description": "The Eggs Benedict here are the best I've ever had! Perfectly poached eggs.", "restaurant_id": 39, "user_id": 161},
    {"stars": 2, "description": "The Pancakes were disappointing, too dry and lacked flavor.", "restaurant_id": 39, "user_id": 162},
    {"stars": 3, "description": "The French Toast is okay, but not as fluffy as I expected. Service was slow.", "restaurant_id": 39, "user_id": 163},
    {"stars": 4, "description": "The Greek Salad is fresh and vibrant, perfect for a light lunch.", "restaurant_id": 40, "user_id": 164},
    {"stars": 1, "description": "Very disappointed with the Cobb Salad, it was soggy and the dressing was bland.", "restaurant_id": 40, "user_id": 165},
    {"stars": 3, "description": "Caprese Salad had fresh tomatoes, but not enough basil or balsamic. Could be better.", "restaurant_id": 40, "user_id": 166},
    {"stars": 5, "description": "Loved the Beef Empanadas! They were juicy and well-seasoned.", "restaurant_id": 41, "user_id": 167},
    {"stars": 2, "description": "The Cheese Empanadas were too greasy and lacked flavor.", "restaurant_id": 41, "user_id": 168},
    {"stars": 4, "description": "The Chicken Empanadas are a great snack, tasty and filling.", "restaurant_id": 41, "user_id": 169},
    {"stars": 4, "description": "The Espresso is strong and flavorful, just how I like it.", "restaurant_id": 42, "user_id": 170},
    {"stars": 1, "description": "The Latte was lukewarm and the foam was not creamy at all. Very disappointed.", "restaurant_id": 42, "user_id": 171},
    {"stars": 3, "description": "The Cappuccino is decent, but the atmosphere of the place doesn't feel cozy.", "restaurant_id": 42, "user_id": 172},
    {"stars": 5, "description": "The Tonkotsu Ramen is amazing! Rich broth and tender pork.", "restaurant_id": 43, "user_id": 173},
    {"stars": 2, "description": "Miso Ramen was too salty, and the noodles were overcooked.", "restaurant_id": 43, "user_id": 174},
    {"stars": 3, "description": "Spicy Ramen has a good kick, but the broth lacked depth.", "restaurant_id": 43, "user_id": 175},
    {"stars": 5, "description": "The Classic Tiramisu is to die for! Perfectly creamy and just the right amount of coffee flavor.", "restaurant_id": 44, "user_id": 176},
    {"stars": 2, "description": "Was not impressed with the Mango Tiramisu; it was too sweet and lacked traditional flavors.", "restaurant_id": 44, "user_id": 177},
    {"stars": 3, "description": "The Chocolate Tiramisu looked promising but was too dense and not as flavorful as expected.", "restaurant_id": 44, "user_id": 178},
    {"stars": 4, "description": "The Raclette was a delightful experience, with perfectly melted cheese and a great selection of sides.", "restaurant_id": 45, "user_id": 179},
    {"stars": 1, "description": "Extremely disappointed with the Gruyere Grilled Cheese, it was burnt and very greasy.", "restaurant_id": 45, "user_id": 180},
    {"stars": 5, "description": "Loved the Classic Fondue! It was a hit with the entire family, and the dippers were fresh and tasty.", "restaurant_id": 45, "user_id": 181},
    {"stars": 5, "description": "The Falafel Wrap is fantastic here—crispy on the outside and soft on the inside, with delicious sauces.", "restaurant_id": 46, "user_id": 182},
    {"stars": 2, "description": "The Baba Ganoush was too smoky and had an overpowering garlic taste, not my favorite.", "restaurant_id": 46, "user_id": 183},
    {"stars": 4, "description": "Hummus Plate was creamy and well-seasoned. Great appetizer for the table!", "restaurant_id": 46, "user_id": 184},
    {"stars": 5, "description": "Chicken and Sausage Gumbo was a bowl of comfort—perfect spice, rich flavors.", "restaurant_id": 47, "user_id": 185},
    {"stars": 3, "description": "Seafood Gumbo was okay; the seafood tasted fresh but the gumbo base lacked the depth I hoped for.", "restaurant_id": 47, "user_id": 186},
    {"stars": 1, "description": "Jambalaya was dry and not at all what I expected. Very disappointing meal.", "restaurant_id": 47, "user_id": 187},
    {"stars": 5, "description": "The Apple Pie is just like homemade—flaky crust and perfectly sweet filling.", "restaurant_id": 48, "user_id": 188},
    {"stars": 3, "description": "Pecan Pie was too sweet for my taste, but my friend loved it.", "restaurant_id": 48, "user_id": 189},
    {"stars": 2, "description": "Cherry Pie had a soggy crust and the cherries were not tart enough, quite bland overall.", "restaurant_id": 48, "user_id": 190}
]
final_reviews = []
for review in new_reviews:
    review["user_id"] = randint(1, 20)
    final_reviews.append(review)
with open("./app/seeds/ai_reviews.json", "w") as handler:
    handler.write(json.dumps(final_reviews))
