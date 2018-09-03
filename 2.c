#include<stdio.h>
int main()
{
	int a[100],n,i,j,k,v,count=0;
	scanf("%d",&n);
	scanf("%d",&k);
	while(n!=0)
	{
		v=n%10;
		a[count]=v;
		count++;
		n=n/10;
	}
	for(i=0;i<count;i++)
	{
		for(j=0;j<count-1;j++)
		{
			if(a[j]>a[j+1])
			{
				v=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
			}
		}
	}
	j=count-k;
	for(i=0;i<j;i++)
	{
		printf("%d",a[i]);
	}
	return 0;
}
