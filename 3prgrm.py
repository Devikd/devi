#include <stdio.h>
#include<string.h>
int main(void) {
int nn,rev=0,rr;
scanf("%d",&nn);
while(nn!=0)
{
	rr=nn%10;
	rev=rev*10+rr;
	nn=nn/10;
}
printf("%d",rev);
	return 0;
}
