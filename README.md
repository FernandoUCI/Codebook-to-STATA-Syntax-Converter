---
output:
  pdf_document: default
  html_document: default
---
# Codebook to STATA Syntax Converter

This converter takes your typical csv-based codebook and converts the information into data labeling syntax for STATA. 

It is important that the first three columns of your codebook are labeled and formatted the same way as the <b>codebook_file.csv</b>

Here's how this csv file looks when opened:

![alt text](https://github.com/FernandoUCI/Codebook-to-STATA-Syntax-Converter/blob/master/codebook_screenshot.png)

Notice that all you need are three pieces of information:

<b>Variable</b> contains the variable name

<b>Item</b> contains the question item

<b>Response Options</b> contains the response options for each question item.

Use the <b>Codebook Converter.ipynb</b> Jupyter Notebook to run the converter. Additional instructions are given within the notebook.

After running the program, you will get STATA output for each variable.
The first part of the output defines the labels for each unique response option
The second part of the output labels each variable




## Author

**Fernando Rodriguez** https://github.com/FernandoUCI


