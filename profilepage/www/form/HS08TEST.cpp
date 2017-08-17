#include<iostream>
int main(void)
{
	int x;
	float y;
	scanf("%d",&x);
	scanf("%f",&y);
	if (y-x-0.5>=0 && x%5==0)
	{
		printf("%.2f",y-x-0.5);
	}
	else
		printf("%.2f",y);
}