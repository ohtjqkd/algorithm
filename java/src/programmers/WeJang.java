package programmers;

import java.util.HashMap;
import java.util.Iterator;
public class WeJang {
	public int solution() {
		String[][] clothes =  {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
		HashMap<String, String> hclothes = new HashMap<String, String>();
		for(int i = 0; i < clothes.length; i++) {
			hclothes.put(clothes[i][0],clothes[i][1]);
		}
		return 0;
	}
}
