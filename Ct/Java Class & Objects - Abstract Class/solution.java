class AcerLaptop extends Laptop{
    int ram;
    String process,brand;
    AcerLaptop(int a,String b,String c){
        ram=a;
        process=b;
        brand=c;
    }
    public int getRAM(){
        return ram;
    }
    public String getProcessor(){
        return process;
    }
    public String getBrand(){
        return brand;
    }
}