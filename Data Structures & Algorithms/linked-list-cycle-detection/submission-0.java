/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        while (head != null) {
            ListNode current = head.next;
            List<ListNode> visited = new ArrayList<>();
            while (current != null && !visited.contains(current)) {
                if(current == head) {
                    return true;
                }
                visited.add (current);
                current = current.next;
            }
            head = head.next;
        }
        return false;
    }
}
