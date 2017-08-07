import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = in.nextInt();
        }
        int cnt = 0;
        for(int i=0; i<n; i++){
            for(int j=i; j<n; j++){
                int sum = 0;
                if(i==j){
                    sum = arr[i];
                }else {
                    for(int k=i; k<j+1; k++){
                        sum += arr[k];
                    }
                }
                if(sum<0){
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
}
