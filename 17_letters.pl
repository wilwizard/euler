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

@array = ();
@numwords = ("","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen");
@tenwords = ("","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety");
$total = 0;

for $i (0..1000){

	$temp = "";
	$hundreds = $i - $i%100;
	$tens = $i%100-$i%10;
	$ones = $i%10;

	if($hundreds) {
		$temp.=$numwords[$hundreds/100]."hundred";
		if($tens||$ones){
			$temp.="and";
		}
	}
	if($tens>10){
		$temp.=$tenwords[$tens/10];
	}
	if($tens==10) {
		$temp.=$numwords[$tens+$ones];
	}
	elsif($ones) {
		$temp.=$numwords[$ones];
	}
	$array[$i]=$temp;
	#print $i.":".$temp."\n";
}

$array[1000]="onethousand";

for $elem (@array){

	print OUTFILE length($elem).":".$elem."\n";
	$total+=length($elem);

}

print $total."\n";



if($opt_b) {close TEST;}
close INFILE;
close OUTFILE;











