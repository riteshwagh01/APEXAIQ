# Data Cleaning

Data cleaning, also known as data cleansing or data scrubbing, is the process of identifying and correcting errors, inconsistencies, and inaccuracies in a dataset to improve its quality and reliability for analysis or decision-making purposes.

**Example:**  
Before analyzing hospital records, incorrect phone numbers, duplicate patient IDs, and missing information are corrected to ensure accurate reports.

## Steps of Data Cleaning

1. Importing and Merging
2. Standardization
3. De-duplication
4. Handling Missing Values
5. Verification
6. Export and Employ

---

## 1. Importing and Merging

Import the created dataset.

Merge two or more datasets.

### Example

**Registration Dataset**

| Patient Name | Age |
|--------------|-----|
| Rahul | 32 |

**Laboratory Dataset**

| Blood Test Result |
|-------------------|
| Positive |

**Insurance Dataset**

| Policy Number |
|---------------|
| Yes |

### After Merging

| Patient ID | Name | Age | Blood Test | Insurance |
|------------|------|-----|------------|-----------|
| 101 | Rahul | 32 | Positive | Yes |

---

## 2. Standardization

Data cleaning often includes standardizing data formats to ensure consistency and compatibility across different fields or variables.

### Example

#### Before Cleaning

**Gender**

```text
Male
male
M
MALE
```

#### After Standardization

```text
Male
```

### Another Example

#### Before Cleaning

```text
12-07-2026
12/07/2026
July 12, 2026
```

#### After Standardization

```text
12/07/2026
```

---

## 3. De-duplication

Data cleaning often involves identifying and removing duplicate records or observations within a dataset.

Duplicate entries can affect analysis results and lead to incorrect conclusions.

### Example

#### Before Cleaning

| Patient ID | Name |
|------------|------|
| 101 | Rahul |
| 101 | Rahul |

#### After De-duplication

| Patient ID | Name |
|------------|------|
| 101 | Rahul |

---

## 4. Handling Missing Values

Data cleaning involves identifying missing values and deciding how to handle them, which may include imputation (estimating missing values based on other data) or removing observations with missing values.

This may involve converting data into a common format (e.g., date formats, units of measurement) to facilitate analysis and comparison.

### Example

#### Before Cleaning

| Name | Age |
|------|-----|
| Rahul | 32 |
| Priya | NULL |

#### Possible Solutions

- Ask the patient for the missing age.
- Estimate the value if appropriate.
- Remove the incomplete record if necessary.

#### After Handling Missing Values

| Name | Age |
|------|-----|
| Rahul | 32 |
| Priya | 28 |

---

## 5. Verification

Data cleaning involves validating the integrity of the dataset to ensure that it meets quality standards and is fit for the intended purpose.

### Example

**Checks Include:**

- Phone number has 10 digits.
- Age is between 0 and 120.
- Patient ID is unique.
- No required field is empty.

This ensures the data is accurate and reliable.

---

## 6. Export and Employ

Once the data is fully cleaned and ready to process, it is exported and published for further process.

### Example

After cleaning, the hospital exports the final dataset to create:

- Monthly health reports
- Interactive dashboards
- Disease trend analysis
- Hospital management reports

**Exported File**

```text
Hospital_Cleaned_Data.csv
```