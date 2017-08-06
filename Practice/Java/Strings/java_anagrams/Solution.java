import java.io.*;
import java.util.*;

public class Solution {
    static boolean isAnagram(String a, String b) {
        HashMap<Character, Integer> cnt_a = new HashMap<>();
        HashMap<Character, Integer> cnt_b = new HashMap<>();
        for(char c: a.toUpperCase().toCharArray()){
            if(cnt_a.containsKey(c)){
                cnt_a.put(c, cnt_a.get(c)+1);
            }else {
                cnt_a.put(c, 1);
            }
        }
        for(char c: b.toUpperCase().toCharArray()){
            if(cnt_b.containsKey(c)){
                cnt_b.put(c, cnt_b.get(c)+1);
            }else {
                cnt_b.put(c, 1);
            }
        }
        return cnt_a.equals(cnt_b);
    }
    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}


