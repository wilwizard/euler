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

print nCr($ARGV[0],$ARGV[1])."\n";



if($opt_b) {close TEST;}
close INFILE;
close OUTFILE;











