#include<stdio.h>
#include<string.h>
int main(){
    char ar1[10],ar2[10];
    printf("Enter frist string : ");
    fgets(ar1,10,stdin);
    strcpy(ar2,ar1);
    puts(ar2);
}