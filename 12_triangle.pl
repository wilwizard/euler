use Getopt::Std;
#use strict;
use vars '$opt_b';

getopts('b');

my $input=$ARGV[0];
my $output=">new_file.txt";
my $test=">test.txt";

if($opt_b) {open(TEST, $test);}
open(INFILE, $input);
open(OUTFILE, $output);

$num_factors = 0;
$count = 0;
$triangle = 0;

while ($num_factors < 501){

	$count++;
	$triangle = triangle($count);
	$num_factors = factors($triangle);
	print $triangle.":".$num_factors."\n";
	
}





if($opt_b) {close TEST;}
close INFILE;
close OUTFILE;


#=========================================================#
# Subroutines:
#=========================================================#

sub print_format() {

	print "ERROR: format is \n";
	die "\n";

}

sub triangle(){

	my $num = $_[0];
	my $total = 0;
	
	$total = .5*($num)*($num+1);
	return $total;
}

sub factors(){

	my $num = $_[0];
	my $sqrt = sqrt($num);
	my $factors = 0;
	
	if (int($sqrt)==$sqrt){
		$factors++;
		
		for $i (1..int($sqrt)-1){
			if ($num % $i == 0) {
				$factors = $factors+2;
			}
		}
	} else {	
		for $i (1..int($sqrt)){
			if ($num % $i == 0) {
				$factors = $factors+2;
			}
		}
	}
	return $factors;
}





























close (TEST);
close (INFILE);	
close (OUTFILE);



