class Solution {
    public int[] solution(int[] num_list, int n) {
        int num = n-1;
        int len = num_list.length-num;
        int[] n_list = new int[len];
        int j = 0;
        for(int i=n-1; i<num_list.length;i++){
            n_list[j] = num_list[i];
            j++;
        }
        return n_list;
    }
}