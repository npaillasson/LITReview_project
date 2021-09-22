from django import template

register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__


@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)


@register.filter()
def type_object(object_to_check):
    if str(type(object_to_check)) == "<class 'review.models.Ticket'>":
        return 'Ticket'
    elif str(type(object_to_check)) == "<class 'review.models.Review'>":
        return 'Review'
    else:
        return str(type(object_to_check))


@register.filter()
def author_name(ticket):
    review = list(ticket.review_set.all())[0]
    review_author = review.user
    return review_author
