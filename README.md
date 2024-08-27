# USD Currency Converter Application

## Overview

This Python-based application allows users to convert an amount in USD to various other currencies using up-to-date exchange rates. The application features a user-friendly graphical interface (GUI) designed with Tkinter, making it easy to input values and view converted amounts.

## Features

- **Real-Time Currency Conversion:** Converts USD to multiple currencies using the latest exchange rates.
- **User-Friendly GUI:** Simple and intuitive interface for easy navigation and operation.
- **Dynamic Updates:** Refreshes exchange rates to ensure accuracy during conversions.
- **Edge Case Handling:** Manages very large or small amounts to provide reliable results.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - Tkinter (for GUI development)
  - Requests (for API calls)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Idhaya-Yuvarj/usd-currency-converter.git
   cd usd-currency-converter
   ```

2. **Install the Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python currency_converter.py
   ```

## How It Works

1. **Input:** Users enter the amount in USD they wish to convert.
2. **Select Currency:** Choose the target currency from the dropdown menu.
3. **Convert:** Click the "Convert" button to view the converted amount in the selected currency.
4. **Refresh Rates:** The "Refresh Rates" button fetches the latest exchange rates to ensure accuracy.


## Future Enhancements

- Add more currencies for conversion.
- Implement error handling for API failures.
- Enhance the GUI for a more modern look and feel.
