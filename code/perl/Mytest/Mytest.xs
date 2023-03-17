#define PERL_NO_GET_CONTEXT
#include "EXTERN.h"
#include "perl.h"
#include "XSUB.h"

#include "ppport.h"


MODULE = Mytest		PACKAGE = Mytest		
void
hello()
CODE:
    printf("Hello, world!\n");