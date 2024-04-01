THE CODE FOR QUESTION 1 IS AS FOLLOWS

BEGIN{
print "----INVENTORY REPORT-------"
print "Part No.      Price       Quantity in Hand       Reorder Point       Minimum Report        Order Amount"
}
// this part is for printing the headings


{
if($3<$4)
print $1,"         ",$2,"            ",$3,"               ",$4,"                  ",$5,"                     ",$5+$4-$3
else
print $1,"         ",$2,"            ",$3,"               ",$4,"                  ",$5,"                     ",$5*0
}
// this part is for calculating the result based on the condition, for each part no.


END{
print "------------END OF REPORT-----------"
}
// this demonstrates the end of the report



COMMANDS FOR TERMINAL (EXECUTION OF THE CODES)

mkdir Assignment1 // creating a directory
cd Assignment1 // going to that directory
gedit 210101110.awk // creating awk file and writing awk code in it
gedit ques1input.txt // storing inventory report's data
awk -f 210101110.awk ques1input.txt // execution of the code and the report is printed on the terminal


------------------------------------------------------- END OF THE FIRST QUESTION --------------------------------------------



THE CODE FOR THE SECOND QUESTION IS AS FOLLOWS

#!/bin/bash // BASIC SYNTAX FOR INITIALIZING BASH FILE
# printing the heading
echo "-------------PAYROLL REGISTER--------------" // USING ECHO COMMAND FOR PRINTING

#printing the column heads
echo "Employee No.        Department          Pay Rate          Exempt           Hours Worked          Base Pay          Overtime Pay         Total Pay"

#reading the data from the file and storing it in the array
while read -a data; // STORING THE DATA IN AN ARRAY WHILE READING EACH LINE
do

#calculating basepay using bc command
basepay=$( bc <<< " ${data[2]} * ${data[4]} "  )  // BASIC BASE PAY CALCULATION




# checking the exempt condition

if [ ${data[3]} == "Y" ]
then
over=0
total=$( bc <<< " $basepay ")
else
over=$( bc <<< " (${data[4]} - 40 )0.5${data[2]} "  )
total=$( bc <<< " $basepay + $over " )

fi
// IF-ELSE BLOCK FOR CALCULATION OF OVERTIME AND TOTAL PAY BASED ON CONDITION





# printing the data
echo " ${data[0]}                   ${data[1]}               ${data[2]}                 ${data[3]}                  ${data[4]}               $basepay                  $over              $total "
// PRINTING THE FINAL DATA IN TABULAR FORM





# taking input from the file ques2input.txt
done < ques2input.txt
// END OF PROGRAM



COMMANDS FOR TERMINAL :-

cd Assignment1 // going into the directory, if already not there
gedit 210101110.sh // for writing bash script
gedit ques2input.txt // for writing and storing data
chmod +x 210101110.sh // for permission to execute bash file
./210101110.sh // to execute bash file



------------------------------------------- END OF THE SECOND QUESTION ---------------------------------------


