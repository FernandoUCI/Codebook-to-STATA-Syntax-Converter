# Codebook to STATA Syntax Converter

This converter takes your typical csv-based codebook and converts the information into data labeling syntax for STATA. 

It is important that the first three columns of your codebook are labeled and formatted the same way as the <b>codebook_file.csv</b>

Here's how this csv file looks when opened:

![alt text](https://github.com/FernandoUCI/Codebook-to-STATA-Syntax-Converter/blob/master/codebook_screenshot.png)

Notice that all you need are three pieces of information:

<b>Variable</b> contains the variable name

<b>Item</b> contains the question item

<b>Response Options</b> contains the response options for each question item.
<br><br>
Use the <b>Codebook Converter.ipynb</b> Jupyter Notebook to run the converter. Additional instructions are given within the notebook.

After running the program, you will get STATA output for each variable:

Here's an example of the STATA output for the variable `pre_ma3`

##### * DEFINING LABELS FOR EACH UNIQUE RESPONSE OPTIONS <br>
##### label define labelname4 1 "Yes"  0 "No" <br>

##### *** DATA LABELING ***
##### label variable pre_int "Are you an international student?" <br>
##### label values labelname4  <br>



## Author

**Fernando Rodriguez** https://github.com/FernandoUCI


