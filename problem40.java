class problem40{
	public static void main(String args[]){
		String ans = asdf(250000);
		System.out.println(ans.length());
		System.out.println(ans.charAt(0) + " " + ans.charAt(9) + " " + ans.charAt(99) + " " + ans.charAt(999) + " " + ans.charAt(9999) + " " + ans.charAt(99999) + " " + ans.charAt(999999));
	}

	public static String asdf(int n){
		String temp = "";
		for(int i = 1; i <= n; i++){
			temp += Integer.toString(i);
		}
		return temp;
	}
}