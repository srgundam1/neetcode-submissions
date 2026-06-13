class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> map = new HashMap<>();
        for (char x: s.toCharArray()) {
            if (map.get(x) != null){
                map.put(x, map.get(x) + 1);
            }
            else {
                map.put(x, 1);
            }
        }
        for (char x: t.toCharArray()) {
            if (map.get(x) != null) {
                map.put(x, map.get(x) - 1);
            }
            else {
                return false;
            }
        }
        for (int value: map.values()) {
            if (value != 0) {
                return false;
            }
        }
        return true;
    }
}
