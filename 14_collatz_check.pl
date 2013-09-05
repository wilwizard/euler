use Getopt::Std;
#use strict;
use vars '$opt_b';
require 'funcs.pl';

getopts('b');

my $input="file.txt";
my $output=">new_file.txt";
my $test=">test.txt";

if($opt_b) {open(TEST, $test);}
open(INFILE, $input);
open(OUTFILE, $output);

	

$i = $ARGV[0];	
$temp = $i;
$count = 0;

while ($temp > 1){
	
	print OUTFILE $temp .":". $count . "\n";
	if ($temp % 2 == 0) {
		$temp /= 2;	
	}else{
		$temp = 3*$temp+1;
	}
	$count++;
	
}

print OUTFILE $temp .":". $count . "\n";





if($opt_b) {close TEST;}
close INFILE;
close OUTFILE;































close (TEST);
close (INFILE);	
close (OUTFILE);



