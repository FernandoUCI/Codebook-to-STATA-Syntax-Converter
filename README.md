
# Codebook to Stata Syntax Converter

This converter takes your typical csv-based codebook and converts the information into data labeling syntax for Stata. 

It is important that the first three columns of your codebook are labeled and formatted the same way as the <b>codebook_file.csv</b>

Here's how this csv file looks when opened:

![alt text](https://github.com/FernandoUCI/Codebook-to-STATA-Syntax-Converter/blob/master/codebook_screenshot.png)

Notice that all you need are three pieces of information:

<b>Variable</b> contains the variable name

<b>Item</b> contains the question item

<b>Response Options</b> contains the response options for each question item.

Use the <b>Codebook Converter.ipynb</b> Jupyter Notebook to run the converter. Additional instructions are given within the notebook.

After running the program, you will get two get the following Stata Syntax:<br>
Syntax that defines the labels for each unique response option.<br>
Syntax that labels each labels each variable.<br>
<br>
<br>

*** DEFINING LABELS FOR EACH UNIQUE RESPONSE OPTIONS ***

label define labelname4 1 "Yes"  0 "No"

label define labelname3 1 "Not at all true" 2 "Not true" 3 "Somewhat true" 4 "True" 5 "Very true"

label define labelname2 1 "Participated" 0 "Did not participate"

label define labelname1 1 "Online" 0 "Face-to-face"
<br><br><br>

*** DATA LABELING ***

* coursetype data label<br>
label variable coursetype "Course type"<br>
label values labelname1<br>

* pre_status data label<br>
label variable pre_status "Pre-survey participation status"<br>
label values labelname2<br>

* post_status data label<br>
label variable post_status "Post-survey participation status"<br>
label values labelname2<br>

* pre_ma3 data label<br>
label variable pre_ma3 "I like class work best when it really makes me think"<br>
label values labelname3<br>

* pre_pav6 data label<br>
label variable pre_pav6 "One reason I would not participate in class is to avoid looking stupid"<br>
label values labelname3<br>

* pre_ma5 data label<br>
label variable pre_ma5 "An important reason I do my class work is because I enjoy it"<br>
label values labelname3<br>

* pre_int data label<br>
label variable pre_int "Are you an international student?"<br>
label values labelname4<br>

* pre_eng data label<br>
label variable pre_eng "Is English your native language"<br>
label values labelname4<br>
<br><br><br><br>

## Author

**Fernando Rodriguez** https://github.com/FernandoUCI


