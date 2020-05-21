1)Using methods charAt() & length() of String class, write a program to print the frequency of each character in a string. “Hello friend”


import java.util.Scanner;
public class Main
{
public static void main(String[] args) {
int i;
        String str;
     
        int count[] = new int[256];
        Scanner s = new Scanner(System.in);
       
        System.out.print("Enter a String : ");
        str=s.nextLine();
       
         for (i = 0; i < str.length(); i++) {
            count[(int) str.charAt(i)]++;
        }
        for (i = 0; i < 256; i++) {
            if (count[i] != 0) {
                  System.out.println( (char) i  + " : " + count[i]);
            }
        }
}
}
