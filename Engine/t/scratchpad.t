#!/usr/bin/env perl
# "Scratchpad" for testing anything...
# Odd Eivind Ebbesen, 2013-05-14 15:40:24

{

   package Lunch2Day::Engine::Util;

   use strict;
   use warnings;
   use 5.016;

   use Carp;

   # NOTE: functional style calling ONLY
   sub merge_named_args {
      # Quite pointless to call this sub w/o args, but as a failsafe just in case,
      # we create empty array/hash refs if no args.
      my $aref = shift || [];
      my $href = shift || {};

      my %args = @{$aref};
      my %opts = %{$href};

      @opts{ keys(%args) } = values(%args);

      return \%opts;
   }

   # NOTE: functional style calling ONLY, if calling from outside this module!
   sub prop {
      # Directly enter and modify callers internal hash.
      my $caller = shift;
      my $k      = shift;
      my $v      = shift;
      if ($k and $v) {
         $caller->{$k} = $v;
         return $caller;    # for easy chaining at assignment
      }
      return $caller->{$k};    # undef if no such key
   }

   # NOTE: functional style calling ONLY
   sub read_config {
      my $file = shift;
      open(my $fh, '<', $file) or carp(qq(Unable to open file "$file" for reading - $!));
      my $rx   = qr/\A\s*(\w+?)\s+(.*)\Z/;    # precompile regex for faster loop exec
      my $href = {};                          # hash of key/value pairs
      while (<$fh>) {
         chomp;
         next unless ($_);
         my ($k, $v) = $_ =~ $rx;
         $href->{$k} = $v if ($k and $v);
      }
      close($fh) or carp($!);
      return $href;
   }

   # NOTE: functional style calling ONLY
   sub write_config {
      my $file = shift || carp("No filename given to write_config()") and return;
      my $href = shift || carp("No data given to write_config()")     and return;
      open(my $fh, '>', $file) or carp(qq(Unable to open file "$file" for writing - $!));
      while (my ($k, $v) = each(%{$href})) {
         print($fh "$k $v\n");
      }
      close($fh) or carp($!);
   }

   1;
}

Lunch2Day::Engine::Util::write_config('/tmp/test.cfg');
