from typing import List, Any

from django.db.models import QuerySet

from .models import MenuItem


def get_menu_from_db(menu_name: str) -> QuerySet:
    """Returns menu tree for given menu name.
    :param menu_name: Menu name
    :return: Menu tree for given name as QuerySet.
    """
    return MenuItem.objects.select_related('menu').filter(menu__name=menu_name).order_by('parent__id')


def build_tree(menu_items: QuerySet, active_item: str) -> list:
    """Builds tree from given menu items.
    :param menu_items: Menu items as QuerySet
    :param active_item: Active item url
    :return: Menu tree for given menu items.
    """
    if not menu_items:
        return []

    if not active_item:
        return [{'name': item.name, 'url': item.url} for item in menu_items if item.parent_id is None]

    parents = dict()
    parents = {child.parent_id: [] for child in menu_items if child.parent_id not in parents}

    for item in menu_items:
        parents[item.parent_id].append(item)

    def get_tree_dictionary(item, active_element=None):
        """Recursive function for building tree dictionary."""
        is_active = item.url == active_item
        if is_active:
            active_element = item
        children = [get_tree_dictionary(child, active_element) for child in parents.get(item.id, [])]
        if active_element and item.parent_id == active_element.id:
            is_active = True
        if is_active or any(child['is_active'] for child in children if child) or item.parent_id is None:
            return {
                'name': item.name,
                'url': item.url,
                'children': children,
                'is_active': True
            }

    return [get_tree_dictionary(item) for item in menu_items if item.parent_id is None]
