# Задание 2

# Имеется структура данных продукта.

# Уменьшите цену товара на 10%.
# Уменьшите количество единиц товара черного цвета на 7 (не забудьте пересчитать общее количество единиц).
# Добавьте изображение товара.
# Добавьте review для товара с рейтингом 2.
# Пересчитайте среднюю оценку товара и количество отзывов.

product1 = {
    "productId": 1001,
    "productName": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
    "brand": "SoundPro",
    "category": "Electronics",
    "price": 199.99,
    "currency": "USD",
    "stock": {
        "available": True,
        "quantity": 50
    },
    "images": [
        "https://example.com/products/1001/main.jpg",
        "https://example.com/products/1001/side.jpg"
    ],
    "variants": [
        {
            "variantId": "1001_01",
            "color": "Black",
            "price": 199.99,
            "stockQuantity": 20
        },
        {
            "variantId": "1001_02",
            "color": "White",
            "price": 199.99,
            "stockQuantity": 30
        }
    ],
    "dimensions": {
        "weight": "0.5kg",
        "width": "18cm",
        "height": "20cm",
        "depth": "8cm"
    },
    "ratings": {
        "averageRating": 4.7,
        "numberOfReviews": 2
    },
    "reviews": [
        {
            "reviewId": 501,
            "userId": 101,
            "username": "techguy123",
            "rating": 5,
            "comment": "Amazing sound quality and battery life!"
        },
        {
            "reviewId": 502,
            "userId": 102,
            "username": "jane_doe",
            "rating": 4,
            "comment": "Great headphones but a bit pricey."
        }
    ]
}

# Решение:

# Уменьшите цену товара на 10%
product1["price"] = product1["price"] - product1["price"] * 0.1

# Уменьшите количество единиц товара черного цвета на 7 (не забудьте пересчитать общее количество единиц).
current_quantity = product1["variants"][0]["stockQuantity"]
new_quantity = current_quantity - 7
product1["variants"][0]["stockQuantity"] = new_quantity

# Добавьте изображение товара
product1["images"].append("https://example.com/products/1001/back.jpg")

# Добавьте review для товара с рейтингом 2
new_review = {
    "reviewId": 500,
    "userId": 100,
    "username": "vlad",
    "rating": 2,
    "comment": "Cool!"
}
product1["reviews"].append(new_review)

# Пересчитайте среднюю оценку товара и количество отзывов
rating1 = product1["reviews"][0]["rating"]
rating2 = product1["reviews"][1]["rating"]
rating3 = product1["reviews"][2]["rating"]
total = rating1 + rating2 + rating3
count = len(product1["reviews"])
average = total / count
average = round(average, 1)
product1["ratings"]["averageRating"] = average
product1["ratings"]["numberOfReviews"] = count
print(product1)
