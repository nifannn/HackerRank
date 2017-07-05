import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = 0;
        
        while(in.hasNext()){
            num ++;
            String s = in.nextLine();
            System.out.printf("%d %s\n",num, s);
        }
        
    }
}
