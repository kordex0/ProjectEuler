public class Problem19{
	static long day = 1;
	static int total = 0;

	public static void main(String args[]){
		for(int i = 1; i <= 12; i++){
			day += month(i, 1900);
		}

		day = day % 7;

		if(day == 0)
			total++;

		for(int i = 1901; i <= 2000; i++){
			for(int j = 1; j <= 12; j++){
				day += month(j, i);
				day = day % 7;
				if(day == 0)
					total++;
			}
		}
		System.out.println(total);
	}

	public static int month(int a, int year){
		switch(a){
			case 2:
				if(year % 100 == 0){
					if(year % 400 == 0)
						return 29;
				} else {
					if(year % 4 == 0){
						return 29;
					}
				}
				return 28;
			case 4:
			case 6:
			case 9:
			case 11:
				return 30;
			case 1:
			case 3:
			case 5:
			case 7:
			case 8:
			case 10:
			case 12:
				return 31;
		}
		return 0;
	}

}