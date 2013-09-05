sub triangle(){

	my $num = $_[0];
	my $total = 0;
	
	$total = .5*($num)*($num+1);
	return $total;
}

sub num_factors(){

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

sub div(){

	my $num = $_[0];
	my $i;
	
	for $i (1..20){
		unless ($num % $i == 0){
			return 0;
		}
	}
	return 1;

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

sub max(){

	$prev = 0;
	for $i (@_){
		if ($i > $prev) {
			$prev = $i;
		} 
	}
	
	return $prev;

}

sub factorial{

	my $num = $_[0];
	my $total = 1;
	
	while($num > 1){
		$total*=$num;
		$num--;
	}
	return $total;

}


sub nCr{

	($n,$r) = @_;
	my $num;
	$num = factorial($n)/(factorial($r)*factorial($n-$r));
	return $num;

}

sub nPr{

	($n,$r) = @_;
	my $num;
	$num = factorial($n)/factorial($n-$r);
	return $num;

}



1;