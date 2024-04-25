class Solution {
    public int[] solution(int[] num_list) {
        int[] answer;
        int[] result = new int[5];
        answer = num_list;
        for(int i=0; i< answer.length-1; i++){
            for(int j=i+1; j<answer.length;j++){
                if(answer[i]>answer[j]){
                    int tmp = answer[i];
                    answer[i] = answer[j];
                    answer[j] = tmp;
                }
            }
        }
        for(int i=0;i<5;i++){
            result[i] = answer[i];
        }
        
        return result;
    }
}