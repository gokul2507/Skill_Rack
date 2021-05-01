char* encloseWordsWithinDoubleQuotes(char S[], char W[])
{
    char *n=(char )malloc(1001*sizeof(char));
    int in=0,i=0;
    while(in<strlen(S)){
        char w[101];
        int wi=0;
        for(int c=in;S[c]!=' '&&S[c];c++){
            w[wi++]=S[c];
        }
        w[wi]='\0';
        if(strcmp(w,W)==0){
            n[i++]='\\"';
            strcat(n,w);
            i+=strlen(w);
            n[i++]='\\"';
        }
        else{
            strcat(n,w);
            i+=strlen(w);
        }
        n[i++]=' ';
        in+=strlen(w)+1;
    }
    n[i]='\0';
    return n;
}
