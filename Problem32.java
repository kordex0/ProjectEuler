class Problem32{
	public static void main(String args[]){
		int nums[] = new int[1234567];
		int temp = 0;
		for(int i = 1; i < 10000; i++){
			for(int j = i; j < 10000; j++){
				if(isPandigital(i, j)){
					nums[temp] = i*j;
					temp++;
				}
			}
		}
		removeDoubles(nums);
		total(nums);
	}

	static void total(int a[]){
		int sum = 0;
		for(int i = 0; i < a.length; i++){
			sum += a[i];
		}
		System.out.println(sum);
	}

	static void removeDoubles(int a[]){
		int temp;
		for(int i = 0; i < a.length; i++){
			temp = a[i];
			if(temp != 0){
				for(int j = i + 1; j < a.length; j++){
					if(a[j] == temp){
						a[j] = 0;
					}
				}
			}
		}
	}

	static boolean isPandigital(int a, int b){
		int ans = a*b;
		String x = Integer.toString(a);
		String y = Integer.toString(b);
		String z = Integer.toString(ans);
		String full = x + y + z;
		String temp;
		for(int i = 1; i <= 9; i++){
			temp = Integer.toString(i);
			if((full.indexOf(temp) == -1) || !(full.indexOf(temp) == full.lastIndexOf(temp))){
				return false;
			}
		}
		if(full.indexOf("0") != -1){
			return false;
		}
		System.out.println(a + " " + b + " " + ans);
		return true;
	}
}