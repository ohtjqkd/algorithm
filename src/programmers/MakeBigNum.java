package programmers;

import java.util.*;

public class MakeBigNum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String number = "128405";
		int k = 2;
		MakeBigNum mbn = new MakeBigNum();
		System.out.println(mbn.solution(number, k));
	}
	public String solution (String number, int k) {
		char[] cha = new char[number.length()-k];
		Stack<Character> st = new Stack<Character>();
		for(int i = 0; i < number.length(); i++) {
			char c = number.charAt(i);
			while(!st.isEmpty() && st.peek() < c && k-- > 0) {
				st.pop();
			}
			st.push(c);
		}
		for(int i = 0; i < st.size(); i++) {
			cha[i] = st.get(i);
		}
		return new String(cha);
	}

}
