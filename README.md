# Cardiac Arrest Risk Predictor


## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Algorithm](#algorithm)
- [Implementation](#implementation)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Features](#features)
- [Future Improvements](#future-improvements)

## Overview

This project implements a **Decision Tree classifier from scratch** to predict cardiac arrest risk in patients based on clinical and diagnostic features. The system provides an interactive GUI application built with Tkinter that allows healthcare professionals to input patient data and receive real-time risk assessments.

The Decision Tree algorithm is implemented entirely from scratch without using machine learning libraries like scikit-learn, demonstrating a deep understanding of the algorithm's inner workings, including entropy calculation, Gini impurity, tree construction, and prediction logic.

## Problem Statement

Cardiac arrest is a life-threatening condition that requires early detection and intervention. Traditional diagnostic methods can be time-consuming and may not always provide immediate risk assessments. This project aims to:

- **Predict cardiac arrest risk** using patient clinical features
- **Assist medical professionals** in making faster diagnostic decisions
- **Provide an accessible interface** for real-time risk assessment
- **Demonstrate machine learning concepts** through a from-scratch implementation

The model classifies patients into two categories:
- **Risk Present** (value 1): Patient has >50% diameter narrowing, indicating cardiac arrest risk
- **Risk Absent** (value 0): Patient has <50% diameter narrowing, indicating no significant risk

## Dataset

The project uses the **UCI Heart Disease Dataset**, which combines data from four medical institutions:

1. **Cleveland Clinic Foundation** (cleveland.data)
2. **Hungarian Institute of Cardiology, Budapest** (hungarian.data)
3. **V.A. Medical Center, Long Beach, CA** (va.data)
4. **University Hospital, Zurich, Switzerland** (switzerland.data)

### Dataset Features

The dataset contains **14 clinical features** used for prediction:

| Feature | Type | Description |
|---------|------|-------------|
| `age` | Numerical | Patient age (years) |
| `sex` | Categorical | Gender (0: Female, 1: Male) |
| `cp` | Categorical | Chest pain type (1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic) |
| `trestbps` | Numerical | Resting systolic blood pressure (mm Hg) |
| `chol` | Numerical | Serum cholesterol (mg/dl) |
| `fbs` | Categorical | Fasting blood sugar (0: <120 mg/dl, 1: ≥120 mg/dl) |
| `restecg` | Categorical | Resting ECG results (0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy) |
| `thalach` | Numerical | Maximum heart rate achieved during thallium test |
| `exang` | Categorical | Exercise induced angina (0: No, 1: Yes) |
| `oldpeak` | Numerical | ST depression induced by exercise relative to rest |
| `slope` | Categorical | Slope of peak exercise ST segment (1: upsloping, 2: flat, 3: downsloping) |
| `ca` | Categorical | Number of major vessels (0-3) colored by fluoroscopy |
| `thal` | Categorical | Thallium test results (3: Normal, 6: Fixed defect, 7: Reversible defect) |
| `num` | Categorical | Target variable - diagnosis (0: <50% narrowing, 1: ≥50% narrowing) |

### Data Preprocessing

- Missing values (marked as "?") are handled during data loading
- Features are automatically classified as categorical or continuous based on unique value thresholds
- Data from multiple sources are concatenated and cleaned
- Features are discretized where appropriate for better tree construction

## Algorithm

### Decision Tree Implementation

The Decision Tree algorithm is implemented from scratch with the following key components:

#### 1. **Tree Construction**
- **Recursive splitting** based on best feature and threshold
- **Stopping criteria**:
  - Maximum depth reached
  - Minimum samples threshold met
  - Data purity achieved (all samples belong to same class)

#### 2. **Split Selection**
The algorithm supports two impurity metrics:

- **Entropy**: Measures information gain
  ```
  Entropy = -Σ(p_i * log2(p_i))
  ```
- **Gini Impurity**: Measures probability of misclassification
  ```
  Gini = 1 - Σ(p_i²)
  ```

#### 3. **Feature Type Handling**
- **Continuous features**: Split using threshold comparison (≤ or >)
- **Categorical features**: Split using equality comparison (= or ≠)

#### 4. **Prediction**
- Traverse tree based on feature values
- Return class label at leaf node
- Handle both binary and multi-class classification

## Implementation

### Core Components

#### `DecisionTree.py`
Contains the complete Decision Tree implementation:

- `train_test_split()`: Splits dataset into training and testing sets
- `check_purity()`: Checks if data contains only one class
- `classify_data()`: Returns majority class for a dataset
- `get_potential_splits()`: Identifies all possible split points
- `split_data()`: Splits data based on feature and threshold
- `calculate_entropy()`: Computes entropy for a dataset
- `calculate_gini()`: Computes Gini impurity
- `determine_best_split()`: Finds optimal feature and threshold
- `decision_tree_algorithm()`: Main recursive tree construction function
- `classify_example()`: Predicts class for a single instance
- `evaluate()`: Computes accuracy, precision, recall, and confusion matrix

#### `main.py`
Contains the GUI application:

- Tkinter-based interface for user input
- Real-time prediction with accuracy display
- Input validation and data preprocessing
- User-friendly warnings and information messages

#### `PreProcess.ipynb`
Data preprocessing notebook:

- Loads and combines data from multiple sources
- Handles missing values
- Feature engineering and discretization
- Data exploration and visualization

#### `decision.ipynb`
Main analysis notebook:

- Model training and evaluation
- Hyperparameter tuning
- Performance visualization
- Tree structure analysis

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Required Libraries

Install the required packages using pip:

```bash
pip install numpy pandas matplotlib seaborn
```

**Note**: Tkinter is usually included with Python installations. If not available, install it:

- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **macOS**: Usually pre-installed with Python
- **Windows**: Usually pre-installed with Python

### Setup

1. Clone the repository:
```bash
git clone https://github.com/munawwar22HU/CS-351-AI-Project.git
cd CS-351-AI-Project
```

2. Ensure data files are in the `data/` directory:
   - `processed.cleveland.data`
   - `processed.hungarian.data`
   - `processed.switzerland.data`
   - `processed.va.data`
   - `HeartData.csv` (processed combined dataset)

3. Run the application:
```bash
python main.py
```

## Usage

### GUI Application

1. **Launch the application**:
   ```bash
   python main.py
   ```

2. **Input patient data**:
   - Fill in all required fields in the GUI:
     - Age (years)
     - Gender (Male/Female)
     - Chest Pain Type
     - Systolic Blood Pressure
     - Serum Cholesterol
     - Fasting Blood Sugar
     - Resting ECG Results
     - Maximum Heart Rate
     - Exercise Induced Angina
     - ST Depression (Old Peak)
     - Slope of Peak Exercise ST Segment
     - Number of Major Vessels (CA)
     - Thallium Test Results

3. **Get prediction**:
   - Click the "Predict" button
   - View the risk assessment result
   - Check the displayed system accuracy

### Programmatic Usage

```python
from DecisionTree import *

# Load data
df = pd.read_csv("data/HeartData.csv")

# Split data
train_df, test_df = train_test_split(df, test_size=0.3)

# Train model
tree = decision_tree_algorithm(
    train_df,
    max_depth=3,
    use_entropy=False  # Use Gini impurity
)

# Evaluate model
accuracy, precision, recall = evaluate(test_df, tree)

# Predict for new patient
patient_data = {
    'age': 1.0,
    'sex': 1.0,
    'cp': 4.0,
    # ... other features
}
prediction = classify_example(patient_data, tree)
```

## Results

### Model Performance

The Decision Tree model achieved the following performance metrics:

- **Accuracy**: 81.11%
- **Precision**: 81.11%
- **Recall**:
  - Class 0 (No Risk): 72.09%
  - Class 1 (Risk Present): 89.36%

### Confusion Matrix

```
                Predicted
              No Risk  Risk
Actual No Risk   31     12
       Risk        5     42
```

### Key Findings

1. **High Recall for Risk Detection**: The model correctly identifies 89.36% of patients at risk, which is crucial for medical applications where false negatives can be life-threatening.

2. **Balanced Performance**: The model maintains good precision while prioritizing recall for the positive class (risk present).

3. **Feature Importance**: The tree structure reveals that features like `ca` (number of major vessels), `thal` (thallium test), and `cp` (chest pain type) are among the most important predictors.

### Model Configuration

- **Max Depth**: 3 levels (prevents overfitting)
- **Split Metric**: Gini Impurity
- **Train-Test Split**: 70-30 ratio
- **Min Samples**: 2 (default)

## Project Structure

```
CS-351-AI-Project/
│
├── data/
│   ├── processed.cleveland.data
│   ├── processed.hungarian.data
│   ├── processed.switzerland.data
│   ├── processed.va.data
│   ├── HeartData.csv
│   ├── HeartDataCt.csv
│   └── heart-disease.names
│
├── DecisionTree.py          # Core Decision Tree implementation
├── main.py                  # GUI application
├── PreProcess.ipynb         # Data preprocessing notebook
├── decision.ipynb           # Model training and evaluation notebook
├── predict.png              # GUI button image
├── README.md                # Project documentation
└── LICENSE                  # License file
```

## Technical Details

### Algorithm Complexity

- **Training Time**: O(n × m × log(n)) where n is number of samples and m is number of features
- **Prediction Time**: O(depth) - logarithmic in best case
- **Space Complexity**: O(n × depth) for storing the tree structure

### Design Decisions

1. **From-Scratch Implementation**: Chose to implement the algorithm from scratch to demonstrate deep understanding of Decision Trees rather than using scikit-learn.

2. **Gini vs Entropy**: The model uses Gini impurity by default as it's computationally faster and produces similar results to entropy.

3. **Max Depth Limitation**: Limited tree depth to 3 to prevent overfitting and maintain interpretability.

4. **Feature Type Detection**: Automatically detects categorical vs continuous features based on unique value count threshold (15).

5. **GUI Design**: Used Tkinter for cross-platform compatibility and ease of deployment without additional dependencies.

## Features

### Core Features

- ✅ **Decision Tree from Scratch**: Complete implementation without ML libraries
- ✅ **Dual Impurity Metrics**: Support for both Entropy and Gini impurity
- ✅ **Feature Type Handling**: Automatic detection and handling of categorical and continuous features
- ✅ **Interactive GUI**: User-friendly Tkinter interface for real-time predictions
- ✅ **Comprehensive Evaluation**: Accuracy, precision, recall, and confusion matrix
- ✅ **Data Preprocessing**: Handles missing values and multiple data sources
- ✅ **Visualization**: Tree structure visualization and performance metrics

### GUI Features

- Clean, intuitive interface
- Input validation
- Real-time accuracy display
- Clear risk warnings and information messages
- Support for all 14 clinical features

## Future Improvements

### Model Enhancements

- [ ] Implement Random Forest for improved accuracy
- [ ] Add support for other tree-based algorithms (XGBoost, LightGBM)
- [ ] Implement pruning techniques to reduce overfitting
- [ ] Add cross-validation for more robust evaluation
- [ ] Feature importance visualization

### Application Improvements

- [ ] Web-based interface using Flask/Django
- [ ] Database integration for patient record storage
- [ ] Export predictions to PDF/CSV
- [ ] Batch prediction capability
- [ ] Model versioning and A/B testing

### Technical Improvements

- [ ] Unit tests for all functions
- [ ] Performance optimization for large datasets
- [ ] Docker containerization
- [ ] API endpoint for integration with other systems
- [ ] Real-time model retraining capabilities

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Dataset**: UCI Machine Learning Repository - Heart Disease Dataset
- **Data Contributors**:
  - Hungarian Institute of Cardiology, Budapest: Andras Janosi, M.D.
  - University Hospital, Zurich: William Steinbrunn, M.D.
  - University Hospital, Basel: Matthias Pfisterer, M.D.
  - V.A. Medical Center & Cleveland Clinic: Robert Detrano, M.D., Ph.D.

## Contact

For questions or suggestions, please open an issue on GitHub or contact the repository maintainer.

---

**Note**: This project is for educational and research purposes. The predictions should not replace professional medical advice, diagnosis, or treatment.
