class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] a = new int[n];
        int[] b = new int[n];
        int[] answer = new int[nums.length];

        for(int i = 0;i < n; i++){
            a[i] = nums[i];
            b[i] = nums[i + n];
        }
        int x = 0;
        for(int i = 0; i < n; i++){
            answer[x] = a[i];
            answer[++x] = b[i];
            x++;
        }

        return answer;
    }
}