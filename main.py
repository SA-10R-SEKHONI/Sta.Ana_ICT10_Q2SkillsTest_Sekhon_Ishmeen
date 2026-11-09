from pyscript import document

# Perfume Information Dictionary
perfumes = {

    "BESPOKE LONDON WOMAN": {
        "name": "Bespoke London Woman",
        "brand": "Bespoke London",
        "type": "Fruity Gourmand",
        "middle_notes": "Mandarin, Praline and White Flowers"
    },

    "GOLDEN HOUR": {
        "name": "Golden Hour",
        "brand": "Lux Organics",
        "type": "Fresh",
        "middle_notes": "Peach Blossom, Neroli and White Tea"
    },

    "EUPHORIA": {
        "name": "Euphoria",
        "brand": "Calvin Klein",
        "type": "Amber Floral",
        "middle_notes": "Black Orchid, Lotus and Champaca"
    },

    "BLACK TIE": {
        "name": "Black Tie",
        "brand": "Celine",
        "type": "Woody Vanilla",
        "middle_notes": "Iris, Cedarwood and Soft Musk"
    },

    "BLACK OPIUM": {
        "name": "Black Opium",
        "brand": "Yves Saint Laurent",
        "type": "Warm Spicy Gourmand",
        "middle_notes": "Coffee, Jasmine and Bitter Almond"
    },

    "GOOD GIRL": {
        "name": "Good Girl",
        "brand": "Carolina Herrera",
        "type": "Amber Gourmand",
        "middle_notes": "Tuberose and Jasmine Sambac"
    },

    "COCO MADEMOISELLE": {
        "name": "Coco Mademoiselle",
        "brand": "Chanel",
        "type": "Amber Woody",
        "middle_notes": "Rose and Jasmine"
    },

    "SAUVAGE": {
        "name": "Sauvage Eau de Toilette",
        "brand": "Dior",
        "type": "Aromatic Fougere",
        "middle_notes": "Sichuan Pepper and Lavender"
    },

    "WOOD SAGE": {
        "name": "Wood Sage & Sea Salt",
        "brand": "Jo Malone London",
        "type": "Woody Aromatic",
        "middle_notes": "Sea Salt and Sage"
    },

    "ALIEN": {
        "name": "Alien",
        "brand": "Mugler",
        "type": "Amber Woody",
        "middle_notes": "Jasmine Sambac"
    },

    "GODDESS": {
        "name": "Burberry Goddess",
        "brand": "Burberry",
        "type": "Vanilla Aromatic Gourmand",
        "middle_notes": "Caviar Vanilla and Vanilla Infusion"
    },

    "DAISY": {
        "name": "Daisy",
        "brand": "Marc Jacobs",
        "type": "Fruity Floral",
        "middle_notes": "Violet and Jasmine"
    }

}

# Perfume Search Function
def perfume_checker(event):

    perfume_name = document.getElementById(
        "perfume_name"
    ).value.strip().upper()

    result = document.getElementById("result")

    if perfume_name in perfumes:

        perfume = perfumes[perfume_name]

        result.innerHTML = f"""
            <h4 class="text-warning">
                {perfume["name"]}
            </h4>

            <hr>

            <p>
                <strong>Perfume Name:</strong>
                {perfume["name"]}
            </p>

            <p>
                <strong>Brand:</strong>
                {perfume["brand"]}
            </p>

            <p>
                <strong>Fragrance Type:</strong>
                {perfume["type"]}
            </p>

            <p>
                <strong>Middle Notes:</strong>
                {perfume["middle_notes"]}
            </p>
        """

    else:

        result.innerHTML = """
            <div class="text-danger">
                <h5>Perfume Not Found!</h5>

                <p>
                    This perfume does not exist
                    in our collection.
                </p>

                <p>
                    Please enter another perfume name.
                </p>
            </div>
        """