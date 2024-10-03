package programmers;

public class Joystick {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Joystick s = new Joystick();
		System.out.println(s.solution("A"));
	}
		public int solution(String name) {
			int answer = name.length()-1;
			for(int i = 0; i < name.length();i++) {
				if(name.codePointAt(i)-65 <= 13) {
					answer += (name.codePointAt(i)-65);
				} else {
					answer += (91 - name.codePointAt(i));
				}
				
			}
			if(name.length() < 1 && name.charAt(1) == 'A') {
				for(int i = 1; i < name.length(); i++) {
					if(name.charAt(i) == 'A') {
						answer--;
					} else {
						break;
					}
				}
			}
			
			return answer;
		}

}
