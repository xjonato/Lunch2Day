#!/usr/bin/env perl
# "Scratchpad" for testing anything...
# Odd Eivind Ebbesen, 2013-05-14 15:40:24

use strict;
use warnings;

use FindBin;
use Data::Dumper;

use lib "$FindBin::Bin/../lib";
use Lunch2Day::Util;


#print("hej\n");
#my %cfg = (
#   logdir      => '/tmp',
#   verbose     => 1,
#   listen_port => 50666,
#   host        => 'batman.hq.oddware.net',
#   gris        => 'hest',
#);
#Lunch2Day::Util::write_config('/tmp/test.cfg', \%cfg)
#  or print("failed to write config\n");

my $cfg = Lunch2Day::Util::read_config('/tmp/test.cfg') or die("Can't read config");
print(Dumper($cfg));
