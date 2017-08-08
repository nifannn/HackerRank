import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        BitSet B1 = new BitSet(N);
        BitSet B2 = new BitSet(N);
        while(M-->0){
            String operation = sc.next();
            int x = sc.nextInt();
            int y = sc.nextInt();
            switch(operation){
                case "AND":
                    if(x == 1){
                        B1.and(B2);
                    }else{
                        B2.and(B1);
                    }
                    break;
                case "SET":
                    if(x == 1){
                        B1.set(y);
                    }else{
                        B2.set(y);
                    }
                    break;
                case "FLIP":
                    if(x == 1){
                        B1.flip(y);
                    }else{
                        B2.flip(y);
                    }
                    break;
                case "OR":
                    if(x == 1){
                        B1.or(B2);
                    }else{
                        B2.or(B1);
                    }
                    break;
                case "XOR":
                    if(x == 1){
                        B1.xor(B2);
                    }else {
                        B2.xor(B1);
                    }
                    break;
                    
            }
            System.out.println(B1.cardinality() + " " + B2.cardinality());
        }
    }
}
