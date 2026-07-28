# Web Scraping HTML Table Using Selenium

## Overview

This project demonstrates how to scrape tabular data from a webpage using **Selenium WebDriver** and **Pandas** in Python.

The script automatically launches the Chrome browser, opens a webpage, locates an HTML table, extracts all rows and columns, stores the data in a Pandas DataFrame, and exports the extracted data to a CSV file.

---

## Features

- Automated browser automation using Selenium
- Extracts HTML table data
- Uses XPath to locate web elements
- Converts extracted data into a Pandas DataFrame
- Saves extracted data into a CSV file
- Simple and easy-to-understand implementation

---

## Technologies Used

- Python 3.x
- Selenium
- Pandas
- Chrome WebDriver
- WebDriver Manager

---

## Project Structure

```
Web-Scraping/
│
├── scraper.py
├── output.csv
└── README.md
```

---

## Prerequisites

Before running the project, install the required Python libraries.

```bash
pip install selenium pandas webdriver-manager
```

---

## Python Libraries Used

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
```

### Selenium

Used to automate the Chrome browser and interact with web pages.

### Pandas

Used to organize extracted data into a DataFrame and export it to CSV.

### WebDriver Manager

Automatically downloads and manages the compatible ChromeDriver.

### Time

Used to pause the program until the webpage loads completely.

---

## Workflow

The program performs the following steps:

1. Launch Chrome browser.
2. Open the target webpage.
3. Wait for the page to load.
4. Locate the HTML table.
5. Read every row (`<tr>`).
6. Read every header (`<th>`) and data cell (`<td>`).
7. Store the extracted data in a Python list.
8. Convert the list into a Pandas DataFrame.
9. Export the DataFrame to a CSV file.
10. Close the browser.

---

## Code Explanation

### Step 1: Launch Chrome Browser

```python
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
```

This launches Chrome in maximized mode.

---

### Step 2: Open the Website

```python
driver.get("https://docs.cyberark.com/pam-self-hosted/10.10/en/content/pas%20inst/endoflifepolicy.htm")
time.sleep(2)
```

The browser navigates to the specified webpage and waits for two seconds.

---

### Step 3: Locate the HTML Table

```python
table = driver.find_element(By.XPATH, "//table")
```

This locates the first HTML table on the webpage using XPath.

---

### Step 4: Extract All Rows

```python
rows = table.find_elements(By.XPATH, ".//tr")
```

This retrieves all table rows.

---

### Step 5: Store Table Data

```python
table_data = []

for row in rows:
    cells = row.find_elements(By.XPATH, ".//th | .//td")
    row_values = []

    for cell in cells:
        row_values.append(cell.text.strip())

    if row_values:
        table_data.append(row_values)
```

Each table row is processed individually.

The program extracts:

- Table headers (`<th>`)
- Table data (`<td>`)

The extracted values are stored in a nested Python list.

---

### Step 6: Display Extracted Data

```python
for row in table_data:
    print(row)
```

Prints every extracted row to the console.

---

### Step 7: Convert to DataFrame

```python
df = pd.DataFrame(table_data[1:], columns=table_data[0])
```

The first row becomes the column names, while the remaining rows become the data.

Example:

| Version | Release Date |
|----------|--------------|
| 10.1 | 2025 |
| 10.2 | 2026 |

---

### Step 8: Save as CSV

```python
df.to_csv("output.csv", index=False)
```

Exports the extracted table to a CSV file.

---

### Step 9: Print DataFrame

```python
print(df)
```

Displays the extracted table in the terminal.

---

### Step 10: Close Browser

```python
driver.quit()
```

Ends the Selenium session and closes the browser.

---

## Sample Output

```
Version,Release Date
10.1,2025
10.2,2026
```

---

## Applications

This project can be used for:

- Web scraping
- Data collection
- Report generation
- Market research
- Data analysis
- Automation tasks

---

## Advantages

- Easy to understand
- Automatic browser management
- No manual ChromeDriver installation
- Exportable CSV output
- Reusable for similar HTML tables

---

## Future Enhancements

- Scrape multiple tables
- Export to Excel
- Add logging
- Implement exception handling
- Use explicit waits instead of `time.sleep()`
- Store extracted data in a database
- Schedule automatic scraping

---

## Conclusion

This project demonstrates a simple and efficient approach to extracting tabular data from a webpage using Selenium. It showcases browser automation, HTML element identification with XPath, data extraction, data processing with Pandas, and exporting structured data into a CSV file. The project serves as a solid foundation for learning web scraping and can be extended to support more advanced automation and data extraction tasks.

---

## Author

**Ritesh Wagh**