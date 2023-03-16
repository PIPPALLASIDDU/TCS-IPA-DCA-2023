import java.util.*; 
public class MyClass{ 
    public static void main(String[] args){ 
        Scanner in=new Scanner(System.in); 
        int[] arr=new int[5]; 
        int cnt=0; 
        for (int i=0;i<5;i++){
            arr[i]=in.nextInt();
        }
        int l=in.nextInt();
        int u=in.nextInt();
        for (int i=0;i<5;i++){
            if(arr[i]>l && arr[i]<u){ 
            sm+=arr[i]; 
            cnt+=1;
        }
        } 
            
     } 
     System.out.println(sm/cnt); 
     } 
     