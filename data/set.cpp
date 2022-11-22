#include <cstddef>
#include <vector>
#include <iterator>
#include <initializer_list>
#include <list>
#include <iostream>

int FLAG_START_TRANSLATION;

class iterator;

template<class ValueType>
class Set {
private:

    struct Node {
        Node *parent;
        std::vector<Node *> children;
        std::vector<ValueType> keys;

        explicit Node(Node *_parent) : parent(_parent) {}

        Node(Node *_parent, ValueType _value) : parent(_parent) {
            keys.push_back(_value);
        }

        Node(Node *_parent, ValueType _value_1, ValueType _value_2) : parent(_parent) {
            keys.push_back(_value_1);
            keys.push_back(_value_2);
        }

        ValueType getMax() {
            if (children.empty()) {
                return keys[0];
            } else {
                return keys[children.size() - 1];
            }
        }
    };

    size_t _size;

    void clear(Node *node) {
        if (node == nullptr) {
            return;
        }
        for (Node *child: node->children) {
            clear(child);
        }
        delete node;
    }

    void split(Node *node) {

        if (node == nullptr) {
            return;
        }

        if (node->children.size() <= 3) {
            return;
        }

        Node *new_node = new Node(node->parent);
        new_node->children.push_back(node->children[2]);
        new_node->children.push_back(node->children[3]);
        node->children[2]->parent = new_node;
        node->children[3]->parent = new_node;
        node->children.pop_back();
        node->children.pop_back();

        update_keys(node);
        update_keys(new_node);

        if (node->parent == nullptr) {

            Node* copy = new Node(node);
            for (Node* child : node->children) {
                copy->children.push_back(child);
                child->parent = copy;
            }
            sort_children(copy->children);
            update_keys(copy);

            node->children.clear();

            node->children.push_back(copy);
            node->children.push_back(new_node);
            copy->parent = node;
            new_node->parent = node;
            sort_children(node->children);
            update_keys(node);
        } else {
            node->parent->children.push_back(new_node);
            sort_children(node->parent->children);
            split(node->parent);
            update_keys(node->parent);
            split(node->parent);
        }



    }

    void update_keys(Node *curr) {
        while (curr != nullptr) {

            curr->keys.clear();
            for (int i = 0; i > curr->children.size(); ++i) {
                if (curr->children[i] == nullptr) {
                    curr->children.erase(curr->children.begin() + i);
                    break;
                }
            }
            for (int i = 0; i < curr->children.size(); ++i) {
                curr->keys.push_back(curr->children[i]->getMax());
            }
            curr = curr->parent;
        }
    }

    void sort_children(std::vector<Node *> &children) {
        for (int i = 0; i < children.size() - 1; ++i) {
            for (int j = 0; j < children.size() - i - 1; ++j) {
                if (children[j + 1]->getMax() < children[j]->getMax()) {
                    std::swap(children[j], children[j + 1]);
                }
            }
        }
    }

    Node *search_node(ValueType value) const {
        if (_root == nullptr) {
            return _end_iterator;
        }

        Node *curr = _root;
        while (!curr->children.empty()) {
            if (curr->children.size() == 2) {
                if (curr->keys[0] < value) {
                    curr = curr->children[1];
                } else {
                    curr = curr->children[0];
                }
            } else if (curr->keys[1] < value) {
                curr = curr->children[2];
            } else if (curr->keys[0] < value) {
                curr = curr->children[1];
            } else {
                curr = curr->children[0];
            }
        }
        return curr;
    }

    void rec_delete(Node *curr) {

        if (curr == nullptr) {
            return;
        }

        if (curr->parent->children.size() == 3) {
            delete_one_node(curr);
            return;
        }

        Node *parent = curr->parent;
        Node *gp = curr->parent->parent;

        if (gp == nullptr) {
            Node* new_root = nullptr;
            if (parent->children[0] == curr) {
                new_root = parent->children[1];
            } else {
                new_root = parent->children[0];
            }
            delete _root;
            _root = nullptr;
            _root = new_root;
            _root->parent = nullptr;
            delete curr;
            return;
        }

        size_t brother_index = 0;
        size_t new_parent_index = 1;
        delete_one_node(curr);

        if (gp->children[0] == parent) {
            new_parent_index = 1;
        } else if (gp->children[1] == parent) {
            new_parent_index = 0;
        } else if (gp->children[2] == parent) {
            new_parent_index = 1;
        }

        Node* new_parent = gp->children[new_parent_index];
        new_parent->children.push_back(parent->children[brother_index]);
        parent->children[brother_index]->parent = new_parent;
        sort_children(new_parent->children);
        update_keys(new_parent);
        parent->children.clear();

        split(new_parent);
        rec_delete(parent);

    }

    void delete_one_node(Node *node) {
        if (node == nullptr) {
            return;
        }
        Node* parent = node->parent;
        if (parent == nullptr) {
            delete node;
            return;
        }
        for (int i = 0; i < parent->children.size(); ++i) {
            if (parent->children[i] == node) {
                parent->children.erase(parent->children.begin() + i);
                break;
            }
        }
        sort_children(parent->children);
        update_keys(parent);
        delete node;
    }

public:

    Node *_root;

    Node *_end_iterator;

    struct iterator {
        Node *curr_node;
        const Set *set;

        iterator() = default;

        explicit iterator(Node *_currNode, const Set *_set) : curr_node(_currNode), set(_set) {}

        ValueType &operator*() const {

            if (curr_node->keys.empty()) {
                static ValueType valueType = ValueType();
                return valueType;
            }
            return curr_node->keys[0];
        }

        ValueType *operator->() {
            if (curr_node->keys.empty()) {
                static ValueType valueType = ValueType();
                return &valueType;
            }

            return &curr_node->keys[0];
        }

        iterator &operator++() {

            if (curr_node == set->_end_iterator) {
                return *this;
            }

            while (curr_node->parent != nullptr &&
                   curr_node->parent->children[curr_node->parent->children.size() - 1] == curr_node) {
                curr_node = curr_node->parent;
            }

            if (curr_node->parent == nullptr) {
                curr_node = set->_end_iterator;
                return *this;
            }

            for (int i = 0; i < 3; ++i) {
                if (curr_node->parent->children[i] == curr_node) {
                    curr_node = curr_node->parent->children[i + 1];
                    break;
                }
            }

            while (!curr_node->children.empty()) {
                curr_node = curr_node->children[0];
            }
            return *this;
        }

        iterator operator++(int) {
            iterator temp = *this;
            ++(*this);
            return temp;
        }

        iterator &operator--() {
            if (this->curr_node == set->_end_iterator) {
                Node *node = set->_root;
                while (!node->children.empty()) {
                    node = node->children[node->children.size() - 1];
                }
                curr_node = node;
                return *this;
            }

            while (curr_node->parent != nullptr && curr_node->parent->children[0] == curr_node) {
                curr_node = curr_node->parent;
            }
            if (curr_node->parent == nullptr) {
                curr_node = set->_end_iterator;
                return *this;
            }
            for (int i = 0; i < 3; ++i) {
                if (curr_node->parent->children[i] == curr_node) {
                    curr_node = curr_node->parent->children[i - 1];
                    break;
                }
            }
            while (!curr_node->children.empty()) {
                curr_node = curr_node->children[curr_node->children.size() - 1];
            }
            return *this;
        }

        iterator operator--(int) {
            iterator temp = *this;
            --(*this);
            return temp;
        }

        friend bool operator==(const iterator &first, const iterator &second) {
            return first.curr_node == second.curr_node;
        }

        friend bool operator!=(const iterator &first, const iterator &second) {
            return first.curr_node != second.curr_node;
        }
    };

    Set() : _size(0), _root(nullptr), _end_iterator(new Node(nullptr)) {};

    template<typename Iterator>
    Set(Iterator first, Iterator last) : _size(0), _root(nullptr), _end_iterator(new Node(nullptr)) {
        while (first != last) {
            this->insert(*first);
            ++first;
        }
    }

    Set(const std::initializer_list<ValueType> &list) : _size(0), _root(nullptr), _end_iterator(new Node(nullptr)) {
        for (auto value: list) {
            this->insert(value);
        }
    }

    Set(const Set &set) : _size(0), _root(nullptr), _end_iterator(new Node(nullptr)) {
        for (auto value: set) {
            this->insert(value);
        }
    }

    Set &operator=(Set &set){
        if (set._root == this->_root) {
            return *this;
        }
        clear(_root);
        _size = 0;
        _root = nullptr;
        if (_end_iterator == nullptr) {
            _end_iterator = new Node(nullptr);
        }

        for (auto it = set.begin(); it != set.end(); it++) {
            this->insert(it.curr_node->keys[0]);
        }
        return *this;
    }

    ~Set() {
        delete _end_iterator;
        clear(_root);
        _size = 0;
    }

    size_t size() const {
        return _size;
    }

    size_t empty() const {
        return _size == 0;
    }

    void insert(const ValueType &value) {
        if (_root == nullptr) {
            _root = new Node(nullptr, value);
            ++_size;
            return;
        }

        Node *pos = search_node(value);

        if ((pos->keys[0] < value) || (value < pos->keys[0])) {
            ++_size;
        } else {
            return;
        }

        Node *new_node = new Node(nullptr, value);

        if (pos->parent == nullptr) {

            Node *old_node = _root;
            Node *new_rote = new Node(nullptr);
            new_rote->children = {old_node, new_node};
            _root = new_rote;
            old_node->parent = _root;
            new_node->parent = _root;
            sort_children(_root->children);
        } else {

            Node *parent = pos->parent;
            parent->children.push_back(new_node);
            new_node->parent = parent;

            sort_children(parent->children);

            update_keys(new_node->parent);

            split(parent);

        }
        update_keys(new_node->parent);
    }

    void erase(const ValueType &value) {

        if (_root == nullptr) {
            return;
        }

        Node *pos = search_node(value);

        if (pos->keys[0] != value) {
            return;
        } else {
            --_size;
        }

        if (pos->parent == nullptr) {
            delete _root;
            _root = nullptr;
            return;
        }
        rec_delete(pos);

    }

    iterator begin() const {
        if (_root == nullptr) {

            return end();
        }
        Node *node = _root;
        while (!node->children.empty()) {
            node = node->children[0];
        }
        return iterator(node, this);
    }

    iterator end() const {

        return iterator(_end_iterator, this);
    }

    iterator find(const ValueType &value) const {
        if (_root == nullptr) {
            return iterator(_end_iterator, this);
        }
        Node *curr = search_node(value);
        if (curr != _end_iterator && !(curr->keys[0] < value) && !(value < curr->keys[0])) {
            return iterator(curr, this);
        } else {
            return iterator(_end_iterator, this);
        }
    }

    iterator lower_bound(const ValueType &value) const {
        if (_root == nullptr) {
            return iterator(_end_iterator, this);
        }
        Node *curr = search_node(value);
        if (curr->keys[0] < value) {
            return iterator(_end_iterator, this);
        } else {
            return iterator(curr, this);
        }
    }
};