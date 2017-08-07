import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> l = new ArrayList<>();
        int n = sc.nextInt();
        for(int i=0; i<n; i++){
            l.add(sc.nextInt());
        }
        int q = sc.nextInt();
        for(int i=0; i<q; i++){
            String query = sc.next();
            if(query.equals("Insert")){
                int idx = sc.nextInt();
                int val = sc.nextInt();
                l.add(idx, val);
            }else {
                int idx = sc.nextInt();
                l.remove(idx);
            }
        }
        for(Integer num: l){
            System.out.print(num+" ");
        }
    }
}
