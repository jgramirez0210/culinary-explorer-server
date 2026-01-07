# Culinary Explorer Database Schema and Dummy Data

This document outlines the database schema for the Culinary Explorer Django application, including all models, their fields, and example dummy data in Django fixture format.

## Database Models

### 1. User Model
**App:** `culinary_explorer_api`  
**Table:** `culinary_explorer_api_user`

| Field | Type | Max Length | Description |
|-------|------|------------|-------------|
| `id` | AutoField | - | Primary key |
| `first_name` | CharField | 50 | User's first name |
| `last_name` | CharField | 50 | User's last name |
| `email_address` | EmailField | 50 | User's email address |
| `profile_image_url` | CharField | 255 | URL to user's profile image |
| `uid` | CharField | 50 | Unique user identifier |

**Example Dummy Data:**
```json
[
  {
    "model": "culinary_explorer_api.user",
    "fields": {
      "first_name": "John",
      "last_name": "Doe",
      "email_address": "john.doe@example.com",
      "profile_image_url": "https://example.com/profiles/john.jpg",
      "uid": "user123"
    }
  },
  {
    "model": "culinary_explorer_api.user",
    "fields": {
      "first_name": "Jane",
      "last_name": "Smith",
      "email_address": "jane.smith@example.com",
      "profile_image_url": "https://example.com/profiles/jane.jpg",
      "uid": "user456"
    }
  }
]
```

### 2. Categories Model
**App:** `culinary_explorer_api`  
**Table:** `culinary_explorer_api_categories`

| Field | Type | Max Length | Description |
|-------|------|------------|-------------|
| `id` | AutoField | - | Primary key |
| `category` | CharField | 50 | Category name (e.g., "Dine In", "Take Out") |

**Example Dummy Data:**
```json
[
  {
    "model": "culinary_explorer_api.categories",
    "fields": {
      "category": "Dine In"
    }
  },
  {
    "model": "culinary_explorer_api.categories",
    "fields": {
      "category": "Take Out"
    }
  },
  {
    "model": "culinary_explorer_api.categories",
    "fields": {
      "category": "Delivery"
    }
  },
  {
    "model": "culinary_explorer_api.categories",
    "fields": {
      "category": "Home Made"
    }
  }
]
```

### 3. Restaurants Model
**App:** `culinary_explorer_api`  
**Table:** `culinary_explorer_api_restaurants`

| Field | Type | Max Length | Description |
|-------|------|------------|-------------|
| `id` | AutoField | - | Primary key |
| `restaurant_name` | CharField | 100 | Name of the restaurant |
| `restaurant_address` | CharField | 100 | Physical address of the restaurant |
| `website_url` | CharField | 100 | Restaurant's website URL |
| `uid` | CharField | 50 | Unique identifier (default: "aPkqPWh2qYXzL2OHlFunih1ZR3U2") |

**Example Dummy Data:**
```json
[
  {
    "model": "culinary_explorer_api.restaurants",
    "fields": {
      "restaurant_name": "Bella Italia",
      "restaurant_address": "123 Main St, Anytown, USA",
      "website_url": "https://bella-italia.com",
      "uid": "rest123"
    }
  },
  {
    "model": "culinary_explorer_api.restaurants",
    "fields": {
      "restaurant_name": "Sakura Sushi",
      "restaurant_address": "456 Oak Ave, Somewhere, USA",
      "website_url": "https://sakura-sushi.com",
      "uid": "rest456"
    }
  },
  {
    "model": "culinary_explorer_api.restaurants",
    "fields": {
      "restaurant_name": "Taco Fiesta",
      "restaurant_address": "789 Pine Rd, Elsewhere, USA",
      "website_url": "https://taco-fiesta.com",
      "uid": "rest789"
    }
  }
]
```

### 4. Dish Model
**App:** `culinary_explorer_api`  
**Table:** `culinary_explorer_api_dish`

| Field | Type | Max Length | Description |
|-------|------|------------|-------------|
| `id` | AutoField | - | Primary key |
| `dish_name` | CharField | 100 | Name of the dish |
| `description` | CharField | 500 | Detailed description of the dish |
| `notes` | CharField | 100 | Additional notes about the dish |
| `food_image_url` | URLField | 500 | URL to an image of the dish |
| `price` | CharField | 100 | Price of the dish as a string |

**Example Dummy Data:**
```json
[
  {
    "model": "culinary_explorer_api.dish",
    "fields": {
      "dish_name": "Margherita Pizza",
      "description": "Classic Italian pizza with tomato sauce, mozzarella cheese, and fresh basil",
      "notes": "Vegetarian option available",
      "food_image_url": "https://example.com/images/margherita-pizza.jpg",
      "price": "$12.99"
    }
  },
  {
    "model": "culinary_explorer_api.dish",
    "fields": {
      "dish_name": "California Roll",
      "description": "Sushi roll with crab, avocado, and cucumber",
      "notes": "Contains shellfish",
      "food_image_url": "https://example.com/images/california-roll.jpg",
      "price": "$8.50"
    }
  },
  {
    "model": "culinary_explorer_api.dish",
    "fields": {
      "dish_name": "Beef Tacos",
      "description": "Three soft tacos filled with seasoned ground beef, lettuce, cheese, and salsa",
      "notes": "Spicy option available",
      "food_image_url": "https://example.com/images/beef-tacos.jpg",
      "price": "$9.99"
    }
  },
  {
    "model": "culinary_explorer_api.dish",
    "fields": {
      "dish_name": "Chicken Parmesan",
      "description": "Breaded chicken breast topped with marinara sauce and melted cheese, served with spaghetti",
      "notes": "Gluten-free pasta available",
      "food_image_url": "https://example.com/images/chicken-parmesan.jpg",
      "price": "$16.99"
    }
  }
]
```

### 5. Food_Log Model
**App:** `culinary_explorer_api`  
**Table:** `culinary_explorer_api_food_log`

| Field | Type | Max Length | Description |
|-------|------|------------|-------------|
| `id` | AutoField | - | Primary key |
| `restaurant` | ForeignKey | - | Reference to Restaurants model |
| `dish` | ForeignKey | - | Reference to Dish model |
| `category` | ManyToManyField | - | Reference to Categories model (multiple categories possible) |
| `uid` | CharField | 50 | User ID associated with this log entry |

**Example Dummy Data:**
```json
[
  {
    "model": "culinary_explorer_api.food_log",
    "fields": {
      "restaurant": 1,
      "dish": 1,
      "category": [1],
      "uid": "user123"
    }
  },
  {
    "model": "culinary_explorer_api.food_log",
    "fields": {
      "restaurant": 2,
      "dish": 2,
      "category": [2],
      "uid": "user456"
    }
  },
  {
    "model": "culinary_explorer_api.food_log",
    "fields": {
      "restaurant": 3,
      "dish": 3,
      "category": [1, 3],
      "uid": "user123"
    }
  },
  {
    "model": "culinary_explorer_api.food_log",
    "fields": {
      "restaurant": 1,
      "dish": 4,
      "category": [1],
      "uid": "user456"
    }
  }
]
```

## Relationships

- **User** has no direct relationships with other models in the current schema
- **Categories** is used in a many-to-many relationship with **Food_Log**
- **Restaurants** is referenced by **Food_Log** (one-to-many)
- **Dish** is referenced by **Food_Log** (one-to-many)
- **Food_Log** connects users (via uid), restaurants, dishes, and categories

## Loading Dummy Data

To load the dummy data into the database, use Django's `loaddata` management command:

```bash
python manage.py loaddata categories.json
python manage.py loaddata restaurants.json
python manage.py loaddata dish.json
python manage.py loaddata users.json
python manage.py loaddata food_log.json
```

Note: The order is important due to foreign key relationships. Always load fixture files for models without foreign keys first.

## Notes

- All string fields use CharField instead of TextField for simplicity
- Prices are stored as strings to accommodate various formats (e.g., "$12.99", "12.99 USD")
- The `uid` field in multiple models appears to be used for user identification, possibly from an external authentication system
- Image URLs are stored as strings; in a production environment, consider using a proper image handling solution
- The `food_image_url` field in Dish has a default value of 'https://example.com/default-image.jpg'