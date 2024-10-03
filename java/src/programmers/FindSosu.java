package programmers;
import java.util.HashMap;
import java.util.Iterator;
import java.util.HashSet;
public class FindSosu {
	public static void main(String[] args) {
		String numbers = "17";
		FindSosu mfs = new FindSosu();
		System.out.println(mfs.solution(numbers));
	}
	public int solution(String numbers) {
		int answer = 0;
		HashSet<Integer> hs = new HashSet<Integer>();
		int[] arr = new int[numbers.length()];
		for(int i = 0; i < numbers.length(); i++) {
			arr[i] = Integer.parseInt(numbers.charAt(i)+"");
		}
		int[] output = new int[numbers.length()];
		boolean[] visited = new boolean[numbers.length()];
		FindSosu fs = new FindSosu();
		fs.perm(hs, arr, output, visited, 0, numbers.length(), numbers.length());
		Iterator<Integer> it = hs.iterator();
		System.out.println("Size of hashset: " + hs.size());
		while(it.hasNext()) {
			int div = Integer.parseInt(it.next().toString());
			System.out.println("Result Number: " + div);
			for(int i = 2; i <= div/2; i++) {
				if(div == 2) {
					answer++;
					break;
				}
				System.out.println("나누는 숫자: " + i);
				if(div % i == 0) {
					System.out.println(div +" / " + i);
					System.out.println("break");
					break;
				}
				if(i == (int) Math.floor(div/2)) {
					System.out.println(div + "of middle: " + i);
					answer++;
					System.out.println("answer: " + answer);
					break;
				}
			}
		}
		return answer;
	}
	public void perm(HashSet<Integer> hs, int[] arr, int[] output, boolean[] visited, int depth, int n, int r) {
        if(depth == r) {
        	String ele = "";
        	for(int i = 0; i < r; i++) {
        		ele += output[i];
        		hs.add(Integer.parseInt(ele));
        	}
        	return;
        }
 
        for(int i=0; i<n; i++) {
            if(visited[i] != true) {
                visited[i] = true;
                output[depth] = arr[i];
                perm(hs, arr, output, visited, depth+1, n, r);       
//                output[depth] = 0; // 이 줄은 없어도 됨
                visited[i] = false;
            }
        }
    }
}
