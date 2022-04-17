#include<stdio.h>
#include<string.h>
int main(){
    char ar1[10],ar2[10];
    printf("Enter frist string : ");
    gets(ar1);
    printf("Enter second string : ");
    gets(ar2);
    int i;
    i =strcmp(ar1,ar2);
    if(i == 0)
        printf("String are equal\n");
    else
        printf("String are not equal\n");
}