import collections
import json
try:
    import statistics
except ImportError:
    import backports.statistics as statistics

import bs4
import datadiff
import lxml.html
import regex
import six


INNER_TEXT_TAGS = ['b', 'i', 'u', 'strong', 'br', 'p', 'code', 'big', 'small']
LIST_TAGS = ['ul', 'ol', 'table']

FEATURE_REGEX = regex.compile('([\'"]\w+\.\d{2}[\'"])')
DIFF_REGEX = regex.compile('[+-].*([\'"]\w+\.\d{2}[\'"])', regex.M)

TREE_SIMILARITY_THRESHOLD = 0.8
LIST_SENSITIVITY_THRESHOLD = 0.80


class TagHash(bs4.Tag):
    """
    Holder class for monkey-patching functions.
    """

    def _hash(self, depth):
        # cache the hash depth and string
        if not self._hash_depth or self._hash_depth != depth:
            self._hash = self._tag_hash(depth)
            self._hash_string = json.dumps(self._hash)
            self._hash_depth = depth
        return self._hash

    def _tag_hash(self, depth, level=0):
        if self.children and not level == depth and self.name not in LIST_TAGS:
            children = [tag._tag_hash(depth, level + 1) for tag in self.children or [] if type(tag) == bs4.Tag]
        else:
            children = []
        return {self._feature_hash(): children}

    def _feature_hash(self):
        """
        Create a feature hash for this tag (not children).

        :param tag: BS4 Tag
        :return: string: name.00
        """
        return '{0}.{1}'.format(self.name, ''.join(['1' if x else '0' for x in (
            self.get('id'), self.get('name')
        )]))

    def _tag_hash_compare(self, tag, depth):
        return TagHash._hash_compare(self.hash(depth), tag.hash(depth))

    @staticmethod
    def _hash_compare(hash1, hash2):
        # quickly: if the top-level tag doesn't match, ditch it
        if list(hash1.keys())[0] != list(hash2.keys())[0]:
            return False

        # otherwise, diff it and find differences
        diff = datadiff.diff(hash1, hash2)
        hash1_string = json.dumps(hash1)
        hash2_string = json.dumps(hash2)

        total = len(FEATURE_REGEX.findall(hash1_string)) + len(FEATURE_REGEX.findall(hash2_string))

        score = 0
        for line in str(diff).splitlines():
            if line.lstrip().startswith(('+', '-')):
                if line.lstrip().startswith(('+++', '---')):
                    # it's a diff header line, skip
                    continue
                elif '{' in line and '}' in line:
                    # not a modification
                    # penalise by 2 (parent + children as a group)
                    # and reduce the total by (len)
                    count = len(FEATURE_REGEX.findall(line))
                    score += 2
                    total -= count
                else:
                    # modification, only half a point since it does it twice
                    score += 0.5 * len(FEATURE_REGEX.findall(line))

        res = 1 - (score / total)
        return res >= TREE_SIMILARITY_THRESHOLD

    def _recursive_structure_xpath(self, depth, level=0):
        if self.children and not level == depth:
            children = collections.Counter([
                tag.name for tag in self.children if
                type(tag) == bs4.Tag and tag.name not in LIST_TAGS
            ])
            parts = []
            parts.append('{0}'.format(' and '.join(
                ['count({0})={1}'.format(tag_name, number) for tag_name, number in sorted(children.items())]
            )))
            recurse_children = [tag._recursive_structure_xpath(depth, level + 1) for tag in self.children if
                                type(tag) == bs4.Tag and tag.name not in LIST_TAGS]
            parts.append(' and '.join(
                [child for child in recurse_children if child]
            ))
            children_xpath = ' and '.join([part for part in parts if part])
            if children_xpath:
                children_xpath = '[ {0} ]'.format(children_xpath)
        else:
            children_xpath = ''

        if children_xpath:
            return '{0} {1}'.format(self.name, children_xpath)
        else:
            return ''

    def _structure_xpath(self, depth=None):
        depth = depth or self._hash_depth
        if not self._xpath_depth or self._xpath_depth != depth:
            self._xpath = '// ' + self._recursive_structure_xpath(depth)
            self._xpath_depth = depth
        return self._xpath

    def _tag_sibling_position(self):
        if not self.parent:
            return None

        type_siblings = [
            sibling for sibling in self.parent.children
            if type(sibling) == bs4.Tag and sibling.name == self.name
            ]
        if len(type_siblings) > 1:
            index = 0
            for i, sibling in enumerate(type_siblings):
                if sibling == self:
                    index = i
                    break
            return '{0}[{1}]'.format(self.name, index + 1)
        else:
            return '{0}[1]'.format(self.name)

    def _identifying_xpath(self):
        tag = self
        path_components = []
        while True:
            if tag.get('id'):
                path = '{0}[@id="{1}"]'.format(tag.name, tag.get('id'))
                path_components.append(path)
                break
            elif tag.get('class'):
                class_paths = []
                for cls in tag.get('class'):
                    class_paths.append('contains(@class, "{0}")'.format(cls))
                path = '{0}[{1}]'.format(tag.name, ' and '.join(class_paths))
                path_components.append(path)
                break
            else:
                if tag.parent:
                    path_components.append(tag._tag_sibling_position())
                    tag = tag.parent
                else:
                    path_components.append('{0}'.format(tag.name))
                    break

        xpath = '//' + '/'.join(reversed(path_components))
        return xpath

    def _relative_xpath(self, target):
        tag = self
        path_components = []
        while True:
            if tag == target:
                break
            else:
                if tag.parent:
                    path_components.append(tag._tag_sibling_position())
                    tag = tag.parent
                else:
                    path_components.append('{0}'.format(tag.name))
                    break

        xpath = '/'.join(reversed(path_components))
        return xpath

    def _count(self, depth):
        return self._recursive_count(depth=depth) - 1

    def _recursive_count(self, depth, level=0):
        if depth == level:
            return 1

        count = 1
        if self.children:
            for child in self.children:
                if type(child) == bs4.Tag and child.name not in LIST_TAGS:
                    count += child._recursive_count(depth, level + 1)

        return count or 1

    def _iterate(self, depth=None, dfs=True, skip_first=False, nested=True):
        return TagHash._tag_iterate(self, depth=depth, dfs=dfs, skip_first=skip_first, nested=nested)

    def _is_list(self, depth=None, minimum_tags=None):
        return TagHash._tag_is_list(self, depth=depth)

    @staticmethod
    def _tag_is_list(tag, depth=None):
        children = tag.find_all(True, recursive=False)
        if children:
            # if there's only one child, it's a lot tricker
            # check if it has an identical parent somewhere
            has_identical_parent = [1 if child.has_identical_parent(depth=depth) else 0 for child in children]
            perc = statistics.mean(has_identical_parent)
            if perc >= LIST_SENSITIVITY_THRESHOLD:
                return True
            else:
                return False
        else:
            # there wasn't any children ._.
            return False

    def _has_identical_parent(self, depth=None):
        return TagHash._tag_has_identical_parent(self, depth=depth)

    @staticmethod
    def _tag_has_identical_parent(tag, depth=None):
        node = tag
        while True:
            if node.name == tag.name and node is not tag:
                # compare hashes
                if tag.hash_compare(node, depth=depth):
                    # found an identical parent!
                    return True

            if node.parent:
                node = node.parent
            else:
                return False

    @property
    def _level(self):
        """
        Returns the depth of the tag from the top-level parent.

        :return: int
        """
        return TagHash._tag_level(self)

    @property
    def _inner_text(self):
        """
        Get text inside tag, but not inside children.

        :param tag:
        :return: string: text
        """
        text = ''

        for element in self.children:
            if type(element) == bs4.NavigableString:
                if element.strip():
                    text += ' ' + element
            elif element.name in INNER_TEXT_TAGS:
                if element.string:
                    string = element.string.strip()
                    if string:
                        text += ' ' + string

        # convert it to a str so we're not leaving a reference
        return str(text.strip())

    @property
    def _lxml(self):
        return lxml.html.fromstring(str(self))

    @classmethod
    def _tag_iterate(cls, tag, depth=None, dfs=True, skip_first=False, nested=True):
        """
        Iterate depth-first through children of tag to depth.

        :param tag: Tag to start at
        :param depth: Maximum depth to iterate to
        :param dfs: boolean: depth-first or breadth-first
        :param skipfirst: boolean: skip first element
        :return: bs4.Tag: next node in dfs pre-order
        """
        # add a level to the tag so we can track depth
        tag._hash_level = 0

        # and start off the tree stack with this node
        stack = [tag]
        nodes = []

        # if there's no elements left in the stack, don't continue
        while stack:
            if dfs:
                # get the last element, so we're depth-first
                node = stack.pop()
            else:
                # otherwise get the first, which is breadth-first
                node = stack.pop(0)

            # check the node level
            if depth:
                if node._hash_level >= depth:
                    # if we're already deep enough, skip this node
                    continue

            if not skip_first or node != tag:
                if not nested:
                    if node.is_list(depth=tag._hash_depth):
                        continue
                # nodes.append(node)
                yield node

            # from this node, find all tags (not strings) that are immediate children
            children = node.find_all(True, recursive=False)
            for child in children:
                child._hash_level = node._hash_level + 1

            # in order to go top-down, dfs wants the stack extended in reverse
            if dfs:
                stack.extend(reversed(children))
            else:
                # bfs doesn't, though.
                stack.extend(children)

    @staticmethod
    def _tag_level(tag):
        level = 0
        while True:
            if not tag.parent:
                break
            level += 1
            tag = tag.parent

        return level


def list_difference(a, b):
    count = collections.Counter(a)  # count items in a
    count.subtract(b)  # subtract items that are in b
    diff = []
    for x in a:
        if count[x] > 0:
            count[x] -= 1
            diff.append(x)
    return diff


def patch():
    """
    Patch `bs4.Tag` to include new functionality.

    :return:
    """
    bs4.Tag._feature_hash = six.get_unbound_function(TagHash._feature_hash)
    bs4.Tag._tag_hash = six.get_unbound_function(TagHash._tag_hash)
    bs4.Tag.hash = six.get_unbound_function(TagHash._hash)
    bs4.Tag.hash_compare = six.get_unbound_function(TagHash._tag_hash_compare)

    bs4.Tag._recursive_structure_xpath = six.get_unbound_function(TagHash._recursive_structure_xpath)
    bs4.Tag.structure_xpath = six.get_unbound_function(TagHash._structure_xpath)

    bs4.Tag._tag_sibling_position = six.get_unbound_function(TagHash._tag_sibling_position)
    bs4.Tag.identifying_xpath = six.get_unbound_function(TagHash._identifying_xpath)
    bs4.Tag.relative_xpath = six.get_unbound_function(TagHash._relative_xpath)

    bs4.Tag._recursive_count = six.get_unbound_function(TagHash._recursive_count)
    bs4.Tag.count = six.get_unbound_function(TagHash._count)

    bs4.Tag.lxml = TagHash._lxml
    bs4.Tag.iterate = six.get_unbound_function(TagHash._iterate)
    bs4.Tag.inner_text = TagHash._inner_text
    bs4.Tag.level = TagHash._level
    bs4.Tag.is_list = six.get_unbound_function(TagHash._is_list)
    bs4.Tag.has_identical_parent = six.get_unbound_function(TagHash._has_identical_parent)
