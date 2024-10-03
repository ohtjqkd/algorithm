package programmers;
import java.util.*;
public class FindBigNum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] input = {0,0,0,0,0};
		String str1 = "6";
		String str2 = "61";
		int hash1 = "6".hashCode();
		int hash2 = "10".hashCode();
		boolean bool = "62".hashCode() > "621".hashCode();
		System.out.println(hash1);
		System.out.println(hash2);
		System.out.println(str1.compareTo(str2));
		FindBigNum fbn =  new FindBigNum();
		System.out.println(fbn.solution(input));
	}
	public String solution(int[] numbers) {
		String answer = "";
		ArrayList<String> arr = new ArrayList<String>();
		for(int i = 0; i < numbers.length; i++) {
			arr.add(String.valueOf(numbers[i]));
		}
		arr.sort(new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				// TODO Auto-generated method stub
				return (o2+o1).compareTo(o1+o2);
			}
		});
		if(arr.get(0).equals("0")) return "0";
		StringBuffer sb = new StringBuffer();
		for(int i = 0; i < arr.size(); i++) {
			sb.append(arr.get(i));
		}
		
		return sb.toString();
	}
}	
//	**해결은 가능하지만 비효율적인 코딩**
//	public String solution(int[] numbers) {
//		String answer = "";
//		for(int i = 0; i < numbers.length-1; i++) {
//			for(int j = i + 1; j < numbers.length; j++) {
//				String str1 = nToStr(numbers);
//				int tmp = numbers[i];
//				numbers[i] = numbers[j];
//				numbers[j] = tmp;
//				String str2 = nToStr(numbers);
//				if(str1.compareTo(str2)>0) {
//					tmp = numbers[i];
//					numbers[i] = numbers[j];
//					numbers[j] = tmp;
//				}
//			}
//		}
//		
//		return nToStr(numbers);
//	}
//	public static String nToStr(int[] numbers) {
//		StringBuffer sb = new StringBuffer();
//		for(int i:numbers) {
//			sb.append(i);
//		}
//		return sb.toString();
//		
//	}
