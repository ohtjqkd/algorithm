import programmers.PickItem;

public class Main {
    public static void main(String[] args) {
        int[][] arr = {{1,1,7,4},{3,2,5,5},{4,3,6,9},{2,6,8,8}};
        PickItem sol = new PickItem();
        sol.solution(arr, 1, 3, 7, 8);
    }
}