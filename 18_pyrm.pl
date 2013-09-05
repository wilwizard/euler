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


@pyram = ();

while (<INFILE>){
	chomp;
	push @pyram,[split /\s+/];
}
	
for $i (0..2**14-1){

	$total = 0;
	$count = 0;
	$bin=sprintf ("%b", $i);
	@turns = split(//,
	
	$bin);
	
	
	$temp = pop @turns;
	$total = 
	
}

	
	




if($opt_b) {close TEST;}
close INFILE;
close OUTFILE;





