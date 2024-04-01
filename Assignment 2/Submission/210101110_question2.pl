#!usr/bin/perl

#starting the program
# the following is to store the string from a file into a variable  

open(FILE,"/home/vj_vatsal_/Assignment2/input2.txt") or die "Can't read file!";
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
