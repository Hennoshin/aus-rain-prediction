# Rain Prediction In Australia with Machine Learning

## Repository Outline

```
1. README.md - Project Overview
2. P1M2_Irfan_Hilmi.ipynb - Notebook which contains the main model creation, from data loading to model saving
3. P1M2_Irfan_Hilmi_Infer.ipynb - Example of model inference using new data
4. weatherAUS.csv - Dataset being used for the model
5. deployment/app.py - Streamlit app for deployment
6. deployment/features_values.json - JSON file for deployment purpose, contains reference values for the deployed app
7. deployment/missing_indicator.py - Custom class used by the model
dst.
```

## Problem Background
Rainfall is one of the most important factors in agriculture since it provides water for crops. This is especially true for places that are usually dry and don’t receive much rainfall, such as Australia. Therefore, rainfall prediction is rather important for farmers and agricultural workers in Australia since it helps them manage and prepare their water resources more effectively and efficiently. This project aims to solve this problem and enables a more efficient water resource management for farmers.

Therefore, this model is created to help solve the water management problem by predicting whether or not there will be rain tomorrow so farmers can prepare accordingly.

## Project Output
The output of this project is deployment of app using Streamlit to HuggingFace repository. The deployed model can be accessed here:

## Data
The data is a weather data in the region of Australia. Refer to the main notebook for full description of the data.

## Method
The final model being used for this prediction is Random Forest model.

## Stacks
Languange: Python
Machine Learning Library: Scikit Learn

## Reference
Problem Background Reference:
https://www.visualcrossing.com/resources/blog/how-does-weather-affect-agriculture/#:~:text=Precipitation%20Since%20precipitation%20is%20the%20primary%20source,rainfall%20helps%20ensure%20those%20needs%20are%20met

https://www.nature.com/articles/103447b0

Deployment Link: https://huggingface.co/spaces/Hennoshin/Rain_Predictor_Deployment

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
