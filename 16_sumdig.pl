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

my @array = ();

for $i (1..350){
	push @array, (0);
}
$array[0]=1;

for $i (1..1000){
	for $x (0..349){
		$array[$x]*=2;
	}
	for $x (0..349){
		if($array[$x]>9){
			$array[$x]-=10;
			$array[$x+1]++;
		}
	}
}

print OUTFILE "@array";

$total = 0;
for $elem (@array){

	$total+=$elem;

}

print $total."\n";

if($opt_b) {close TEST;}
close INFILE;
close OUTFILE;











