#include<stdio.h>
int main(){
	int a = 89;
	int* ptra = &a;
	printf("The address of a is : %p", &ptra);
	//pritnf("The value of : %zu", &ptra);
	float str = 3e5;
	printf("The following value is a float type %f",str);

	return 0;

}
