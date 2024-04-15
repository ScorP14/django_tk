from django import template
from django.core.paginator import Paginator

register = template.Library()


@register.simple_tag
def get_proper_elided_page_range(pag, number, on_each_side=3, on_ends=2):
    # paginator = Paginator(pag.object_list, pag.per_page)
    paginator = Paginator(range(1000), pag.per_page)
    q = []
    for i in paginator.get_elided_page_range(number=50, on_each_side=on_each_side, on_ends=on_ends):
        q.append(i)

    middle_index = len(q) // 2
    for ind, ch in enumerate(q):
        if ch == paginator.ELLIPSIS:
            if ind < middle_index:
                q[ind] = q[middle_index] // 2
            else:
                q[ind] = (q[-1] + q[middle_index]) // 2
    print(q)
    return paginator.get_elided_page_range(
        number=number,
        on_each_side=on_each_side,
        on_ends=on_ends
    )
