QUESTION-1 

1. Create the file question1_210101110.src
2. Start the bash script using #!/bin/sh
3. Entering the details from the user and applying the conditions given in the question, comments given in the lines to depict the steps clearly.
4. In the input file 210101110_input1.txt , we write "f1.txt f2.txt", and keep the given files blank
5. We also create the directory backup
6. In the terminal , we write
             bash question1_210101110.src 210101110_input1.txt bakcup
   to execute the given program.
   
   The code for the first question is as follows :-

---------------------------------------------------------------------------------------------------------------------------------------------------------------

#!/bin/sh

# entering the data about name of file and directory from the user
args_number=$# #for storing the number of arguements entered by the user
namefile=$1
dirname=$2

#checking the condition as mentioned in the question
if [ "$args_number" == 2 ]
then
    if [ -f "$namefile" ] # checking if the file exists or not
    then 
        if [ -d "$dirname" ] #checking if the directory exists or not
        then
            while read list ;
            
            do
            cp $list $dirname # for copying the given file names into the directory
            done < $namefile # closing the given file
            cd $dirname # changing the working directory into the required directory
            for file in *.*
            do
                mv -v "$file" "${file%.*}.bak"
            done; # changing the extension of .txt file into .bak
            
            
        else 
            echo "The given directory does not exist"
        fi
        
        
    else
    
        if [ -d "$dirname" ] #checking if the directory exists, if the file does not exist
        then
            echo "The given file does not exist"
        else 
            echo "The directory and the file does not exist"
        fi
        
        
    fi 
    
    
else 


    echo "You have entered invalid information"
fi

---------------------------------------------------------------------------------------------------------------------------------


QUESTION-2 :-

1. In the terminal, we write 
       sudo apt-get install perl
   to install the software and the compiler for perl.
   
2. We write gedit 210101110_question2.pl to open the perl file.
3. At the top of the file, we write #!usr/bin/perl to start the perl file
4. We read the file from the path using the syntax as mentioned in the code, closing the <FILE>.
5. We use "chop" to remove the line chanegs at the end of the sentences read.
6. We enter the data from the user.
7. Then we keep a track of all the changes with the length of the strings and the maximum permissible length of printing as mentioned in the question.
8. The steps have been explained in the comments.
9. In the terminal, we write perl 210101110_question2.pl to execute the program.

#!usr/bin/perl

#starting the program
# the following is to store the string from a file into a variable  

open(FILE,"/home/vj_vatsal_/testing.txt") or die "Can't read file!";
$content = <FILE>;
close(FILE);
chop $content; #chop function is used to remove the line changes from the end of the sentence


# input for count and length is given by the user
print "Enter count:";
$count = <STDIN>;
print "Enter length:";
$length = <STDIN>;

$t=1; # this variable keeps a track of the no of characters in the string being printed


$lengthofstring = length($content);
@lastindex = $lengthofstring+1;


$content =~ tr/ //ds; # this is used to remove the spaces from the string to avoid the blank spaces from being printed
@array = split(//,$content); # storing the string into an array of characters
# this loop is for printing the characters based on conditions



for($t=1;$t<=$length;$t = $t+0)
{
# for random index
do
{
$index = rand($lengthofstring);
$index = int($index);
}while($lastindex == $index);

#storing the character at that random index
$ch= $array[$index];
# randomizing count and storing it in a variable
$ra = rand($count);
$ra = int($ra);
# the following loop is for printing the characters and updating t for keeping a check with the condition 


for($i=0;$i<$ra;$i=$i+1)
{
if ( ($t<=$length) )
{
print "$ch";
$t=$t+1;
}
}
$lastindex = $index;
};

print "\n";
-------------------------------------------------------------------------
