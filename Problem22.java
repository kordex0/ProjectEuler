import java.io.*;
import java.util.*;
import java.math.*;

public class Problem22{
	public static void main(String args[])throws Exception{
		BigInteger total = BigInteger.valueOf(0);
		Scanner s = new Scanner(new File("names.txt"));
		//s.skip("\",\"");
		String in = s.next();
		String a[] = in.split("\",\"");
		a[0] = "MARY";
		a[5162] = "ALONSO";
		Arrays.sort(a);
		for(int i = 0; i < a.length; i++){
			total = total.add(BigInteger.valueOf(toNum(a[i]) * (i+1)));
		}
		System.out.println(total);
	}

	public static int toNum(String s){
		int total = 0;
		for(int i = 0; i < s.length(); i++){
			if(s.charAt(i) > 64){
				total += s.charAt(i) - 64;
			}
		}
		return total;
	}
}