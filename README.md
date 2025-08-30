# Linear_Regression_With_SciKit
Implementing linear regression using SKLearn

Here's a **simple and clear README content** for your code, suitable for a project or GitHub repository:

---

## 📊 Simple Linear Regression with scikit-learn

This project demonstrates how to implement **Simple Linear Regression** using `scikit-learn` to predict salaries based on years of experience.

---

### 🧾 Dataset

The model uses a CSV file named:

```
Salary_dataset.csv
```

It must contain at least two columns:

* `YearsExperience`
* `Salary`

Example:

| YearsExperience | Salary   |
| --------------- | -------- |
| 1.1             | 39343.00 |
| 2.0             | 45000.00 |
| 3.2             | 60000.00 |
| ...             | ...      |

---

### 📦 Requirements

* Python 3.6+
* pandas
* numpy
* scikit-learn

Install them using pip if needed:

```bash
pip install pandas numpy scikit-learn
```

---

### 🚀 How It Works

1. Loads the dataset from a CSV file.
2. Extracts the input feature (`YearsExperience`) and target (`Salary`).
3. Fits a Linear Regression model.
4. Predicts the salary for a given number of years of experience.

---

### 🧪 Example Usage

```python
lr = Linear_Regression_sk()
lr.load()
print("The predicted Salary is : ", round(lr.predict([[8.0]])[0]))
```

**Output:**

```
The predicted Salary is : 100000
```

---

### 📁 File Structure

```
.
├── Linear_Regression.py      # Main Python file with class and prediction
├── Salary_dataset.csv        # Input dataset
└── README.md                 # This file
```

---

### 📌 Notes

* The model is retrained each time you call `predict()` for simplicity.
* Warnings are suppressed using `warnings.filterwarnings("ignore")`.

---

Let me know if you want a version that includes plotting, model evaluation, or command-line usage.

