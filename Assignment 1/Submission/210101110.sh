# ENVIRONMENT FOR EXECUTING THE CODE = UBUNTU 20.04 LTS

#!/bin/bash
# printing the heading
echo "-------------PAYROLL REGISTER--------------"

#printing the column heads
echo "Employee No.        Department          Pay Rate          Exempt           Hours Worked          Base Pay          Overtime Pay         Total Pay"

#reading the data from the file and storing it in the array
while read -a data;
do

#calculating basepay using bc command
basepay=$( bc <<< " ${data[2]} * ${data[4]} "  )

# checking the exempt condition

if [ ${data[3]} == "Y" ]
then
over=0
total=$( bc <<< " $basepay ")
else
over=$( bc <<< " (${data[4]} - 40 )0.5${data[2]} "  )
total=$( bc <<< " $basepay + $over " )

fi

# printing the data
echo " ${data[0]}                   ${data[1]}               ${data[2]}                 ${data[3]}                  ${data[4]}               $basepay                  $over              $total "

# taking input from the file EMPLOYEE.txt
done < ques2input.txt

