# Data Processing

Data processing refers to the manipulation and transformation of raw data into meaningful information through various operations and techniques.

**Example:**  
A hospital collects patient records (raw data) and processes them to identify disease trends and improve patient care.

## Steps of Data Processing
1. Data Collection
2. Data Entry
3. Data Cleaning
4. Data Transformation
5. Data Analysis

---

## Data Collection

The first step in data processing is collecting raw data from various sources such as databases, sensors, surveys, or documents. This data may be structured (e.g., databases, spreadsheets) or unstructured (e.g., file documents, images, videos).

### Example
The hospital collects patient data from:
- Registration forms
- Online appointment portal
- Laboratory reports
- Insurance documents
- Doctor prescriptions

### Sample Data

| Patient ID | Name          | Age | Disease |
|------------|---------------|-----|----------|
| 101 | Rahul Sharma | 32 | Dengue |
| 102 | Priya Patel | 27 | Diabetes |

---

## Data Entry

Data is entered into a computer system or database for further processing. Data entry can be done manually by human operators or automatically through data extraction tools and software.

### Example

The hospital receptionist manually enters patient details into the Hospital Management System (HMS), while online appointment data is automatically stored in the database.

The receptionist enters:
- Name
- Age
- Mobile Number
- Address
- Disease

---

## Data Cleaning

Data cleaning is the process of identifying and correcting errors, inconsistencies, and inaccuracies in the dataset.

This stage involves tasks such as removing duplicate entries, handling missing values, correcting inaccurate data, and standardizing data formats.

### Example

The hospital removes duplicate patient records, corrects spelling mistakes in patient names, fills missing age values, and ensures all phone numbers follow the same format.

#### Before Cleaning

| Patient ID | Name | Age | Phone |
|------------|------|-----|------------|
| 101 | Rahul Sharma | 32 | 9876543210 |
| 101 | Rahul Sharma | 32 | 9876543210 |
| 102 | Priya Patil | NULL | 9876512345 |
| 103 | Amit | 25 | 98765 |

#### After Cleaning

| Patient ID | Name | Age | Phone |
|------------|------|-----|------------|
| 101 | Rahul Sharma | 32 | 9876543210 |
| 102 | Priya Patil | 28 | 9876512345 |
| 103 | Amit | 25 | 9876501234 |

---

## Data Transformation

Data transformation involves converting raw data into a format that is suitable for analysis or further processing.

This may include aggregating data, summarizing information, or performing calculations to derive new variables or metrics.

### Examples
- Calculate average patient age.
- Group patients disease-wise.
- Convert all dates to **DD/MM/YYYY** format.

### Transformed Data

| Disease | Number of Patients |
|----------|-------------------:|
| Dengue | 120 |
| Diabetes | 80 |
| Malaria | 45 |

---

## Data Analysis

Data analysis is the process of examining, interpreting, and extracting insights from the processed data.

This may involve using statistical techniques, machine learning algorithms, or data visualization tools to identify patterns, trends, relationships, or anomalies within the dataset.

### Example

The hospital analyzes the processed data to answer questions like:
- Which disease is most common?
- Which age group is most affected?
- Which month has the highest number of patients?

### Result
- Dengue cases increase during the rainy season.
- Most diabetic patients are above 40 years.