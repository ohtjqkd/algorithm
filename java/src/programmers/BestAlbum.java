package programmers;

import java.util.*;
import java.util.*;
public class BestAlbum {
	
	public static void main(String[] args) {
		String[] genres = {"classic", "pop", "classic", "classic", "pop"};
		int[] plays = {500, 600, 150, 800, 2500};
		// TODO Auto-generated method stub
		HashMap<String, ArrayList<Integer>> play = new BestAlbum().sumPlay(genres, plays);
		System.out.println(play.get(genres[0]));
	}
    public HashMap<String, ArrayList<Integer>> sumPlay (String[] genres, int[] plays){
    	HashMap<String, ArrayList<Integer>> hashMap = new HashMap<String, ArrayList<Integer>>();
    	for(int i = 0; i < genres.length; i++) {
    		if(hashMap.get(genres[i]) == null) {
    			hashMap.put(genres[i], new ArrayList<Integer>());
    			hashMap.get(genres[i]).add(plays[i]);
    			hashMap.get(genres[i]).add(i);
    			hashMap.get(genres[i]).add(plays[i]);
    		} else {
    			hashMap.get(genres[i]).set(0, hashMap.get(genres[i]).get(0) + plays[i]);
    			hashMap.get(genres[i]).add(i);
    			hashMap.get(genres[i]).add(plays[i]);
    		}
    	}
    	System.out.println(hashMap.values());
        return hashMap;
    }

}
