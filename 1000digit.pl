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

# while (<INFILE>){

	# chomp;
	# @array=split//;
	# for $i (0..$#array){
		# print OUTFILE $array[$i]."\n";
	# }
# }

for $i (0..4){

	$temp = <INFILE>;
	chomp $temp;
	push @array, $temp;

}

$prev_prod = 0;

while (<INFILE>){

	$prod = $array[0]*$array[1]*$array[2]*$array[3]*$array[4];
	if ($prod > $prev_prod){
		print $prod."\n";
		$prev_prod = $prod;
	}

	for $i (0..3){
		$array[$i]=$array[$i+1];
	}
	$array[4]=$_;

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



