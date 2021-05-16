#include<stdio.h>
struct combi{ 
    int person1,person2;
};
int num_people,combinations;
int max=0,stack[50],top=0;
int findmygang(int key,int *a,struct combi *possible){
int count=1,i,k=0;
a[key-1]=1;
while(k<num_people){
    for(i=0;i<combinations;i++){    
        if(possible[i].person1==key && possible[i].person2==key)
        {
            continue;
        }else if(possible[i].person1==key){
            if(a[possible[i].person2-1]!=1){                
                a[possible[i].person2-1]=1;                
                stack[top++]=possible[i].person2;              
                count++;
            }
        }
        else if(possible[i].person2==key){  
            if(a[possible[i].person1-1]!=1){                
                a[possible[i].person1-1]=1;                
                stack[top++]=possible[i].person1;              
                count++;
            }
        }
    }
    if(top!=0){
        key=stack[top-1];
        top--;
    }
    else{
        break;
    }
    k++;
}
return count;
}
int main()
{
    scanf("%d%d",&num_people,&combinations);    
    int i,a[num_people],t_result; 
    struct combi possible[combinations];
    for(i=0;i<combinations;i++){        
        scanf("%d%d",&possible[i].person1,&possible[i].person2);
    }
    for(i=0;i<num_people;i++)
    a[i]=0;    
    i=0;    
    while(i<num_people){        
        if(a[i]==0){    
            t_result=findmygang(i+1,a,possible);
            if(max<t_result)        
            max=t_result; 
        }
        i++;
    }
    printf("%d",max);
    return 0;
}
