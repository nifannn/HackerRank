import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        smallest = s.substring(0,k);
        largest = s.substring(0,k);
        
        if(k<s.length()){
            for(int i=1; i<=s.length()-k; i++){
            String sub = s.substring(i,i+k);
            if(s.substring(i,i+k).compareTo(smallest)<0){
                smallest = s.substring(i,i+k);
            }
            if(s.substring(i,i+k).compareTo(largest)>0){
                largest = s.substring(i,i+k);
            }
        }
        }
        
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
