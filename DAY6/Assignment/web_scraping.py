from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Launch Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Open Website
driver.get("https://docs.cyberark.com/pam-self-hosted/10.10/en/content/pas%20inst/endoflifepolicy.htm")
time.sleep(2)

# Locate table
table = driver.find_element(By.XPATH, "//table")

# Get all rows
rows = table.find_elements(By.XPATH, ".//tr")

table_data = []

for row in rows:
    cells = row.find_elements(By.XPATH, ".//th | .//td")
    row_values = []

    for cell in cells:
        row_values.append(cell.text.strip())

    if row_values:
        table_data.append(row_values)

# Display extracted data
for row in table_data:
    print(row)

# Convert to DataFrame
df = pd.DataFrame(table_data[1:], columns=table_data[0])

# Save CSV
df.to_csv("output.csv", index=False)

print(df)

driver.quit()