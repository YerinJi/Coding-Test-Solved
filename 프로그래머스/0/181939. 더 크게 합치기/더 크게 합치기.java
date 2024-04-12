class Solution {
    public int solution(int a, int b) {
        String tmp1 = Integer.toString(a) + Integer.toString(b);
        String tmp2 = Integer.toString(b) + Integer.toString(a);
        if(Integer.parseInt(tmp1) > Integer.parseInt(tmp2))
            return Integer.parseInt(tmp1);
        else
            return Integer.parseInt(tmp2);
    }
}