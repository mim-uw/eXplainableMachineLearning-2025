# Homework 2

The purpose of the second homework is to become familiar with Local Interpretable Model-agnostic Explanations (LIME). 

You may use any vision model from https://huggingface.co/. 
You can choose any classification problem. 
There are many example models on huggingface, for example, for food classification.
You can also try to reproduce the classification example for wolf/husky classes shown in the paper on LIME.

Try to implement the lime algorithm yourself, for this there is a full set of points. If you have problems, you can use some existing implementation, for this there will be a part of points.

Submit the homework to this directory.

## Deadline 

2023-11-08 EOD

## Task

For the selected two or three images and a vision model, prepare a knitr/jupyter notebook based on the following points.
Submit your results on GitHub to the directory `Homeworks/HW2`.

1. Calculate the predictions for selected observations
2. Then, calculate 20-50 regions (may be less, depending on the resolution of the image) for a given image. You may divide the image in a grid of rectangles or use some smarter segmentation algorithms.
3. Generate N (100-1000 depending) subimages with randomly selected parts of an image. Calculate predictions for these parts.
4. Calculate LIME explanations 
5. Comment on the results obtained in (4)


## **Important note:**

Try to convert the jupyter notebook into an HTML file, e.g. using the following command in bash

```
jupyter nbconvert --to=html --template=classic FILE_NAME.ipynb
```

The submitted homework should consist of two parts:

1. The 1st part is the key results and comments from points (3)-(5). In this part **PLEASE DO NOT SHOW ANY R/PYTHON CODES, ONLY RESULTS (FIGURES, COMMENTS).**
2. The 2nd part should start with the word "Appendix" or "Załącznik" and should include the reproducible R/Python code used to implement points (1)-(5).

Such division: 1. will make this homework more readable, and 2. will develop good habits related to reporting.


