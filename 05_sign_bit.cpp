#include <bits/stdc++.h>
using namespace std;

void bin(long n)
{
  if(n>0){
    cout<<"0";
  }
  else{
    cout<<"1";
  }
	long i;
	for (i = 1 << 30; i > 0; i = i / 2)
	{
	if((n & i) != 0)
	{
		cout << "1";
	}
	else
	{
		cout << "0";
	}
	}
}

int main(void)
{
	bin(-7);
	cout << endl;
	bin(4);
}