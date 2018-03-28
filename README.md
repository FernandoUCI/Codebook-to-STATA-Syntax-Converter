# Codebook to STATA Syntax Converter

This converter takes your typical csv-based codebook and converts the information into data labeling syntax for STATA. 

It is important that the first three columns of your codebook are labeled and formatted the same way as the <b>codebook_file.csv</b>

Here's this csv file looks when opened:

![alt text](https://github.com/FernandoUCI/Codebook-to-STATA-Syntax-Converter/blob/master/codebook_screenshot.png)

Notice that all you need are three pieces of information:

<b>Variable</b> contains the variable name

<b>Item</b> contains the question item

<b>Response Options</b> contains the response options for each question item


Use the <b>Codebook Converter.ipynb</b> Jupyter Notebook to run the converter. Additional instructions are given within the notebook.

After running the program, you will get the following STATA output:

* pre_ma3 DATA LABELING
label variable pre_ma3 "I like class work best when it really makes me think"
label define pre_ma3label 1 "Not at all true" 2 "Not true" 3 "Somewhat true" 4 "True" 5 "Very true"
label values pre_ma3 pre_ma3label

* pre_pav6 DATA LABELING
label variable pre_pav6 "One reason I would not participate in class is to avoid looking stupid"
label define pre_pav6label 1 "Not at all true" 2 "Not true" 3 "Somewhat true" 4 "True" 5 "Very true"
label values pre_pav6 pre_pav6label

* pre_ma5 DATA LABELING
label variable pre_ma5 "An important reason I do my class work is because I enjoy it"
label define pre_ma5label 1 "Not at all true" 2 "Not true" 3 "Somewhat true" 4 "True" 5 "Very true"
label values pre_ma5 pre_ma5label

* pre_int DATA LABELING
label variable pre_int "Are you an international student?"
label define pre_intlabel 1 "Yes"  0 "No"
label values pre_int pre_intlabel

* pre_eng DATA LABELING
label variable pre_eng "Is English your native language"
label define pre_englabel 1 "Yes"  0 "No"
label values pre_eng pre_englabel


## Author

**Fernando Rodriguez** https://github.com/FernandoUCI


