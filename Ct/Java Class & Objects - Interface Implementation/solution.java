public class BellKeyBoard implements KeyBoard{
    String a="";
    boolean b;
    public void setCapsLock(boolean da){
        b=da;
    }
    public void type(String str){
       if(b==true){
           a+=str.toUpperCase();
       }
       else{
           a+=str;
       }
    }
    public String getText(){
        return a;
    }
}