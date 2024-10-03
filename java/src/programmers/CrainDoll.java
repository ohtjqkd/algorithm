package programmers;

//성공!!!

public class CrainDoll {

	public static void main(String[] args) {
		CrainDoll cd = new CrainDoll();
		int[][] board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
		int[] moves = {1,5,3,5,1,2,1,4};
		System.out.println(cd.solution(board, moves));
		// TODO Auto-generated method stub
	}
	
	public int solution(int[][] board, int[] moves) {
		int[] bucket = new int[20];// new int[board.length * board[0].length];
		int answer = 0;
		
		int maxDept = board.length;
		int bucketTop = 0;
		for(int i = 0; i < moves.length; i++) {
			
			System.out.println(i + "회차 시작");
			int dept = 0;
			int column = moves[i]-1;
			while (dept < maxDept && board[dept][column] == 0) {
				int nextDept = dept+1;
				System.out.println("현재 깊이" + dept + "다음 깊이" + nextDept);
				dept++;
			}
			if(dept == maxDept) {
				System.out.println("비어있음");
				continue;
			}
			for(int n : bucket) {
				System.out.println(n);
			}
			System.out.println("pick up target");
			int target = board[dept][column];
			board[dept][column] = 0;
			System.out.println("target=" + target);
			System.out.println("bucket의 Top = " + bucket[bucketTop]);
			if(bucket[0] != 0 && bucket[bucketTop-1] == target) {
				System.out.println();
				bucket[bucketTop-1] = 0;
				bucketTop--;
				answer += 2;
				continue;
			}
			bucket[bucketTop] = target;
			System.out.println("bucket의" + bucketTop + "에" + target + "을 쌓는다.");
			System.out.println("bucketTop = " + bucket[bucketTop]);
			bucketTop++;
		}
		return answer;
	}

}
