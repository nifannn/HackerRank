import java.io.*;
import java.util.*;
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        s = s.trim();
        if(s.length()==0){
            System.out.println(0);
        }else{
        String delims = "[ !,?._'@]+";
        String[] tokens = s.split(delims);
        System.out.println(tokens.length);
        for(String str: tokens){
            System.out.println(str);
        }}
        scan.close();
    }
}
