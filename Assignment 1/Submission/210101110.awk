# ENVIRONMENT FOR EXECUTING THE CODE = UBUNTU 20.04 LTS


BEGIN{
print "----INVENTORY REPORT-------"
print "Part No.      Price       Quantity in Hand       Reorder Point       Minimum Report        Order Amount"
}

{
if($3<$4)
print $1,"         ",$2,"            ",$3,"               ",$4,"                  ",$5,"                     ",$5+$4-$3
else
print $1,"         ",$2,"            ",$3,"               ",$4,"                  ",$5,"                     ",$5*0
}

END{
print "------------END OF REPORT-----------"
}
