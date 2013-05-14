# Odd Eivind Ebbesen, 2013-05-14 23:23:05

package Lunch2Day::Engine::Server;

use base qw(Net::Server::Multiplex);

use 5.016;
use strict;
use warnings;

use Carp;

use constant DEFAULT_PORT => 0x0DDEE;   # 56814

our $VERSION = '2013-05-14';


sub new {
   return bless(
      Lunch2Day::Util::merge_named_args(
         \@,
         {  port     => DEFAULT_PORT,
            bullshit => 'something',
         }
      ),
      shift # yes please, keep the intermediate vars away...
   );
}

#---
# overridden methods

#sub mux_connection {
#   my $self = shift;
#   my $mux  = shift;
#   my $fh   = shift;
#}

sub mux_connection {
   my $self   = shift;
   my $mux    = shift;
   my $fh     = shift;
   my $in_ref = shift;    # scalar ref to input, remember to $$deref

   while ($$in_ref =~ s/\A(.*?)\r?\n//) {
      my $arg = $1;
      next unless ($arg);
   }
}

1;
__END__
