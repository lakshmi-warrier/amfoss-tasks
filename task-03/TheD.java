import java.io.*;
import java.util.*;

public class Solution 
{

    public static void main(String[] args) 
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=1; i<=n/2+1;i++)
        {
            for(int k=1; k<=n/2+1-i;k++)
                System.out.print("*");
            for(int j=1; j<i*2; j++)
                System.out.print("D");
            for(int k=1; k<=n/2+1-i;k++)
                System.out.print("*");
            
            System.out.println();
        }
         for(int i=n/2; i>0;i--)
         {
            for(int k=n/2+1-i; k>=1; k--)
                System.out.print("*");
            for(int j=i*2-1; j>0; j--)
                System.out.print("D");
            for(int k=n/2+-i; k>=0;k--)
                System.out.print("*");
            System.out.println();
         }
    
    }
}
