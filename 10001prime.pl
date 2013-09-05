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


my $num=1;
my $prime=0;

until($prime==10001){

	$num++;
	if(is_prime($num)){
		$prime++;
		print OUTFILE $num.":".$prime."\n";
	}

	

}
print $num."\n";


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


sub is_pala(){

	$number = join("",@_);
	$temp = 0;
	if (($_[0]==$_[6])&&($_[1]==$_[5])&&($_[2]==$_[4])){
		print @_;
		$temp = is_prime($number);
		if($temp){
			print":prime";
		}
		print "\n";
		return $temp;
	} else { 
		return 0;
	}

}

sub is_prime(){

	$num = $_[0];
	$div = int(sqrt($_[0]))+1;
	 
	$i = 2;
	while ($i < $div){
		if ($num % $i == 0) {
			return 0;
			last;
		} else {
			$i++;
		}
	}
	return 1;
}






























close (TEST);
close (INFILE);	
close (OUTFILE);



