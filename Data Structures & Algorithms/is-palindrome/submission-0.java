class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int a = 0;
        int b = s.length() - 1;

        while (a < b){
            while (a<b && !Character.isLetterOrDigit(s.charAt(a))){
                a += 1;
            }
            while(a<b && !Character.isLetterOrDigit(s.charAt(b))){
                b -= 1;
            }
            if(s.charAt(a) == s.charAt(b)) {
                a += 1;
                b -= 1;
            }
            else {
                return false;
            }
        }
        return true;}
    }
