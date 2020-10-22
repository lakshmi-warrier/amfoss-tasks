import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        int req_sum = sc.nextInt();
        for(int i=0; i<n; i++)
            arr[i] = sc.nextInt();
        String flag = "False";
        Arrays.sort(arr);
        int leftInd = 0;
        int rightInd = n-1;
        
        while(leftInd<rightInd)
        {
            if (arr[leftInd] + arr[rightInd] < req_sum) leftInd++;
            else if (arr[leftInd]+ arr[rightInd] == req_sum)
            {
                flag = "True";
                break;
            }
            else rightInd--;
        }
        
    
        System.out.println(flag);
    }
}
