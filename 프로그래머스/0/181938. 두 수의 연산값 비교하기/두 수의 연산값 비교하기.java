class Solution {
    public int solution(int a, int b) {
        String aa = String.valueOf(a);
        String bb = String.valueOf(b);
        int aabb = Integer.valueOf(aa+bb);
        if(aabb>(2*a*b))
            return aabb;
        else
            return 2*a*b;
    }
}