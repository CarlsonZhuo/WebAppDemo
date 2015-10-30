# Django Code Book

- django form:
https://docs.djangoproject.com/en/1.8/topics/forms/
- django send mail:
https://docs.djangoproject.com/en/1.8/topics/email/
- customize django action:
https://godjango.com/78-custom-django-admin-actions/
- django {% blocktrans %}:
https://docs.djangoproject.com/en/1.8/topics/i18n/translation/#std:templatetag-blocktrans
- django command:
https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/
- django queryset:
http://blog.amir.rachum.com/blog/2013/07/13/django-querysets-fucking-awesome-yes/
- django tag and templates:
https://docs.djangoproject.com/en/1.8/ref/templates/builtins/
- django signal receiver:
https://docs.djangoproject.com/en/1.8/topics/signals/#receiver-functions

---------------------------------------------

#### Django Model Form

> What is the invoke procedure of django model form?

```python
''' 1.'''
def init(self, *args```, **kwargs):
  super(TheFormClass, self).__init__(*args, **kwargs)
  # do sth. Nothing to return

''' 2 when is_valid() is called, or clean() is called'''
def clean_dataName(self):
  # do something to 'clean' dataName
  # the return value is a data value
  return dataName

def clean(self):
  cleaned_data = super(TheFormClass, self).clean()
  # all clean_dataField functions have invoked. Do sth
  # the return value is a dict
  return cleaned_data

''' 3, when save() is called '''
def save(self, commit=True):
  # not yet studied
```

> How to find the not cleaned data in the form?

```python
i_am_a_form['data_field'].value()
# not yet find a way to insert value directly into form
```

> How to create ModelForm from model?

Just use `class meta()`

> What do you mean by bind data?

Django ModelForm is valid only after it is bind with a model object.

Then it changes from a ModelForm object to a BoundForm object.

The `clean()` method and so on can only apply to BoundForm objects.

>How can I change a Django form field value before saving?

http://stackoverflow.com/questions/8924993/how-can-i-change-a-django-form-field-value-before-saving


--------------------------------------------

#### Django Admin

> The property fields of Django Admin

```python
class Clientadmin(admin.ModelAdmin):
  list_filter = (ModeFilter,
                 'rewardsapp_active',
                 'referralsapp_active',
                 'fansapp_active',
                 'is_bigcommerce',
                 'subscription',
                 'test',
                 )
  readonly_fields = ('country',
                     'trial',
                     'trial_period',
                     )
  search_fields = ('id',
                   'domain',
                   'custom_store_name',
                   )
  actions = ('check_shopper',
             'check_coupon',
             'check_order',
             'restore_webdav',
             )

  def check_coupon(modeladmin, request, selected):
    return TemplateResponse(request, template_name, context)
```

>  How to sort by one of the custom list_display fields that has no database field

http://stackoverflow.com/questions/2168475/django-admin-how-to-sort-by-one-of-the-custom-list-display-fields-that-has-no-d


--------------------------------------------

#### Django Model

1. Notice the power of the class `queryset()`

2. Using `Choices`
```python
# define PLANS here as a list
subscription = models.CharField(max_length=16, default='trial',
                                db_index=True, choices=PLANS)
```

3. Data Migration
https://docs.djangoproject.com/en/1.8/topics/migrations/

4. Backward Data Migration
http://stackoverflow.com/questions/5814190/backwards-migration-with-django-south

5. Performing Raw SQL
https://docs.djangoproject.com/en/1.8/topics/db/sql/

6. How do I do a not equal in Django queryset filtering?
http://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering

7. How to do a less than or equal to filter in Django queryset?
http://stackoverflow.com/questions/10040143/how-to-do-a-less-than-or-equal-to-filter-in-django-queryset

--------------------------------------------

#### Django Templates and tags

> What is Template Context Processor

In some cases, we want to create a global variable for Django. For example, the platform nouns:

```python
if shopify:
	coupon, collection
if bc:
	reward, catagary
```

It is not  a good practice to use if else everywhere in the Django template. Therefore, we can introduce a global variable for Django template. And this is called Template Context Processor.
`apps/common/context_processors.py`

The pages that make use of Template Context Processor have to have `request` available.

> How to customize Django tags and templates

`apps/dashboard/templatetags/dashboard_extras.py`

Django context processor
https://docs.djangoproject.com/en/1.8/ref/templates/api/
--------------------------------------------

#### Django middleware

https://pypi.python.org/pypi/django-htmlmin
