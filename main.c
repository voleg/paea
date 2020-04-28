# include <stdio.h>

long long int ack(m,n)
  long long int  m, n;
{
  long long int ans;
  if (m == 0) ans = n + 1;
  else if (n == 0 ) ans = ack(m-1, 1);
  else ans = ack(m-1, ack(m, n-1));
  return (ans);
}

long long int main (argc, argv)
     int argc; char ** argv;
{ int i,j;
  for (i=0; i<6 ; i++)
    for (j=0; j<6; j++)

printf ("ackerman (%d, %d) is: %lld\n", i, j, ack(i,j));
}
