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


my %main_hash = ();
my $max = 0;

for $i (2..1000000) {
	$temp = $i;
	$count = 0;
	
	
	while ($temp > 1){
		if ($main_hash{$temp}){
			$count = $main_hash{$temp} + $count;
			last;
		}
	
		if ($temp % 2 == 0) {
			$temp /= 2;	
		}else{
			$temp = 3*$temp+1;
		}
		$count++;
	}

	$main_hash{$i} = $count;
	
	if ($count > $max) {
		$max = max($count,$max);
		print $i .":". $max . "\n";
	}
}



if($opt_b) {close TEST;}
close INFILE;
close OUTFILE;































close (TEST);
close (INFILE);	
close (OUTFILE);



