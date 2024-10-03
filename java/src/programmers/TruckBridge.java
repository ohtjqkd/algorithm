package programmers;
import java.util.LinkedList;
import java.util.Queue;

public class TruckBridge {

	public void test(String[] args) {
		// TODO Auto-generated method stub
		TruckBridge tb = new TruckBridge();
		int bridge_length = 2;
		int weight = 10;
		int[] truck_weights = {7,4,5,6};
		
		System.out.println(tb.solution(bridge_length, weight, truck_weights));
	}
	public int solution(int bridge_length, int weight, int[] truck_weights) {
		//성공!
		Queue<Integer> trucks = new LinkedList<Integer>();
		Queue<Integer> bridge = new LinkedList<Integer>();

        
        int time = 0;
        for(int truck : truck_weights){
            trucks.add(truck);
            System.out.println(truck);
        }
        for(int i = 0; i < bridge_length; i++){
            bridge.add(0);
        }
        int totalWeight = 0;
        int j = 0;
        while(!(trucks.isEmpty()&&totalWeight==0)){
        	System.out.println(j++ + "circles");
        	System.out.println("trucks is empty?" + trucks.isEmpty());
        	totalWeight -= bridge.peek();
            bridge.remove();
 
            System.out.println("On bridge weight = " + totalWeight);
            if( trucks.peek() != null && (totalWeight + trucks.peek()) <= weight ) {
            	System.out.println("trucks's first element = "+trucks.peek());
            	totalWeight += trucks.peek(); 
                bridge.add(trucks.poll());
            } else {
                bridge.add(0);
            }
            time += 1;
            System.out.println("after 1 second weight = " + totalWeight );
            System.out.println("time = " + time + "\n");
        }
        return time;
	}
}
		
		
//		Queue<Truck> trucks = new LinkedList();
//		Queue<Truck> ingTruck = new LinkedList();
//		for(int w:truck_weights) {
//			Truck truck = new Truck();
//			truck.weight = w;
//			truck.position = 0;
//			trucks.add(truck);
//		}
//		int sec = 0;
//		while(!trucks.isEmpty()||!ingTruck.isEmpty()) {
//			sec++;
//			int sum = 0;
//			Truck doneTruck = null;
//			for(Truck truck:ingTruck) {
//				sum += truck.weight;
//				truck.position++;
//				if(truck.position > bridge_length) {
//					doneTruck = truck;
//				}
//			}
//			if(doneTruck != null) {
//				sum -= doneTruck.weight;
//				ingTruck.remove(doneTruck);
//			}
//			if(!trucks.isEmpty() && (ingTruck.size() < bridge_length)) {
//				Truck truck = trucks.peek();
//				if(truck.weight + sum <= weight) {
//					trucks.remove(truck);
//					ingTruck.add(truck);
//					truck.position++;
//				}
//			}
//		}
//		return sec;
//	}
//	private class Truck {
//		int weight;
//		int position;
//	}

