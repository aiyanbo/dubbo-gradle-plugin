import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Objects;


public class SearchTree {

    @Test
    void testCase1() {
        final Node node = new Node();
        node.value = 2;
        final Node left = new Node();
        left.value = 1;
        node.left = left;
        final Node right = new Node();
        right.value = 3;
        node.right = right;

        boolean result = isVaildTree(node);
        Assertions.assertTrue(result);
    }

    @Test
    void testCase2() {
        final Node root = new Node();
    }


    private boolean isVaildTree(final Node node) {
        if (Objects.isNull(node.left) && Objects.isNull(node.right)) {
            return true;
        }
        if (Objects.nonNull(node.left) && Objects.nonNull(node.right)) {
            if (node.left.value < node.value && node.right.value > node.value) {
                return isVaildTree(node.left) && isVaildTree(node.right);
            } else {
                return false;
            }
        } else if (Objects.nonNull(node.left)) {
            return isVaildTree(node.left);
        } else {
            return isVaildTree(node.right);
        }
    }

    private static class Node {
        private int value;
        private Node left;
        private Node right;

    }
}


