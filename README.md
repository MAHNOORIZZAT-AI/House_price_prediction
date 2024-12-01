# House_price_prediction

## Overview
This project aims to predict house prices using various machine learning algorithms. The dataset used contains features such as the number of bedrooms, bathrooms, floors, and built year.

## Dataset
The dataset used for this project is the **Ames Housing dataset**. It includes detailed information about houses sold in Ames, Iowa.

## Requirements
- Python 3.x
- Jupyter Notebook
- Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn

You can install the required libraries using:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Project Structure
```
house-price-prediction/
├── static/
│   └── css
│   └── main
├── template/
│   └── index
├── data/
│   └── data.csv
├── notebooks/
│   └── model.ipynb
├── src/
│   ├── model.py
│   ├── model.pickle
│   └── app.py
├── README.md

```

## Usage
1. **Applying Model**: fit the model on input and output variables.
   ```python
   from sklearn.linear_model import LinearRegression
    regr = LinearRegression()
    regr.fit(X,y)
   ```

2. **Model Training**: Train the model using the preprocessed data.
   ```python
   pickle.dump(regr, open('model.pickle', 'wb')): This command serializes the regr object (which is presumably your trained model) and writes it to a file named model.pickle in 
   binary mode ('wb')
    ```
3. **Model Evaluation**: Evaluate the model's performance.
   ```python
   from src.model_evaluation import evaluate_model
   evaluate_model(model, data)
   ```

## Results
The model's performance to predict the price on bedrooms, bathrooms, floors, yr_built

## Contributing
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

---

