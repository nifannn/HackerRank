import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        @SuppressWarnings("unchecked")
        ArrayList[] set = new ArrayList[n];
        for(int i=0; i<n; i++){
            int d = in.nextInt();
            ArrayList al = new ArrayList();
            if(d > 0){
                for(int k=0; k<d; k++){
                    al.add(in.nextInt());
                }
            }
            set[i] = al;
        }
        int q = in.nextInt();
        for(int i=0; i<q; i++){
            int x = in.nextInt();
            int y = in.nextInt();
            try{
                System.out.println(set[x-1].get(y-1));
            }catch(Exception e){
                System.out.println("ERROR!");
            }
        }
    }
}
