#include<stdio.h>
#include<string.h>
int main(){
    char ar1[10];
    printf("Enter frist string : ");
    //gets(ar1);
    fgets(ar1,10,stdin);
    int i;
    i = strlen(ar1);
    printf("The length of String is %d.",i);
}