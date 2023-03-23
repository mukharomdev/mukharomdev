package FileLogger;
# FileLogger.pm

use strict;
use warnings;

my $LEVEL = 1; # default log level

sub open{
   my $logfile = shift;
   # open log file for appending
   open(LFH, '>>', $logfile) or die "cannot open the log file $logfile: $!";
   # write logged time:
   print LFH "Time: ", scalar(localtime), "\n";
}

sub log{
   my($log_level,$log_msg) = @_;
   # append log if the passed log level is lower than
   # the module log level
   if($log_level <= $LEVEL){
      print LFH "$log_msg\n";
   }
}

sub close{
   close LFH;
}

sub set_level{
   # set the log level
   my $log_level = shift;
   # check if the passed log level is a number
   if($log_level =~ /^\d+$/){
      $LEVEL = $log_level;
   }
}

1;