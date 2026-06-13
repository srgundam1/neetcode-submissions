class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char i: s.toCharArray()) {
            if (i == '}') {
                if (!stack.isEmpty() && stack.peek() == '{'){
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else if (i == ']'){
                if (!stack.isEmpty() && stack.peek() == '['){
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else if (i == ')'){
                if (!stack.isEmpty() && stack.peek() == '('){
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else {stack.push(i);}
        }
        return stack.isEmpty();
    }
}
