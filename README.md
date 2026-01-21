

# Topsis-aviral-102303726

A Python implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method. This repository contains the source code, an IPython notebook demonstrating the algorithm, a Flask-based web service, and a published PyPI package.

---

## Project Contents

- **IPython Notebook (`.ipynb`)**  
  A detailed notebook that explains the TOPSIS algorithm, walks through the code, and demonstrates usage with sample datasets. This is useful for learning, experimentation, and validation.

- **Web Service**  
  A Flask-based web application that allows users to:
  - Upload a CSV file containing alternatives and criteria.
  - Provide custom weights and impacts.
  - Compute TOPSIS scores and ranks.
  - Download the results as a CSV file.
  - Access the functionality through a simple browser interface.

  The web service is deployed and available here:  
  [Live Demo on Render](https://topsis-aviral-102303726.onrender.com)

- **PyPI Package**  
  The project is also published on PyPI as `topsis-aviral-102303726`, making it easy to install and use directly in Python scripts or via the command line.

---

## Features

- Accepts CSV input files with multiple alternatives and criteria.
- Supports user-defined weights and impacts for decision-making.
- Computes TOPSIS scores and assigns ranks automatically.
- Provides both a command-line interface (CLI) and a web-based interface.
- Includes an IPython notebook for demonstration and educational purposes.
- Available as a Python package on PyPI for easy installation.

---

## Installation

Install the package directly from PyPI:

```bash
pip install topsis-aviral-102303726
```

---

## Usage

### As a Python Library
```python
from topsis_aviral_102303726 import topsis

# Example usage
topsis("data.csv", "1,1,1,1", "+,+,-,+", "result.csv")
```

### As a CLI Tool
```bash
topsis data.csv "1,1,1,1" "+,+,-,+" result.csv
```

### As a Web Service (Local)
1. Clone the repository:
   ```bash
   git clone https://github.com/Avi3784/Topsis_Aviral_102303726.git
   cd Topsis_Aviral_102303726
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser at `http://localhost:5000` to access the web interface.

### As a Web Service (Deployed)
Visit the deployed version here:  
[https://topsis-aviral-102303726.onrender.com](https://topsis-aviral-102303726.onrender.com)

---

## Example

Input (`data.csv`):
```csv
Model,Price,Storage,Camera,Battery
M1,25000,64,12,3000
M2,30000,128,48,4000
M3,28000,128,12,3500
M4,35000,256,48,4500
```

Command:
```bash
topsis data.csv "0.25,0.25,0.25,0.25" "+,+,+,+" result.csv
```

Output (`result.csv`):
```csv
Model,Price,Storage,Camera,Battery,Score,Rank
M1,25000,64,12,3000,0.42,3
M2,30000,128,48,4000,0.75,1
M3,28000,128,12,3500,0.55,2
M4,35000,256,48,4500,0.30,4
```

---

## Notes

- The IPython notebook provides a detailed walkthrough of the algorithm and can be used for academic or practical understanding.  
- The web service is designed for ease of use, allowing non-programmers to apply TOPSIS through a browser.  
- The PyPI package ensures portability and quick installation for developers.  
- A live demo is available at [https://topsis-aviral-102303726.onrender.com](https://topsis-aviral-102303726.onrender.com).

---

