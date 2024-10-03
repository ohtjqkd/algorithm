package programmers;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;

public class DevelopFunction {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DevelopFunction df = new DevelopFunction();
		int[] progresses = {70, 78, 12, 10, 54, 9};
		int[] speeds =     {3, 6, 11, 8, 2, 4};
		int[] arr = df.solution(progresses, speeds);
		for(int i : arr) {
			System.out.println(i);
		}
	}
	public int[] solution(int[] progresses, int[] speeds) {
		Queue<Integer> qu = new LinkedList<Integer>();
		for(int i = 0; i < progresses.length; i++) {
			qu.add((int) Math.ceil((100-(double)progresses[i])/(double)speeds[i]));
		}
		ArrayList<Integer> arr = new ArrayList<Integer>();
		Iterator quIt = qu.iterator();
		for(int i = 0; i < qu.size(); i++) {
			System.out.println(quIt.next());
		}
		while(qu.size()!=0) {
			int size = 1;
			int tmp = qu.peek();
			qu.poll();
			while(qu.size()!=0) {
				if(tmp >= qu.peek()) {
					qu.poll();
					size++;
				} else {
					break;
				}
			}
			arr.add(size);
		}
		int[] answer = new int[arr.size()];
		for(int i = 0; i < arr.size(); i++) {
			answer[i] = arr.get(i);
		}
		return answer;
	}
}
