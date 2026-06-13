class Solution {
    public boolean isValid(String s){
        Stack <Character> stack = new Stack<>();
        List <Character> items = Arrays.asList('(', '[', '{');

        for (int i = 0; i < s.length(); i++){
            if(items.contains(s.charAt(i))){
                stack.push(s.charAt(i));
            }
            else if(s.charAt(i) == ')' && !stack.empty()){
                if(stack.peek() != '('){
                    return false;
                }
                stack.pop();
            }

            else if(s.charAt(i) == ']' && !stack.empty()){
                if(stack.peek() != '['){
                    return false;
                }
                stack.pop();
            }

            else if(s.charAt(i) == '}' && !stack.empty()){
                if(stack.peek() != '{'){
                    return false;
                }
                stack.pop();
            }
            else {
                return false;
            }
        }

        return stack.empty();
    }
}
