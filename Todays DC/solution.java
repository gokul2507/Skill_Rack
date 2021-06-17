package com.skillrack;
import java.util.*;
public class BasicCalculator{
    public static int addition(int a,int b){
        return a+b;
    }
    public static int subtraction(int a, int b){
        return a-b;
    }
    public static int multiplication(int a, int b){
        return a*b;
    }
    public static int integerDivision(int a, int b){
        return a/b;
    }
    public static double floatDivision(int a, int b){
        return a/(b*1.0);
    }
    public static int modulo(int a, int b){
        return a%b;
    }
}