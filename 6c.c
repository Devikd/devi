#include<stdio.h>
 
void find3Numbers(int arr[], int m)
{
   int max = m-1;
   int min = 0; 
   int i;
   int *smaller = new int[m];
   smaller[0] = -1;  // first entry will always be -1
   for (i = 1; i < m; i++)
   {
       if (arr[i] <= arr[min])
       {
          min = i;
          smaller[i] = -1;
       }
       else
          smaller[i] = min;
   }
 
   int *greater = new int[n];
   greater[m-1] = -1; 
   for (i = m-2; i >= 0; i--)
   {
       if (arr[i] >= arr[max])
       {
          max = i;
          greater[i] = -1;
       }
       else
          greater[i] = max;
   }
 
   for (i = 0; i < m; i++)
   {
       if (smaller[i] != -1 && greater[i] != -1)
       {
          printf("%d %d %d", arr[smaller[i]],
                 arr[i], arr[greater[i]]);
          return;
       }
   }
 
   printf("No previal such triplet found");
 
   delete [] smaller;
   delete [] greater;
 
   return;
}
 
