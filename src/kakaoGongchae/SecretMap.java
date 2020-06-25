package kakaoGongchae;

public class SecretMap {

	public static void main(String[] args) {
		int[] arr1 = {9,20,28,18,11};
		int[] arr2 = {30,1,21,17,28};
		SecretMap bo = new SecretMap();
		bo.BinaryOr(arr1, arr2);
		int[] arr3 = {46,33,33,22,31,50};
		int[] arr4 = {27,56,19,14,14,10};
		bo.BinaryOr(arr3, arr4);
	}
	public String BinaryOr(int[] x, int[] y) {
		for(int i = 0; i < x.length; i++) {
			String line = Integer.toBinaryString(x[i] | y[i]);
			for(int j = 0; j < line.length(); j++) {
				if(line.charAt(j) == '1') {
					System.out.print("#");
				} else {
					System.out.print(" ");
				}
			}
			System.out.println();
		}
		return "1";
	}
	
}
