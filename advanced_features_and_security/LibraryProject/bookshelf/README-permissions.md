# Permissions & Groups Setup

## Custom Permissions Added to Book Model
- can_view
- can_create
- can_edit
- can_delete

## Groups Created
### Viewers
- can_view

### Editors
- can_view
- can_create
- can_edit

### Admins
- can_view
- can_create
- can_edit
- can_delete

## Views Protection
Views are protected using:
@permission_required('<app_label>.<permission>', raise_exception=True)

Examples:
- @permission_required('bookshelf.can_view')
- @permission_required('bookshelf.can_create')
- @permission_required('bookshelf.can_edit')
- @permission_required('bookshelf.can_delete')
