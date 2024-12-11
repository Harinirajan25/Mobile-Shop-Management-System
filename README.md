# Mobile Shop Management System

## Description
The Mobile Shop Management System is a Python-based console application for efficiently managing a mobile shop inventory. It allows users to:

- View all mobiles categorized by brand, color, or price.
- Search and display specific brands.
- Browse mobiles based on their attributes for easy decision-making.

This program streamlines mobile inventory management and enhances customer experience.

---

## Features

1. **Display by Brand**
   - Lists all available models under each brand, including their colors and prices.

2. **Display by Color**
   - Categorizes and displays mobiles based on their colors.

3. **Display by Price**
   - Shows mobile details sorted by their prices.

4. **Search Specific Brand**
   - Allows users to filter and view details of mobiles under a single brand.

5. **Exit**
   - Provides an option to exit the application.

---

## How to Use

1. Run the program using Python.
2. Use the menu to select the desired option:
   - `1`: Display mobiles by brand.
   - `2`: Display mobiles by price.
   - `3`: Display mobiles by color.
   - `4`: Exit the application.
3. For brand-specific search, enter the brand name to view models available under it.

---

## Code Structure

The program is implemented using a `mobileshop` class with:

- **Class Variables**: Holds shop details, inventory lists, and sets for brands, colors, and prices.
- **Instance Variables**: Stores mobile attributes like brand, model, color, and price.
- **Methods**:
  - `display_brand`: Displays mobiles grouped by brand.
  - `display_color`: Displays mobiles grouped by color.
  - `display_price`: Displays mobiles grouped by price.
  - `one_brand`: Searches and displays mobiles of a specific brand.

---

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of Python to modify or enhance the program if needed.

---

## Future Enhancements

- Add price filtering (e.g., within a range).
- Enable persistent storage for inventory using a database.
- Develop a GUI for easier navigation and user interaction.

---

## License
This project is open-source and available for modification and distribution under the [AVH](https://avhinfotechs.netlify.app).
