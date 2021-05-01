char* getInterlacedString(int X, int Y, char ch1, char ch2)
{
    int l=X+Y;
    char  *s=malloc(sizeof(char)*l);
    for(int i=0;i<l;i++){
        if(i%2==0 && X>0){ s[i]=ch1; X--;}
        else if(i%2==1 && Y>0){ s[i]=ch2; Y--;}
        else if(X>0) {s[i]=ch1; X--;}
        else{s[i]=ch2; Y--;}
    }
    return s;
    
}
