import pytest
from k_tree import KTree


def test_tree_repr(small_ktree):
    """Test repr magic method."""
    assert repr(small_ktree) == '<Root Val: 1>'


def test_insert_empty_tree(empty_ktree):
    """Test insert into empty tree."""
    empty_ktree.insert(1, None)
    assert empty_ktree.root.val == 1


def test_insert_small_tree(small_ktree):
    """Test insert into existing tree."""
    small_ktree.insert(15, 3)
    assert small_ktree.root.children[1].children[2].val == 15


def test_insert_failure(small_ktree):
    """Test insert error fires."""
    with pytest.raises(ValueError):
        small_ktree.insert(20, 400)


def test_preorder(small_ktree):
    """Test pre-order traversal."""
    temp = []
    small_ktree.preorder(lambda x: temp.append(x.val))
    assert temp == [1, 2, 3, 5, 6, 7, 4]


def test_preorder_empty(empty_ktree):
    """Test pre-order traversal on empty tree."""
    temp = []
    empty_ktree.preorder(lambda x: temp.append(x.vall))
    assert temp == []


def test_postorder(small_ktree):
    """Test post-order traversal."""
    temp = []
    small_ktree.postorder(lambda x: temp.append(x.val))
    assert temp == [2, 5, 7, 6, 3, 4, 1]


def test_postorder_empty(empty_ktree):
    """Test post-order traversal on empty tree."""
    temp = []
    empty_ktree.postorder(lambda x: temp.append(x.vall))
    assert temp == []


def test_breadth_first(small_ktree):
    """Test breadth-first traversal."""
    temp = []
    small_ktree.breadth_first(lambda x: temp.append(x.val))
    assert temp == [1, 2, 3, 4, 5, 6, 7]


def test_breadth_first_empty(empty_ktree):
    """Test breadth-first traversal."""
    temp = []
    empty_ktree.breadth_first(lambda x: temp.append(x.val))
    assert temp == []
