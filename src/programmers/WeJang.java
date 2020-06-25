package programmers;

import java.*;
import java.util.HashMap;
import java.util.Iterator;
public class WeJang {
	String[][] clothes =  {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
	HashMap<String, String> hclothes = new HashMap<String, String>();
	for(int i = 0; i < clothes.length; i++) {
		hclothes.put(clothes[i][0],clothes[i][1]);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	}

}
